"""MCP server exposing the Hamar forecast as one tool.

Usage: .venv/bin/python harness/mcp_met.py [--offline]   (stdio; started by .mcp.json)
"""
import sys

from mcp.server.mcpserver import MCPServer  # mcp >= 2 (in 1.x: mcp.server.fastmcp.FastMCP)

from probe import fetch, load_fixture, to_items

OFFLINE = "--offline" in sys.argv
server = MCPServer("met")


@server.tool()
def forecast(hours: int = 24) -> list[dict]:
    """Hourly forecast for Hamar: title (local time, temperature, symbol), ISO time, air temperature in C."""
    raw = load_fixture() if OFFLINE else fetch()
    return to_items(raw)[: max(1, min(hours, 24))]


if __name__ == "__main__":
    server.run()  # stdio: never print to stdout
