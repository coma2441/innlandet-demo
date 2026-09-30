# Task 001: Probe the MET Norway forecast for Hamar

## Goal
`python3 harness/probe.py` fetches the next hours of forecast for Hamar and writes `out/probe.json`.

## Context
- API: https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=60.79&lon=11.07
- Terms of service: https://api.met.no/doc/TermsOfService (requests must carry an identifying User-Agent)
- Output format: whatever `eval/check_probe.py` accepts. Read it; do not change it.
  Each item: `title` (short human-readable line), `date` (ISO 8601 time from the API), `air_temperature` (°C).

## Constraints
- Do not edit anything in `eval/`.
- User-Agent: `innlandet-demo/0.1 github.com/coma2441/innlandet-demo` (identifies the app without personal data).
- Save the raw API response to `fixtures/met_hamar.json`. With `--offline`, read that file instead of calling the API.
- Python 3 standard library only (`urllib`, `json`). No new dependencies.
- Keep the text in UTF-8 (Norwegian characters: æ, ø, å).

## Acceptance (all must pass)
- `python3 harness/probe.py && python3 eval/check_probe.py` prints `PASS`
- `python3 harness/probe.py --offline && python3 eval/check_probe.py` prints `PASS`
- The check failed before this task started (red first)

## Out of scope
Summaries, scheduling, anything with an LLM (later tasks).
