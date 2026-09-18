#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")/.."
if [[ $# == 0 ]]; then
  # Synthetic Mandarin fixture only; the app does not implement TTS/playback.
  say -v Tingting '这个产品最大的优势是价格很便宜。今天我们测试中文语音识别。' \
      -o tests/mandarin.wav --file-format=WAVE --data-format=LEI16@16000
fi
.venv/bin/python asr/server.py --debug-wav "${1:-tests/mandarin.wav}"
