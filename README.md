# innlandet-demo

A course project for two people: an agentic workflow that turns the MET Norway forecast for Hamar
into a short, checked summary for commuters. See SPEC.md.

## Setup

Requires Python 3.11+, git and Claude Code (`claude --version`).

```
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt   # only for the MCP server and SDK
```

## Offline run (fixtures, no network)

```
./harness/run.sh --offline --dry-run   # print the stages, touch nothing
./harness/run.sh --offline             # probe -> check -> summarise (claude -p) -> check
```

## Normal run (live MET API)

```
./harness/run.sh
```

## Tools

- `.mcp.json` starts `harness/mcp_met.py --offline`, which exposes the tool `forecast(hours)`.
  Claude Code asks once to approve project MCP servers; `/mcp` shows the status.
- `harness/sdk_summarise.py`: the same summarise stage as a Python program (agent SDK + MCP tool).
- `.claude/agents/reviewer.md`: a read-only subagent that checks a diff against a task's Acceptance.

## Layout

- `SPEC.md`: problem, users, definition of success
- `tasks/`: one task per file, each with an acceptance check
- `harness/`: stages, prompts, tools
- `eval/`: checks
- `fixtures/`: saved real inputs
- `docs/meetings/`: meeting notes
- `docs/prompt-log.md`: log of agent output we corrected or rejected
