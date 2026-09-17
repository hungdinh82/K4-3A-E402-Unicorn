#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")/.."
TASK_CARGO_BIN="${TASK_CARGO_BIN:-/Users/phongnguyen/.cargo/bin}"
SDKROOT="${SDKROOT:-/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk}" \
PATH="$TASK_CARGO_BIN:$PATH" \
npm run tauri build -- --bundles app "$@"
# Tauri's linker signature does not seal copied resources on this Command Line
# Tools setup. Re-sign the development bundle after resources are in place.
TASK_APP="src-tauri/target/release/bundle/macos/VietNote.app"
if [[ -d "$TASK_APP" ]]; then
  codesign --force --deep --sign - "$TASK_APP"
  codesign --verify --deep --strict "$TASK_APP"
fi
