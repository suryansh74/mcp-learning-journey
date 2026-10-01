# Python MCP Server

This folder contains MCP servers built with the official **Python SDK** (`MCPServer`) and a separate client.

## Quick Start

```bash
# From the python-server directory
uv venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
uv sync
```

## Current files

| File | Role | Status |
| --- | --- | --- |
| hello_world.py | Server. Exposes tools, resources, and prompts. Waits for a client. | Ready |
| client.py | Client. Starts the server as another process and talks over stdio. | Ready |
| chatbot.py | Host. An LLM agent that uses the server tools. | Ready |

## Client vs server

- `hello_world.py` is the server. Run it only if a host such as Claude Desktop, Cursor, or MCP Inspector will connect to it.
- `client.py` is a client. It does not import the tool functions. It launches `hello_world.py` and calls tools over MCP.

```bash
uv run python client.py
```

You should see the tool list, `add_numbers(2, 3)` returning 5, a resource read, and a prompt. No API key is required for this demo (`get_weather` is listed but not called).

## Running the server for a host

### Option 1: Direct run

```bash
uv run python hello_world.py
```

### Option 2: With MCP Inspector

```bash
npx @modelcontextprotocol/inspector
# point the inspector at: uv run python hello_world.py
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
