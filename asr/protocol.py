"""Loopback newline JSON. PCM payloads: base64 little-endian Float32, 16 kHz mono."""
import json
MAX_LINE = 1024 * 1024

def encode(message):
    return (json.dumps(message, ensure_ascii=False, allow_nan=False) + '\n').encode('utf-8')

def decode(line):
    if len(line) > MAX_LINE:
        raise ValueError('Oversized protocol message')
    message = json.loads(line)
    if not isinstance(message, dict) or 'type' not in message:
        raise ValueError('Expected typed object')
    return message
