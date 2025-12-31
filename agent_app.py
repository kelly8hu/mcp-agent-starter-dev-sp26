"""
Run a CLI agent powered by the OpenAI Agents SDK.
The agent can call real tools exposed by a local MCP server (mcp_server.py) via stdio.

You should ONLY edit:
- AGENT_NAME
- AGENT_INSTRUCTIONS
- (Optional) MODEL

DO NOT restructure the agent loop or MCP connection.
"""

import asyncio
from pathlib import Path

from dotenv import load_dotenv
from agents import Agent, Runner
from agents.mcp import MCPServerStdio

# Load OPENAI_API_KEY from .env (students create .env from .env.example)
load_dotenv()

# ---- Student-editable knobs ----
AGENT_NAME = "Creative Mini-Agent"
AGENT_INSTRUCTIONS = (
    "You are a creative but scoped assistant. "
    "Use MCP tools when they help. Keep outputs short, concrete, and demo-friendly. "
    "When you propose something, include a small scope (1 core feature + 1 optional twist)."
)

# You can set an explicit model, or rely on the default model configured by the SDK/env.
# If you do set one, keep it cheap/fast for class.
MODEL = "gpt-4o-mini"
# --------------------------------


async def main() -> None:
    project_dir = Path(__file__).parent
    server_path = project_dir / "mcp_server.py"

    # Spawn the MCP server as a subprocess and connect via stdin/stdout. :contentReference[oaicite:1]{index=1}
    async with MCPServerStdio(
        name="Local MCP Server",
        params={
            "command": "python",
            "args": [str(server_path)],
        },
    ) as server:
        agent = Agent(
            name=AGENT_NAME,
            instructions=AGENT_INSTRUCTIONS,
            model=MODEL,
            mcp_servers=[server],
        )

        print("\n✅ Agent ready. Type 'exit' to quit.\n")
        while True:
            user = input("You: ").strip()
            if user.lower() in {"exit", "quit"}:
                break

            # Runner.run() implements the agent loop (LLM call → tool calls → repeat → final output). :contentReference[oaicite:2]{index=2}
            result = await Runner.run(agent, input=user)
            print(f"\nAgent: {result.final_output}\n")


if __name__ == "__main__":
    asyncio.run(main())
