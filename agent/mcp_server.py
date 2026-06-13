from mcp.server.fastmcp import FastMCP

from agent.tools import (
    detect_patterns,
    check_singleton,
    check_factory,
    check_pr_size,
    check_class_count,
    check_naming,
    get_lines
)

mcp = FastMCP("code-review")


@mcp.tool()
def get_diff() -> str:
    with open("diff.txt", "r") as f:
        return f.read()


@mcp.tool()
def analyze_patterns(diff: str) -> list:
    return detect_patterns(diff)


@mcp.tool()
def run_checks(diff: str) -> dict:
    lines = get_lines(diff)

    results = {
        "singleton": check_singleton(diff, lines),
        "factory": check_factory(diff, lines),
        "size": check_pr_size(lines),
        "classes": check_class_count(lines),
        "naming": check_naming(lines),
    }

    return results


if __name__ == "__main__":
    mcp.run()
