#!/usr/bin/env bash
# Apply project.md commit to local push clone when cloud agent cannot push to push repo.
set -euo pipefail
PUSH_REPO="${1:-.}"
PATCH="$(cd "$(dirname "$0")/.." && pwd)/patches/push-etsy-project-md-28files.patch"
cd "$PUSH_REPO"
git fetch origin cursor/etsy-store-automation-f219
git checkout cursor/etsy-store-automation-f219
git am "$PATCH" || { echo "If am fails, try: git apply --3way $PATCH"; exit 1; }
echo "Applied. Push with: git push -u origin HEAD:cursor/etsy-project-md-1753"
echo "Then open PR into cursor/etsy-store-automation-f219 on GitHub."
