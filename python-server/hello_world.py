"""
Minimal MCP Server - Hello World
This is the starting point. We will expand it lecture by lecture.
"""

from mcp.server.fastmcp import FastMCP

# Create the MCP server instance
mcp = FastMCP("hello-world")

@mcp.tool()
def say_hello(name: str = "World") -> str:
    """
    A simple tool that greets the user.
    
    Args:
        name: The name of the person to greet
    """
    return f"Hello, {name}! 👋 Welcome to the MCP Learning Journey."


@mcp.tool()
def add_numbers(a: float, b: float) -> float:
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
    """
    return a + b


if __name__ == "__main__":
    # Run the server using stdio transport (default for local development)
    mcp.run(transport="stdio")
