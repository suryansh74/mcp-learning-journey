# Python MCP Server

This folder contains MCP servers built with the official **Python SDK** (FastMCP).

## Quick Start

```bash
# From the python-server directory
uv venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

# Install dependencies only (no package build)
uv sync
```

## Current Servers

| Server | Description | Status |
|--------|-------------|--------|
| `hello_world.py` | Minimal "Hello World" MCP server with 2 tools | ✅ Ready |

## Running the server

### Option 1: Direct run
```bash
uv run python hello_world.py
```

### Option 2: With MCP Inspector (recommended for testing)
```bash
# In one terminal start the inspector
npx @modelcontextprotocol/inspector

# Then in another terminal (or through the inspector UI) run:
uv run python hello_world.py
```

### Option 3: Claude Desktop / Cursor
Add this to your Claude Desktop config (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "hello-world": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/mcp-learning-journey/python-server",
        "run",
        "python",
        "hello_world.py"
      ]
    }
  }
}
```

Replace `/absolute/path/to/...` with the real path on your machine.
