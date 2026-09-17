# VietNote desktop

VietNote is a single Tauri + React + TypeScript desktop application for macOS and Windows. The shared UI and meeting-note workflow live in `src/`, native capture and local AI commands live in `src-tauri/`, and the protocol-compatible ASR worker lives in `asr/`.

## Run and build

```bash
npm install
./scripts/bootstrap.sh
./scripts/dev-tauri.sh
```

Build a macOS application bundle:

```bash
./scripts/build-tauri.sh
```

On Windows, install Node.js LTS, Rust with the MSVC toolchain, and Python 3.12, then run:

```powershell
.\scripts\bootstrap-windows.ps1
```

## Meeting-note pipeline

```text
System audio / microphone
→ bounded VAD segments
→ Groq Whisper Large V3 ASR (local fallback)
→ bounded technical-term normalization
→ transcript segments with stable IDs and timestamps
→ structured meeting summary
→ evidence links back to transcript segments
```

When `GROQ_API_KEY` is available, Vietnamese, English, and Mandarin use Groq's accuracy-first `whisper-large-v3` through the OpenAI-compatible audio transcription API. Without the key, Vietnamese uses local PhoWhisper-medium and English/Mandarin use local Whisper Turbo. Raw ASR text is retained next to cleaned text so term corrections remain auditable.

Choose **Groq** in **Cài đặt → Tóm tắt & dịch AI** and enter the API key there. The desktop app stores provider keys separately in macOS Keychain or Windows Credential Manager. Updating the Groq key also restarts the ASR worker. Stop recording before changing a key. Keys are never saved to notes, localStorage, or the repository. You can alternatively provide the Groq key before starting the app:

```bash
export GROQ_API_KEY="gsk_..."
./scripts/dev-tauri.sh
```

Optional overrides are `ASR_BACKEND=local|groq|auto` (default `auto`), `GROQ_ASR_MODEL` (default `whisper-large-v3`), and `GROQ_BASE_URL`. Never commit the API key to the repository. Groq requests receive mono 16 kHz WAV utterances; silence commits naturally and continuous speech is capped at 10 seconds to improve context and avoid excessive requests.

The summarizer and translator can switch between **9Router** and **Groq** from one provider dropdown. 9Router defaults to the local OpenAI-compatible endpoint at `http://127.0.0.1:20128/v1/chat/completions` with `cx/gpt-5.5`; its endpoint, model ID, and optional dashboard API key are configurable. The key can also be supplied through `NINE_ROUTER_API_KEY`. Groq uses `openai/gpt-oss-120b` with low reasoning effort and a completion budget that leaves room for the final answer. The same securely stored Groq key is reused for ASR without exposing it to React. The summary separates final decisions, tentative decisions, unresolved topics, action items, open questions, and deferred work. Important items must reference real transcript segment IDs; invalid evidence IDs are removed, and unsupported important items are discarded. The final saved note is regenerated from the full transcript instead of trusting accumulated realtime summaries.

Notes are stored in the Tauri application data directory. Existing string-based notes remain readable; newly generated notes additionally store the structured summary and transcript segments.

## Tests

```bash
npm test
npm run build
.venv/bin/python -m unittest discover -s tests -v
```

Acceptance test 20 câu cho đánh giá sản phẩm thật:

```bash
# Đọc tests/VietNote_ACCEPTANCE_TESTS.md và nói VN01–VN20 vào VietNote
python3 scripts/score_vietnote_acceptance.py /absolute/path/to/results.json
```

Danh sách câu nằm ở `tests/vietnote_acceptance_cases.json`; tiêu chí và ngưỡng MVP nằm ở `tests/VietNote_ACCEPTANCE_TESTS.md`.

ASR debug with a mono 16 kHz PCM16 WAV:

```bash
./scripts/debug.sh /absolute/path/to/input.wav
```

## Current limits

- Audio is not persisted, so evidence links jump to and highlight transcript text; they do not play audio.
- Microphone and system audio maintain separate ASR contexts, but there is no speaker diarization. The summarizer may assign an owner only when a person's name is explicit in the transcript.
- Technical-term normalization is intentionally conservative. Add observed variants with positive and negative regression tests instead of broad prose rewrites.
- DRM-protected system audio may be unavailable to the operating-system capture API.
- The local summary API and local model runtime must be available separately.
# VietNote
# VietNote
