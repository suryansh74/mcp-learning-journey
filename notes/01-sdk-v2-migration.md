# Note: MCP Python SDK v2 Changes

**Date**: 2026-09-28

## What happened
When we ran `uv add "mcp[cli]"`, it installed **MCP Python SDK v2**.

In v2:
- `FastMCP` was renamed to `MCPServer`
- Import path changed from `mcp.server.fastmcp` → `mcp.server` (or `mcp.server.mcpserver`)

## Correct import (v2)
```python
from mcp.server import MCPServer

mcp = MCPServer("my-server")
```

## Old import (v1 - no longer works)
```python
from mcp.server.fastmcp import FastMCP   # ❌ ModuleNotFoundError
```

## Official migration guide
https://py.sdk.modelcontextprotocol.io/v2/migration/
