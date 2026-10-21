# Prompt log

The exam asks for instances where agent output was corrected, challenged, or rejected.
Add one entry each time that happens, newest at the bottom.

Format: `date · who · prompt · what we corrected or rejected, and why`

<!-- Template, copy below this line:
- YYYY-MM-DD · name · "prompt text or summary" · what the agent produced, what we changed or rejected, and why
-->

- 2026-09-30 · CK · /plan Implement tasks/001-probe.md · Approved the plan without reviewing it; a post-hoc review found the spec omitted MET's caching requirement (Terms of Service) → task 002
- 2026-10-21 · CK · `./harness/run.sh --offline` (task 003) · Both rehearsal runs passed with different wording. The agent flagged that the fixture covers 30 Sep–1 Oct, so the offline summary describes a stale forecast; nothing in our checks looks at dates or clock times → W44 evaluation
