#!/usr/bin/env bash
# Build one zip per skill in dist/, for uploading to claude.ai (Settings > Capabilities > Skills).
set -euo pipefail
cd "$(dirname "$0")/.."
rm -rf dist && mkdir -p dist
for d in skills/*/; do
  n=$(basename "$d")
  (cd skills && zip -qr "../dist/$n.zip" "$n")
done
ls -1 dist
