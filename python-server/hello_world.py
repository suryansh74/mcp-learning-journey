"""
Minimal MCP Server - Hello World
Using MCP Python SDK v2 (MCPServer)
"""

from mcp.server import MCPServer
import requests
import os
from dotenv import load_dotenv

load_dotenv()
openWeatherAPIKey = os.getenv("OPEN_WEATHER_API_KEY")
grokAPIKey = os.getenv("GROQ_API_KEY")

# Create the MCP server instance
mcp = MCPServer("hello-world")


@mcp.tool()
def get_weather(city: str) -> str:
    """Get the current weather for a given city.

    Args:
        city: Name of the city (e.g. "Warsaw", "London", "New York")
    """
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": openWeatherAPIKey,
        "units": "metric",  # Celsius
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return f"Error: Could not fetch weather for '{city}'. {response.json().get('message', '')}"

    data = response.json()

    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    return (
        f"Weather in {data['name']}:\n"
        f"- Condition: {weather}\n"
        f"- Temperature: {temp}°C (feels like {feels_like}°C)\n"
        f"- Humidity: {humidity}%\n"
        f"- Wind Speed: {wind_speed} m/s"
    )


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
