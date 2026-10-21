#!/usr/bin/env bash
# Stop hook: the agent may not finish while a check fails.
# Exit 2 sends stderr back to the agent. One retry only: if this hook already blocked, let it stop.
cd "${CLAUDE_PROJECT_DIR:-.}"
grep -q '"stop_hook_active": *true' && exit 0
[ -f out/probe.json ] || exit 0                 # nothing produced yet: nothing to check
python3 eval/check_probe.py >&2 || exit 2
[ -f out/summary.md ] || exit 0
python3 eval/check_summary.py >&2 || exit 2
