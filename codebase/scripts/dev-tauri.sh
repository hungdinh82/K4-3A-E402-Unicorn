#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")/.."
TASK_CARGO_BIN="${TASK_CARGO_BIN:-/Users/phongnguyen/.cargo/bin}"
TASK_SDK_ROOT="${SDKROOT:-$(xcrun --sdk macosx --show-sdk-path)}"
TASK_COMPAT_SDK="/Library/Developer/CommandLineTools/SDKs/MacOSX15.4.sdk"
TASK_SYSTEM_TBD="$TASK_SDK_ROOT/usr/lib/libSystem.B.tbd"
if [[ -d "$TASK_COMPAT_SDK" && -f "$TASK_SYSTEM_TBD" ]] &&
   { ! grep -q 'arm64-macos' "$TASK_SYSTEM_TBD" || grep -q 'arm64e\.x1-macos' "$TASK_SYSTEM_TBD"; }; then
  TASK_SDK_ROOT="$TASK_COMPAT_SDK"
fi
SDKROOT="$TASK_SDK_ROOT" \
PATH="$TASK_CARGO_BIN:$PATH" \
npm run tauri dev
