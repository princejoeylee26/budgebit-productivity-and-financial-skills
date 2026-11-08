#!/usr/bin/env bash
# Copy shared reference files into every skill that uses them.
# Each skill must stay self-contained (Claude.ai uploads skills one by one),
# so shared files are copied, never linked. Edit shared/, then run this.
set -euo pipefail
cd "$(dirname "$0")/.."
for skill in hachibu hachibu-money hachibu-memory hachibu-review; do
  mkdir -p ".claude/skills/$skill/references"
  cp shared/budgebit-tools.md ".claude/skills/$skill/references/budgebit-tools.md"
done
echo "shared files synced"
