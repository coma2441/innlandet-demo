"""Stage 2 as a program: the agent SDK with the met MCP tool instead of out/probe.json.

Usage: .venv/bin/python harness/sdk_summarise.py   (writes out/summary_sdk.md)
"""
import asyncio

from claude_agent_sdk import ClaudeAgentOptions, ResultMessage, query

PROMPT = """Call the forecast tool for the next 24 hours in Hamar, Norway.
Write out/summary_sdk.md: one paragraph of 30-60 words in English for someone commuting in Hamar.
Give the lowest and highest air temperature with their local times, exactly as in the data, followed by °C.
Write only that file."""

opts = ClaudeAgentOptions(
    mcp_servers={"met": {"command": ".venv/bin/python", "args": ["harness/mcp_met.py", "--offline"]}},
    allowed_tools=["mcp__met__forecast", "Write(/out/**)", "Edit(/out/**)"],
    permission_mode="dontAsk",
    max_budget_usd=0.50,
)


async def main():
    async for msg in query(prompt=PROMPT, options=opts):
        if isinstance(msg, ResultMessage):
            print(f"done: {msg.subtype}, cost ${msg.total_cost_usd or 0:.3f}")


asyncio.run(main())
