# innlandet-demo

Two-person course project building an agentic workflow. See SPEC.md.

## Checks
No application code yet, so there are no checks. Once the stack is chosen, put the single
command that runs lint and tests here (e.g. `make check`).

## Layout
tasks/ task definitions · harness/ agent runner · eval/ evaluation suite
fixtures/ test inputs · docs/meetings/ notes · docs/prompt-log.md corrections log

## Rules
- Never edit anything under eval/ without asking first.
- No personal data anywhere in the repo (fixtures, logs, prompts, meeting notes). Use synthetic data.
- Never read or print .env; add new variables to .env.example instead.
- When agent output is corrected, challenged, or rejected, log it in docs/prompt-log.md.
