"""20 ms energy VAD. Bounded segments, pre-roll, and overlap only at forced cuts."""
from collections import deque
import numpy as np
import re
import unicodedata

RATE = 16000
FRAME = 320

class AudioBuffer:
    def __init__(self, threshold=0.006, warmup_frames=15, max_segment_seconds=3.2):
        self.threshold = threshold
        self.noise_floor = 0.0
        self.warmup_remaining = warmup_frames
        self.warmup_energies = []
        self.pending = np.empty(0, dtype=np.float32)
        self.pre = deque(maxlen=15)
        self.active = []
        self.onset = 0
        self.silent = 0
        self.voiced = 0
        self.overlap = False
        self.max_segment_frames = max(1, round(max_segment_seconds * RATE / FRAME))

    @property
    def speech_threshold(self):
        # A fixed threshold mistakes steady microphone/room noise for speech. Keep
        # the original floor for quiet rooms, but require substantially more
        # energy than the noise measured at the beginning of each capture.
        # Do not cap this value: a cap made loud, steady room noise look like
        # uninterrupted speech and forced a bogus ASR job every 3.2 seconds.
        # The lower absolute floor still lets short/quiet speech through in a
        # quiet room.
        return max(self.threshold, self.noise_floor * 1.6)

    def observe_noise(self, energy):
        if self.noise_floor == 0:
            self.noise_floor = energy
        else:
            # Only quiet frames reach here, so a slow EMA follows changing room
            # noise without allowing speech to raise the gate immediately.
            self.noise_floor = self.noise_floor * 0.97 + energy * 0.03

    def finish_warmup(self):
        """Estimate room noise without learning an opening utterance as noise.

        A steady signal during calibration is usually fan/room noise, while
        speech changes energy substantially from frame to frame.  In the latter
        case, keep the absolute speech gate and let the buffered warmup frames
        become pre-roll.  This lets somebody speak immediately after pressing
        Start instead of silencing the whole opening sentence.
        """
        energies = np.asarray(self.warmup_energies, dtype=np.float32)
        low, middle, high = np.percentile(energies, (10, 50, 90))
        relative_spread = (high - low) / max(middle, 1e-6)
        measured_floor = float(np.percentile(energies, 30))
        if relative_spread >= .25 and high >= self.threshold:
            self.noise_floor = min(measured_floor, self.threshold / 1.6)
        else:
            self.noise_floor = measured_floor

    def feed(self, samples):
        self.pending = np.concatenate((self.pending, samples))
        output = []
        while len(self.pending) >= FRAME:
            frame, self.pending = self.pending[:FRAME].copy(), self.pending[FRAME:]
            # Remove DC offset before measuring energy. Some microphone paths
            # carry a stable offset/low-frequency bias that is not speech.
            centered = frame - float(np.mean(frame))
            energy = float(np.sqrt(np.mean(centered * centered)))
            if self.warmup_remaining:
                self.warmup_energies.append(energy)
                self.pre.append(frame)
                self.warmup_remaining -= 1
                if not self.warmup_remaining:
                    self.finish_warmup()
                continue
            speech = energy >= self.speech_threshold
            if not self.active:
                if not speech:
                    self.onset = 0
                    self.observe_noise(energy)
                    self.pre.append(frame)
                    continue
                self.onset += 1
                self.pre.append(frame)
                # Require 60 ms above the adaptive gate. This prevents keyboard
                # clicks and short capture glitches from invoking Whisper.
                if self.onset < 3:
                    continue
                self.active = list(self.pre)
                self.pre.clear()
                self.voiced = self.onset
                self.onset = 0
            else:
                self.active.append(frame)
            self.voiced += int(speech)
            self.silent = 0 if speech else self.silent + 1
            forced = len(self.active) >= self.max_segment_frames
            ended = self.silent >= 25  # 500 ms trailing silence
            if forced or ended:
                if self.voiced >= (25 if self.overlap else 8):  # keep short phrases; onset filtering rejects clicks
                    output.append((np.concatenate(self.active), self.overlap))
                tail = self.active[-20:] if forced and speech else []
                self.active = list(tail)
                self.overlap = bool(tail)
                self.voiced = 0
                self.silent = 0
        return output

def deduplicate(previous, current, overlapping):
    current = current.strip()
    if not overlapping:
        return current
    # Ignore punctuation while matching a suffix/prefix; preserve output punctuation.
    def normalized(s):
        return [(c, i) for i, c in enumerate(s) if c.isalnum()]
    old, new = normalized(previous[-60:]), normalized(current)
    for count in range(min(len(old), len(new)), 1, -1):
        if [c for c, _ in old[-count:]] == [c for c, _ in new[:count]]:
            return current[new[count-1][1]+1:].lstrip('，。！？、,.!? ')
    return current


def is_repetitive(text):
    normalized = ''.join(c for c in text if c.isalnum())
    if len(normalized) < 12:
        return False
    match = re.search(r"(.{1,12})\1{3,}", normalized)
    return bool(match and len(match.group()) / len(normalized) > 0.6)


def is_implausibly_fast(text, audio_seconds, language):
    """Reject Vietnamese decoder text that cannot fit in the captured speech."""
    if language != 'vi':
        return False
    syllables = len(text.split())
    return syllables >= 8 and syllables > 8 * max(0.5, audio_seconds - 0.35) + 1


def is_hallucination_signature(text, language):
    """Reject common Whisper silence/noise completions, not general meeting text."""
    if language != 'vi':
        return False
    folded = unicodedata.normalize('NFD', text.lower())
    folded = ''.join(c for c in folded if unicodedata.category(c) != 'Mn')
    folded = folded.replace('đ', 'd')
    words = ' '.join(re.findall(r'[a-z0-9]+', folded))
    if words.startswith('cam on cac ban da theo doi'):
        return True
    promotes_channel = ('subscribe' in words or 'dang ky' in words or 'dang ki' in words)
    if promotes_channel and 'kenh' in words:
        return True
    if 'ung ho kenh' in words:
        return True
    # Whisper often splits one hallucinated promo across adjacent ASR jobs.
    return words.startswith('de khong bo lo nhung video')


def normalize_meeting_terms(text, language):
    """Apply an auditable, bounded glossary; never rewrite general prose."""
    if language == 'vi':
        text = re.sub(r'\b(?:đảo|báo)\s+sát\s+chưa\s+hoàn\s+tất\b',
                      'khảo sát chưa hoàn tất', text, flags=re.IGNORECASE)
        text = re.sub(
            r'^\s*điều\s+kiểm\s+soát\s+chưa\s+hoàn\s+tất'
            r'(?=\s+hiện\s+tại\s+nhóm\b)',
            'khảo sát chưa hoàn tất', text, flags=re.IGNORECASE)
    # Corrections below are deliberately limited to canonical technical names
    # or stable phonetic confusions observed in mixed Vietnamese/English speech.
    glossary = (
        (r'\b(?:land|lang)\s*graph\b', 'LangGraph'),
        (r'\blang\s*chain\b', 'LangChain'),
        (r'\brag\s*(?:us|as)\b', 'RAGAS'),
        (r'\bcross\s*encoder\b', 'CrossEncoder'),
        (r'\bfast\s*api\b', 'FastAPI'),
        (r'\bqdrant\b', 'Qdrant'),
        (r'\bchroma\b', 'Chroma'),
        (r'\bopen\s*ai\b', 'OpenAI'),
        (r'\bgpt[ -]?4o\b', 'GPT-4o'),
        (r'\blanggraph\b', 'LangGraph'),
        (r'\blangchain\b', 'LangChain'),
        (r'\bragas\b', 'RAGAS'),
        (r'\bllm\b', 'LLM'),
        (r'\brag\b', 'RAG'),
        (r'\bapi\b', 'API'),
    )
    for pattern, canonical in glossary:
        text = re.sub(pattern, canonical, text, flags=re.IGNORECASE)
    return text
