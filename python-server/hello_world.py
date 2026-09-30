"""
MCP Server - Tools + Resources
Using MCP Python SDK v2 (MCPServer)
"""

from mcp.server import MCPServer
import requests
import os
from datetime import datetime
from dotenv import load_dotenv
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mcp-server")

load_dotenv()
openWeatherAPIKey = os.getenv("OPEN_WEATHER_API_KEY")

mcp = MCPServer("hello-world")

THIS_FOLDER = Path(__file__).parent.absolute()
ACTIVITY_LOG_FILE = THIS_FOLDER / "activity.log"


# ======================
# TOOLS
# ======================


@mcp.tool()
def get_weather(city: str) -> str:
    """Get the current weather for a given city."""
    logger.info(f"get_weather called with city={city}")

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": openWeatherAPIKey,
        "units": "metric",
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

    # write log to file
    with open(ACTIVITY_LOG_FILE, "a") as f:
        f.write(
            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
            f"Weather tool called → city={city}, temp={temp}°C, humidity={humidity}%\n"
        )

    return (
        f"Weather in {data['name']}:\n"
        f"- Condition: {weather}\n"
        f"- Temperature: {temp}°C (feels like {feels_like}°C)\n"
        f"- Humidity: {humidity}%\n"
        f"- Wind Speed: {wind_speed} m/s"
    )


@mcp.tool()
def say_hello(name: str = "World") -> str:
    """A simple tool that greets the user."""
    logger.info(f"say_hello called with name={name}")

    # write log to file
    with open(ACTIVITY_LOG_FILE, "a") as f:
        f.write(
            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
            f"say_hello tool called → name={name}\n"
        )
    return f"Hello, {name}! 👋 Welcome to the MCP Learning Journey."


@mcp.tool()
def add_numbers(a: float, b: float) -> float:
    """Add two numbers together."""
    logger.info(f"add_numbers called with a={a} and b={b}")
    with open(ACTIVITY_LOG_FILE, "a") as f:
        f.write(
            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
            f"add_numbers tool called → a={a}, b={b}\n"
        )
    return a + b


# ======================
# RESOURCES
# ======================


# resoureces are like static site generation very less frequently changes
# whereas tool are like server side rendering
@mcp.resource("config://server")
def get_server_config() -> str:
    """Returns basic information about this MCP server."""
    return """{
  "name": "hello-world",
  "version": "0.2.0",
  "description": "Learning MCP - Tools + Resources",
  "author": "Suryansh",
  "features": ["tools", "resources"]
}"""


@mcp.resource("file://activity.log")
def activity_log() -> str:
    """Read logs from activity log file"""
    try:
        with open(ACTIVITY_LOG_FILE, "r") as f:
            content = f.read()
            return content if content.strip() else "No activity logged yet."
    except FileNotFoundError:
        return "Activity log file not found."


# this tool is for access activity_log resource
@mcp.tool()
def read_activity_log() -> str:
    """Read the recent activity log of tool calls."""
    try:
        with open(ACTIVITY_LOG_FILE, "r") as f:
            content = f.read()
            return content if content.strip() else "No activity logged yet."
    except FileNotFoundError:
        return "Activity log file not found."


@mcp.resource("time://current")
def get_current_time() -> str:
    """Returns the current date and time."""
    now = datetime.now()
    return f"Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}"


@mcp.resource("greeting://{name}")
def personalized_greeting(name: str) -> str:
    """A personalized greeting resource (example of a resource template)."""
    return f"Hello {name}! This greeting came from a Resource, not a Tool."


# ======================
# Prompt
# ======================
@mcp.prompt()
def code_review(language: str, code: str) -> str:
    """Review code and suggest improvements."""
    return f"""
You are an expert {language} developer.
Please review the following code and suggest improvements:

{language}
{code}
"""


if __name__ == "__main__":
    if not Path(ACTIVITY_LOG_FILE).exists():
        Path(ACTIVITY_LOG_FILE).touch()
    mcp.run(transport="stdio")
