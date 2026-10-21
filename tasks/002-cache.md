# Task 002: Cache MET responses (terms of service)

## Goal
Repeat live runs of `harness/probe.py` do not download the forecast again until it expires.

## Context
- Terms of service: https://api.met.no/doc/TermsOfService (use the met-api skill)
- MET sends `Expires` and `Last-Modified`. Before `Expires`: no request. After: send
  `If-Modified-Since`; a `304 Not Modified` means reuse the saved response.
- Found in review of task 001 (docs/prompt-log.md, 2026-09-30).

## Constraints
- Do not edit anything in `eval/`.
- Python 3 standard library only. Cache metadata next to the fixture, e.g. `fixtures/met_hamar.meta.json`.
- `--offline` behaviour is unchanged.

## Acceptance (all must pass)
- Two live runs in a row: the second makes no HTTP request (it says so on stdout)
- `python3 harness/probe.py && python3 eval/check_probe.py` prints `PASS`
- `python3 harness/probe.py --offline && python3 eval/check_probe.py` prints `PASS`

## Out of scope
Scheduling. Nothing runs on a schedule until this task is merged.
