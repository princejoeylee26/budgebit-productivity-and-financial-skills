#!/usr/bin/env bash
# Copy shared reference files into every skill that uses them.
# Each skill must stay self-contained (Claude.ai uploads skills one by one),
# so shared files are copied, never linked. Edit shared/, then run this.
set -euo pipefail
cd "$(dirname "$0")/.."
version=$(tr -d '[:space:]' < VERSION)
sed -i.bak -E "s/^\*\*Installed version: .*\*\*$/**Installed version: ${version}**/" shared/updates.md && rm -f shared/updates.md.bak
for skill in hachibu hachibu-money hachibu-memory hachibu-review hachibu-improve; do
  mkdir -p ".claude/skills/$skill/references"
  for f in shared/*.md; do
    cp "$f" ".claude/skills/$skill/references/$(basename "$f")"
  done
done
echo "shared files synced"
