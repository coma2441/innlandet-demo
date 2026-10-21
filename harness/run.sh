#!/usr/bin/env bash
# The chain: probe -> check -> summarise (claude -p, up to 3 tries) -> check.
# Usage: ./harness/run.sh [--offline] [--dry-run]
set -euo pipefail
cd "$(dirname "$0")/.."

OFFLINE=""; DRY=""
for arg in "$@"; do
  case "$arg" in
    --offline) OFFLINE="--offline" ;;
    --dry-run) DRY=1 ;;
    *) echo "unknown option: $arg" >&2; exit 64 ;;
  esac
done

if [ -n "$DRY" ]; then
  src=$([ -n "$OFFLINE" ] && echo "fixtures/met_hamar.json" || echo "api.met.no")
  echo "[1] probe      $src -> out/probe.json     check: eval/check_probe.py"
  echo "[2] summarise  out/probe.json -> out/summary.md     check: eval/check_summary.py (max 3 tries)"
  echo "[3] publish    (not built yet)"
  exit 0
fi

echo "[1] probe"
python3 harness/probe.py $OFFLINE
python3 eval/check_probe.py

echo "[2] summarise"
FEEDBACK="none"
for attempt in 1 2 3; do
  rm -f out/summary.md
  claude -p "$(cat harness/prompts/summarise.md)

Previous check output (fix this): $FEEDBACK" \
    --permission-mode dontAsk --allowedTools "Read,Edit(/out/**)" \
    --max-budget-usd 0.50 > out/summarise.log
  if FEEDBACK=$(python3 eval/check_summary.py 2>&1); then
    echo "$FEEDBACK (attempt $attempt)"
    exit 0
  fi
  echo "attempt $attempt failed: $(echo "$FEEDBACK" | tail -1)" >&2
done
echo "summarise: no passing summary after 3 attempts" >&2
exit 1
