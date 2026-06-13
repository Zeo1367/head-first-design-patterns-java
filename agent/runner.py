import asyncio
from mcp.client import ClientSession


async def main():
    async with ClientSession("stdio", ["python", "-m", "agent.mcp_server"]) as session:

        diff = await session.call_tool("get_diff", {})

        patterns = await session.call_tool("analyze_patterns", {
            "diff": diff
        })

        checks = await session.call_tool("run_checks", {
            "diff": diff
        })

        issues = []
        score = 10

        for key, value in checks.items():
            if value:
                issues.extend(value)
                score -= len(value)

        score = max(score, 0)

        if not issues:
            review = f"""### MCP Code Review Agent

Score: {score}/10
Patterns: {', '.join(patterns) if patterns else 'None'}

No major issues detected.
"""
        else:
            formatted = "\n".join(f"- {i}" for i in issues)

            review = f"""### MCP Code Review Agent

Score: {score}/10
Patterns: {', '.join(patterns) if patterns else 'None'}

Issues:
{formatted}
"""

        with open("review.txt", "w") as f:
            f.write(review)


if __name__ == "__main__":
    asyncio.run(main())
