# Python MCP Server

This folder contains MCP servers built with the official **Python SDK** (FastMCP).

## Quick Start

```bash
# From the python-server directory
uv venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
uv add "mcp[cli]"
```

## Current Servers

| Server | Description | Status |
|--------|-------------|--------|
| `hello_world.py` | Minimal "Hello World" MCP server | 🟡 Ready for first lecture |

## Running a server with MCP Inspector

```bash
# Install inspector globally once
npx @modelcontextprotocol/inspector

# Then run your server
uv run python hello_world.py
```

Or configure it in Claude Desktop / Cursor.
