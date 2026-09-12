#!/usr/bin/env bash
# Copy generated project.md files into a local clone of push @ etsy branch.
set -euo pipefail
PUSH_REPO="${1:-$HOME/src/push}"
BRANCH="cursor/etsy-store-automation-f219"
SRC="$(cd "$(dirname "$0")/.." && pwd)/project-files/push/cursor-etsy-store-automation-f219/ai-agent-team/products"

if [[ ! -d "$PUSH_REPO/.git" ]]; then
  echo "Usage: $0 /path/to/push-clone"
  exit 1
fi
cd "$PUSH_REPO"
git fetch origin "$BRANCH" 2>/dev/null || true
git checkout "$BRANCH"
for dir in "$SRC"/*/; do
  slug="$(basename "$dir")"
  cp "$dir/project.md" "ai-agent-team/products/$slug/project.md"
  echo "copied $slug"
done
echo "Done. Review with: git status && git diff"
