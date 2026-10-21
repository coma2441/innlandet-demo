# harness/

- Python 3 standard library only, except `mcp_met.py` and `sdk_summarise.py` (see requirements.txt).
- `mcp_met.py` talks over stdio: never print to stdout; log to stderr.
- Agent prompts live in `prompts/`. After changing one, run `./harness/run.sh --offline`.
