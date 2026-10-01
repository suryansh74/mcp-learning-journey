"""
MCP client demo.

This file is the client, not the server. It does not import tools from
hello_world.py. It starts that file as another process and talks to it
over stdio (stdin/stdout), which is how Claude Desktop and Cursor connect
to a local MCP server.

Run from python-server/:

    uv run python client.py
"""

import asyncio
from pathlib import Path

from mcp import Client
from mcp.client.stdio import StdioServerParameters

SERVER_DIR = Path(__file__).resolve().parent

# How to launch the server. The client never calls add_numbers() itself.
server = StdioServerParameters(
    command="uv",
    args=["run", "python", "hello_world.py"],
    cwd=str(SERVER_DIR),
)


def text_of(result) -> str:
    """Pull plain text out of a tool or prompt result."""
    blocks = getattr(result, "content", None) or []
    parts = [block.text for block in blocks if getattr(block, "text", None)]
    if parts:
        return "\n".join(parts)
    structured = getattr(result, "structured_content", None)
    return str(structured if structured is not None else result)


async def main() -> None:
    print("Client starting the server as a separate process...")
    print("  command: uv run python hello_world.py")
    print(f"  cwd: {SERVER_DIR}\n")

    async with Client(server) as client:
        info = client.server_info
        name = info.name if info else "unknown"
        print(f"Connected to server: {name}")
        print(f"Protocol: {client.protocol_version}\n")

        tools = await client.list_tools()
        print("Tools (work the server can do):")
        for tool in tools.tools:
            print(f"  - {tool.name}: {tool.description}")

        resources = await client.list_resources()
        print("\nResources (data the server can read):")
        for resource in resources.resources:
            print(f"  - {resource.uri}")

        prompts = await client.list_prompts()
        print("\nPrompts (reusable instructions):")
        for prompt in prompts.prompts:
            print(f"  - {prompt.name}: {prompt.description}")

        print("\nCalling tool add_numbers(2, 3)...")
        added = await client.call_tool("add_numbers", {"a": 2, "b": 3})
        print(f"  is_error={getattr(added, 'is_error', None)}")
        print(f"  result: {text_of(added)}")

        print("\nCalling tool say_hello...")
        hello = await client.call_tool("say_hello", {"name": "Suryansh"})
        print(f"  result: {text_of(hello)}")

        print("\nReading resource config://server...")
        config = await client.read_resource("config://server")
        first = config.contents[0]
        print(f"  {getattr(first, 'text', first)}")

        print("\nGetting prompt code_review...")
        review = await client.get_prompt(
            "code_review",
            arguments={"language": "python", "code": "def add(a, b): return a + b"},
        )
        print(f"  {text_of(review.messages[0])}")

    print("\nClient closed. The server process exited with it.")


if __name__ == "__main__":
    asyncio.run(main())
