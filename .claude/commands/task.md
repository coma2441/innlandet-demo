---
description: Run one task through the loop (spec, plan, run, verify)
argument-hint: NNN
disable-model-invocation: true
---
Read tasks/$ARGUMENTS-*.md. Propose a plan and wait for my approval before editing anything.
After implementing, run every command under "## Acceptance" and paste the output.
Do not touch eval/. If I rejected or corrected anything, add a line to docs/prompt-log.md.
