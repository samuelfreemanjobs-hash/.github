#!/usr/bin/env bash
# Apply HUNTER launch prep patch to a local -build-ai-agents-with-claude clone.
set -euo pipefail
REPO_ROOT="${1:?Usage: $0 /path/to/-build-ai-agents-with-claude}"
PATCH="$(cd "$(dirname "$0")/.." && pwd)/patches/hunter-launch-prep-c763.patch"
cd "$REPO_ROOT"
git checkout cursor/autonomous-hunter-os-54da 2>/dev/null || { git fetch origin cursor/autonomous-hunter-os-54da && git checkout cursor/autonomous-hunter-os-54da; }
git checkout -B cursor/hunter-launch-prep-c763
git apply "$PATCH"
echo "✅ Patch applied on branch cursor/hunter-launch-prep-c763 in $REPO_ROOT"
echo "   Next: npm ci && npm run verify-launch && npm run health"
