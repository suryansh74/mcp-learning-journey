"""MCP server for the remote-host demo.

Listens on Streamable HTTP so a Next.js host can connect by URL.
DNS-rebinding checks are off so a changing tunnel hostname is accepted.
Put auth in front of this later. Do not leave that off on a public box.
"""

import os

from mcp.server import MCPServer
from mcp.server.transport_security import TransportSecuritySettings

mcp = MCPServer("remote-hello")


@mcp.tool()
def add_numbers(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


@mcp.tool()
def say_hello(name: str = "World") -> str:
    """Greet someone."""
    return f"Hello, {name}. This reply came from the Docker MCP server."


@mcp.resource("config://server")
def server_config() -> str:
    """Static description of this server."""
    return "remote-hello MCP server, streamable-http, no auth yet"


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host=os.environ.get("MCP_HOST", "0.0.0.0"),
        port=int(os.environ.get("MCP_PORT", "8000")),
        transport_security=TransportSecuritySettings(
            enable_dns_rebinding_protection=False,
        ),
    )
