# innlandet-demo

Two-person course project: an agentic workflow that turns the MET Norway forecast for Hamar
into a short, checked summary. See SPEC.md.

## Checks
`./harness/run.sh --offline` runs every stage on fixtures and its check. Run it before saying "done".

## Layout
tasks/ one task per file · harness/ stages, prompts, tools · eval/ checks
fixtures/ saved real inputs · docs/meetings/ notes · docs/prompt-log.md corrections log

## Rules
- Never edit anything under eval/ without asking first.
- No personal data anywhere in the repo. Use synthetic data.
- Never read or print .env; add new variables to .env.example instead.
- MET API details: use the met-api skill.
- When agent output is corrected, challenged, or rejected, log it in docs/prompt-log.md.
