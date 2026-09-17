"""Real socket/MLX smoke test with realtime PCM and trailing silence; no capture permission."""
import base64
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import threading
import time
import uuid
import wave
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'asr'))
from protocol import encode, decode

def main():
    token = uuid.uuid4().hex
    env = dict(os.environ, ASR_TOKEN=token)
    log = open(ROOT/'logs/socket-smoke.log', 'w')
    process = subprocess.Popen([str(ROOT/'.venv/bin/python'), '-u', str(ROOT/'asr/server.py')],
                               stdout=subprocess.PIPE, stderr=log, env=env, text=True)
    events = []
    ready = threading.Event()
    def reader():
        for line in process.stdout:
            log.write(line); log.flush()
            try:
                obj = json.loads(line)
                if obj.get('type') == 'ready': events.append(obj); ready.set()
            except ValueError: pass
    threading.Thread(target=reader, daemon=True).start()
    try:
        assert ready.wait(120), 'Worker did not become READY within 120 seconds'
        with socket.create_connection(('127.0.0.1', events[0]['port'])) as conn:
            conn.sendall(encode(dict(type='hello', token=token)))
            conn.sendall(encode(dict(type='reset', generation=1)))
            responses = []
            def receive():
                with conn.makefile('rb') as stream:
                    for line in stream:
                        responses.append(decode(line))
            thread = threading.Thread(target=receive, daemon=True)
            thread.start()
            with wave.open(str(ROOT/'tests/mandarin.wav')) as w:
                samples = np.frombuffer(w.readframes(w.getnframes()), '<i2').astype('<f4')/32768
            samples = np.concatenate((samples, np.zeros(16000, '<f4')))
            for offset in range(0, len(samples), 1600):
                chunk = samples[offset:offset+1600]
                conn.sendall(encode(dict(type='audio', pcm=base64.b64encode(chunk.tobytes()).decode(), captured_at=time.time())))
                time.sleep(len(chunk)/16000)
            deadline = time.monotonic()+15
            while time.monotonic() < deadline and len([r for r in responses if r.get('text')]) < 2:
                time.sleep(.1)
            count = len([r for r in responses if r.get('text')])
            assert count >= 2, responses
            for _ in range(40):
                conn.sendall(encode(dict(type='audio', pcm=base64.b64encode(np.zeros(1600, '<f4').tobytes()).decode(), captured_at=time.time())))
                time.sleep(.1)
            assert len([r for r in responses if r.get('text')]) == count, 'Unexpected transcripts during silence'
            assert all(r.get('generation') == 1 for r in responses if r.get('type') == 'transcript')
            request_id = uuid.uuid4().hex
            conn.sendall(encode(dict(type='synthesize', id=request_id, generation=1,
                                     text='Bắc Hải rất gần Việt Nam.')))
            deadline = time.monotonic()+15
            while time.monotonic() < deadline and not any(
                    r.get('type') == 'tts_end' and r.get('id') == request_id for r in responses):
                time.sleep(.05)
            speech = [r for r in responses if r.get('id') == request_id]
            ending = next((r for r in speech if r.get('type') == 'tts_end'), None)
            assert ending, speech
            chunks = [np.frombuffer(base64.b64decode(r['pcm']), '<f4')
                      for r in speech if r.get('type') == 'tts_audio']
            spoken = np.concatenate(chunks)
            assert len(spoken) > 4800 and np.isfinite(spoken).all()
            assert float(np.sqrt(np.mean(spoken**2))) > .001
            with wave.open(str(ROOT/'logs/socket-smoke-tts.wav'), 'wb') as output:
                output.setnchannels(1); output.setsampwidth(2); output.setframerate(48000)
                output.writeframes((np.clip(spoken, -1, 1)*32767).astype('<i2').tobytes())
            conn.shutdown(socket.SHUT_RDWR)
            thread.join(3)
        process.wait(timeout=15)
        assert process.returncode == 0, process.returncode
        print(json.dumps(responses, ensure_ascii=False, indent=2))
        print('PASS: persistent ASR + ZeroTTS worker, authenticated socket, realtime PCM, generation, silence, streamed speech, clean disconnect')
    finally:
        if process.poll() is None:
            process.terminate()
            process.wait(timeout=15)
        log.close()

if __name__ == '__main__': main()
