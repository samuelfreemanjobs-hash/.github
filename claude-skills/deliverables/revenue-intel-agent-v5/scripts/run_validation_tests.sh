#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
VALIDATOR="$ROOT/scripts/validate_run.py"

python3 "$VALIDATOR" "$ROOT/fixtures/valid-sample-run.json"

if python3 "$VALIDATOR" "$ROOT/fixtures/invalid-math-run.json"; then
  echo "Expected invalid-math-run.json to fail validation" >&2
  exit 1
fi

echo "All validation tests passed."
