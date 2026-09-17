import sys
import time
import base64
import json
import socket
import threading
import unittest
from types import SimpleNamespace
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'asr'))
import numpy as np
from audio_buffer import (AudioBuffer, deduplicate, is_repetitive,
                          is_implausibly_fast, is_hallucination_signature,
                          normalize_meeting_terms, RATE)
from protocol import encode, decode
from server import GroqRecognizer, Recognizer
from install_phowhisper import mlx_config, mlx_key
import server

def synthetic_speech(seconds, amplitude=.05):
    count = int(RATE * seconds)
    t = np.arange(count, dtype=np.float32) / RATE
    envelope = .55 + .45 * np.sin(2 * np.pi * 3 * t) ** 2
    voice = amplitude * envelope * (np.sin(2 * np.pi * 180 * t)
                                    + .35 * np.sin(2 * np.pi * 360 * t))
    voice[:min(count, int(RATE * .35))] = 0
    return voice.astype(np.float32)

def immediate_speech(seconds, amplitude=.05):
    count = int(RATE * seconds)
    t = np.arange(count, dtype=np.float32) / RATE
    envelope = .35 + .65 * np.sin(2 * np.pi * 4 * t) ** 2
    return (amplitude * envelope * (np.sin(2 * np.pi * 180 * t)
            + .35 * np.sin(2 * np.pi * 360 * t))).astype(np.float32)

class PipelineTests(unittest.TestCase):
    def test_silence(self):
        self.assertEqual(AudioBuffer().feed(np.zeros(RATE*30, np.float32)), [])
    def test_steady_microphone_noise_sets_adaptive_floor(self):
        vad = AudioBuffer()
        # This is above the old fixed 0.008 gate and previously generated a
        # forced ASR segment every 3.2 seconds.
        noise = np.random.default_rng(7).normal(0, .012, RATE * 12).astype(np.float32)
        self.assertEqual(vad.feed(noise), [])
        self.assertGreater(vad.speech_threshold, .012)
    def test_speech_beginning_during_calibration_is_kept(self):
        vad = AudioBuffer()
        signal = np.concatenate((immediate_speech(1.0),
                                 np.zeros(RATE, np.float32)))
        results = vad.feed(signal)
        self.assertEqual(len(results), 1)
        self.assertGreaterEqual(len(results[0][0]), int(RATE * .8))
        self.assertLessEqual(vad.speech_threshold, vad.threshold * 1.05)
    def test_speech_and_bounded_segments(self):
        vad = AudioBuffer()
        signal = np.concatenate((synthetic_speech(11), np.zeros(RATE)))
        results = []
        for chunk in np.array_split(signal, 240): results.extend(vad.feed(chunk))
        self.assertGreaterEqual(len(results), 3)
        self.assertTrue(all(len(x) <= RATE*5 for x, _ in results))
        self.assertTrue(results[1][1])
    def test_cloud_segment_limit_is_configurable(self):
        vad = AudioBuffer(max_segment_seconds=10)
        signal = np.concatenate((synthetic_speech(11), np.zeros(RATE)))
        results = vad.feed(signal)
        self.assertTrue(results)
        self.assertTrue(all(len(x) <= RATE * 10.1 for x, _ in results))
    def test_short_quiet_phrase_is_kept(self):
        vad = AudioBuffer()
        signal = np.concatenate((synthetic_speech(.9, amplitude=.010),
                                 np.zeros(RATE, np.float32)))
        results = vad.feed(signal)
        self.assertEqual(len(results), 1)
        self.assertGreaterEqual(len(results[0][0]), int(RATE * .8))
    def test_fragmentation(self):
        vad = AudioBuffer()
        self.assertEqual(vad.feed(np.ones(159, np.float32)*.1), [])
        self.assertEqual(len(vad.pending), 159)
    def test_short_overlap_tail(self):
        vad = AudioBuffer()
        signal = np.concatenate((synthetic_speech(3.4), np.zeros(RATE)))
        self.assertEqual(len(vad.feed(signal)), 1)
    def test_repetitive_hallucination(self):
        self.assertTrue(is_repetitive('试'*100))
        self.assertTrue(is_repetitive('谢谢观看'*20))
        self.assertFalse(is_repetitive('这个产品最大的优势是价格很便宜'))
    def test_implausibly_fast_vietnamese_hallucination(self):
        outro = 'Hãy subscribe cho kênh Ghiền Mì Gõ Để không bỏ lỡ những video hấp dẫn'
        self.assertTrue(is_implausibly_fast(outro, 1.8, 'vi'))
        self.assertFalse(is_implausibly_fast('Xin chào các bạn', 1.8, 'vi'))
        self.assertFalse(is_implausibly_fast(outro, 1.8, 'zh'))
    def test_known_vietnamese_noise_hallucinations(self):
        self.assertTrue(is_hallucination_signature(
            'Cảm ơn các bạn đã theo dõi và hẹn gặp lại.', 'vi'))
        self.assertTrue(is_hallucination_signature(
            'Các bạn hãy đăng kí cho kênh lalaschool để không bỏ lỡ những video hấp dẫn', 'vi'))
        self.assertTrue(is_hallucination_signature(
            'Các bạn hãy đăng ký kênh để ủng hộ kênh của mình nhé.', 'vi'))
        self.assertTrue(is_hallucination_signature(
            'Để không bỏ lỡ những video hấp dẫn', 'vi'))
        self.assertFalse(is_hallucination_signature(
            'Cảm ơn anh Nam đã theo dõi tiến độ dự án.', 'vi'))
        self.assertFalse(is_hallucination_signature(
            'Cảm ơn các bạn đã theo dõi và hẹn gặp lại.', 'zh'))
    def test_narrow_meeting_term_corrections(self):
        self.assertEqual(normalize_meeting_terms('đảo sát chưa hoàn tất.', 'vi'),
                         'khảo sát chưa hoàn tất.')
        self.assertEqual(normalize_meeting_terms(
            'điều kiểm soát chưa hoàn tất hiện tại nhóm đã nhận.', 'vi'),
            'khảo sát chưa hoàn tất hiện tại nhóm đã nhận.')
        self.assertEqual(normalize_meeting_terms(
            'Điều kiểm soát chưa hoàn tất.', 'vi'),
            'Điều kiểm soát chưa hoàn tất.')
    def test_technical_glossary_repairs_only_known_terms(self):
        self.assertEqual(
            normalize_meeting_terms('land graph kết hợp rag us qua fast api và qdrant', 'vi'),
            'LangGraph kết hợp RAGAS qua FastAPI và Qdrant')
        self.assertEqual(
            normalize_meeting_terms('We discussed langchain, cross encoder, and gpt 4o.', 'en'),
            'We discussed LangChain, CrossEncoder, and GPT-4o.')
    def test_protocol(self):
        obj = dict(type='transcript', text='这个产品很便宜', asr_ms=713)
        self.assertEqual(decode(encode(obj)), obj)
        with self.assertRaises(ValueError): decode(b'[]')
    def test_deduplication(self):
        self.assertEqual(deduplicate('这个产品，价格便宜。', '价格便宜，而且很好。', True), '而且很好。')
        self.assertEqual(deduplicate('你好', '你好', False), '你好')
        self.assertEqual(deduplicate('你好', '你好', True), '')
    def test_vietnamese_recognition_uses_selected_language(self):
        recognizer = Recognizer.__new__(Recognizer)
        recognizer.model = 'zh-model'
        recognizer.models = {'zh': 'zh-model', 'vi': 'vi-model'}
        recognizer.context = ''
        selected = []
        def fake_transcribe(audio, **kwargs):
            selected.append((kwargs['language'], kwargs['path_or_hf_repo'],
                             kwargs['initial_prompt']))
            return {'segments': [{'text': 'Xin chào', 'no_speech_prob': 0,
                                  'avg_logprob': 0, 'compression_ratio': 1}]}
        recognizer.transcribe = fake_transcribe
        result = recognizer.recognize(np.ones(RATE, np.float32), False, time.time(), 'vi')
        self.assertEqual(selected, [('vi', 'vi-model', None)])
        self.assertEqual(result['text'], 'Xin chào')
    def test_english_recognition_uses_turbo_with_english_decoder(self):
        recognizer = Recognizer.__new__(Recognizer)
        recognizer.model = 'turbo-model'
        recognizer.models = {'zh': 'turbo-model', 'en': 'turbo-model', 'vi': 'vi-model'}
        recognizer.context = ''
        selected = []
        def fake_transcribe(audio, **kwargs):
            selected.append((kwargs['language'], kwargs['path_or_hf_repo']))
            return {'segments': [{'text': 'We need more context before translating.',
                                  'no_speech_prob': 0, 'avg_logprob': 0,
                                  'compression_ratio': 1}]}
        recognizer.transcribe = fake_transcribe
        result = recognizer.recognize(np.ones(RATE, np.float32), False,
                                      time.time(), 'en')
        self.assertEqual(selected, [('en', 'turbo-model')])
        self.assertEqual(result['text'], 'We need more context before translating.')
    def test_groq_recognizer_calls_audio_transcription_with_wav(self):
        calls = []
        class Transcriptions:
            def create(self, **kwargs):
                calls.append(kwargs)
                return SimpleNamespace(text='Xin chào Lang Graph')
        recognizer = GroqRecognizer.__new__(GroqRecognizer)
        recognizer.client = SimpleNamespace(audio=SimpleNamespace(transcriptions=Transcriptions()))
        recognizer.model_name = 'whisper-large-v3'
        recognizer.context = ''
        result = recognizer.recognize(np.ones(RATE, np.float32) * .01,
                                      False, time.time(), 'vi')
        self.assertEqual(calls[0]['model'], 'whisper-large-v3')
        self.assertEqual(calls[0]['language'], 'vi')
        self.assertTrue(calls[0]['file'][1].startswith(b'RIFF'))
        self.assertEqual(result['text'], 'Xin chào LangGraph')
    def test_recognizer_does_not_publish_known_noise_hallucination(self):
        recognizer = Recognizer.__new__(Recognizer)
        recognizer.model = 'fallback-model'
        recognizer.models = {'vi': 'fallback-model'}
        recognizer.context = ''
        recognizer.transcribe = lambda audio, **kwargs: {'segments': [{
            'text': 'Cảm ơn các bạn đã theo dõi và hẹn gặp lại.',
            'no_speech_prob': 0, 'avg_logprob': 0, 'compression_ratio': 1,
        }]}
        result = recognizer.recognize(np.ones(RATE * 3, np.float32), False,
                                      time.time(), 'vi')
        self.assertEqual(result['text'], '')
    def test_phowhisper_conversion_maps_huggingface_weights(self):
        self.assertEqual(mlx_key('model.decoder.layers.0.encoder_attn.q_proj.weight'),
                         'decoder.blocks.0.cross_attn.query.weight')
        self.assertEqual(mlx_key('model.encoder.conv1.weight'), 'encoder.conv1.weight')
        self.assertEqual(mlx_config(dict(num_mel_bins=80, max_source_positions=1500,
                                         d_model=1024, encoder_attention_heads=16,
                                         encoder_layers=24, vocab_size=51865,
                                         max_target_positions=448,
                                         decoder_attention_heads=16, decoder_layers=24))['n_audio_state'], 1024)
    def test_system_and_microphone_keep_separate_asr_context(self):
        ready = threading.Event()
        port = []
        contexts = []
        original_log = server.log
        def capture_log(message):
            if isinstance(message, str) and message.startswith('{'):
                obj = json.loads(message)
                if obj.get('type') == 'ready':
                    port.append(obj['port'])
                    ready.set()
        class StubRecognizer:
            context = ''
            def recognize(self, audio, overlap, started, language):
                contexts.append(self.context)
                self.context += 'x'
                return {'type': 'transcript', 'text': 'x'}
        class StubSynthesizer:
            display_name = 'test'
        server.log = capture_log
        worker = threading.Thread(target=server.serve,
                                  args=(StubRecognizer(), StubSynthesizer(), 'test-token'), daemon=True)
        try:
            worker.start()
            self.assertTrue(ready.wait(5))
            with socket.create_connection(('127.0.0.1', port[0]), timeout=5) as connection:
                connection.settimeout(5)
                with connection.makefile('rb') as incoming:
                    connection.sendall(encode({'type': 'hello', 'token': 'test-token'}))
                    self.assertEqual(decode(incoming.readline())['type'], 'connected')
                    connection.sendall(encode({'type': 'reset', 'generation': 1, 'language': 'vi'}))
                    samples = np.concatenate((synthetic_speech(1),
                                              np.zeros(RATE, np.float32)))
                    payload = base64.b64encode(samples.tobytes()).decode('ascii')
                    for source in ('system', 'microphone', 'system'):
                        connection.sendall(encode({'type': 'audio', 'source': source,
                                                   'pcm': payload, 'captured_at': time.time()}))
                        while True:
                            response = decode(incoming.readline())
                            if response['type'] == 'transcript': break
                        self.assertEqual(response['source'], source)
                        self.assertEqual(response['generation'], 1)
            worker.join(3)
            self.assertFalse(worker.is_alive())
            self.assertEqual(contexts, ['', '', 'x'])
        finally:
            server.log = original_log

if __name__ == '__main__': unittest.main()
