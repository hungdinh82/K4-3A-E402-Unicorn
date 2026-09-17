$ErrorActionPreference = 'Stop'
Set-Location (Split-Path -Parent $PSScriptRoot)
if (-not (Get-Command py -ErrorAction SilentlyContinue)) { throw 'Python 3.12 is required. Install Python and the py launcher first.' }
py -3.12 -m venv .venv
& .\.venv\Scripts\python.exe -m pip install --upgrade pip
& .\.venv\Scripts\python.exe -m pip install -r asr\requirements-windows.txt
npm install
npm run tauri build
