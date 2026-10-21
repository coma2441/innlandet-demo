# Task 003: Summarise the forecast for a commuter

## Goal
A headless agent stage turns `out/probe.json` into `out/summary.md`, a short English summary
for someone commuting in Hamar.

## Context
- Input: `out/probe.json` from task 001 (run `python3 harness/probe.py --offline` first).
- Runtime prompt: `harness/prompts/summarise.md`. The stage is `claude -p`, not Python code.
- Output check: `eval/check_summary.py`. Read it; do not change it.

## Constraints
- Do not edit anything in `eval/`.
- The stage may read files and write only under `out/`.
- Every temperature in the summary must come from `out/probe.json`. No invented numbers.

## Acceptance (all must pass)
- `python3 harness/probe.py --offline && <summarise stage> && python3 eval/check_summary.py` prints `PASS`
- The check failed before this task started (red first)

## Out of scope
Publishing, scheduling, caching (task 002).
