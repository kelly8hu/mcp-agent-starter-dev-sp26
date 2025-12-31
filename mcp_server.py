"""
A REAL MCP server implemented in Python using FastMCP.
The agent discovers and calls these tools through MCP.

Students MUST:
- Add at least ONE new tool (see TODO below)
- Keep tools small-scope and text-based

No web scraping, no databases, no auth.
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Literal

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("CreativeMCP")


@mcp.tool()
def generate_brief(
    theme: str,
    format: Literal["app idea", "short story", "brand concept", "event"] = "app idea",
    audience: str = "college students",
) -> str:
    """Generate a compact creative brief with clear scope constraints."""
    return (
        "Creative Brief\n"
        f"- Format: {format}\n"
        f"- Theme: {theme}\n"
        f"- Audience: {audience}\n\n"
        "Hook:\n"
        f"- A fresh, memorable angle on '{theme}'.\n\n"
        "Scope (keep small):\n"
        "- 1 core feature / concept\n"
        "- 1 optional twist\n"
        "- Demo in text in under 2 minutes\n"
    )


@mcp.tool()
def save_text(filename: str, content: str) -> str:
    """Save content to ./outputs and return the file path."""
    safe = "".join(ch for ch in filename if ch.isalnum() or ch in ("-", "_", ".", " "))
    if not safe.strip():
        safe = "draft.txt"

    out_dir = Path("outputs")
    out_dir.mkdir(exist_ok=True)

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = out_dir / f"{stamp}_{safe}"
    path.write_text(content, encoding="utf-8")
    return f"Saved: {path.as_posix()}"


# =========================
# TODO (Student): Add 1 new tool below.
# Examples:
# - make_checklist(goal: str, n: int = 5) -> list[str]
# - summarize(text: str, max_bullets: int = 5) -> str
# - name_generator(theme: str, n: int = 10) -> list[str]
# =========================

@mcp.tool()
def make_checklist(goal: str, n: int = 5) -> list[str]:
    """Create a short checklist for achieving a goal."""
    n = max(3, min(int(n), 10))
    items = [f"Define success for: {goal}", "Gather needed inputs/resources"]
    while len(items) < n - 1:
        items.append("Do the next smallest step")
    items.append("Review, refine, and finalize")
    return items


if __name__ == "__main__":
    # Run MCP over stdio (the client spawns this process). :contentReference[oaicite:3]{index=3}
    mcp.run()
