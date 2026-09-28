"""
LangGraph chatbot using the new official langchain.mcp (MCPAdapter)
"""

import asyncio
import os
from pathlib import Path
from dotenv import load_dotenv

from langchain.mcp import MCPAdapter
from langchain.agents import create_agent
from langchain_groq import ChatGroq

load_dotenv()

# Path to your MCP server
SERVER_PATH = Path(__file__).parent / "hello_world.py"


async def main():
    print("Connecting to MCP server...")

    # MCPAdapter automatically launches the server over stdio
    async with MCPAdapter(SERVER_PATH) as adapter:
        tools = await adapter.list_tools()
        print(f"✅ Loaded tools: {[t.name for t in tools]}\n")

        # Create the LLM
        llm = ChatGroq(
            model="openai/gpt-oss-20b",
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_KEY"),
            max_retries=2,
            timeout=30,
        )

        # Create the agent
        agent = create_agent(llm, tools)

        print("Chatbot ready! Type 'quit' to exit.\n")

        while True:
            user_input = input("You: ").strip()
            if user_input.lower() in ["quit", "exit", "q"]:
                break
            if not user_input:
                continue

            result = await agent.ainvoke(
                {"messages": [{"role": "user", "content": user_input}]}
            )

            final_message = result["messages"][-1]
            print(f"\nAssistant: {final_message.content}\n")


if __name__ == "__main__":
    asyncio.run(main())
