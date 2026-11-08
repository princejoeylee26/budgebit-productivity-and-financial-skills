#!/usr/bin/env bash
# Build one zip per skill for upload to Claude.ai (Settings → Capabilities → Skills).
set -euo pipefail
cd "$(dirname "$0")/.."
scripts/sync-shared.sh
mkdir -p dist
for dir in .claude/skills/*/; do
  name=$(basename "$dir")
  (cd .claude/skills && zip -qr "../../dist/$name.zip" "$name" -x '*/__pycache__/*')
  echo "dist/$name.zip"
done
