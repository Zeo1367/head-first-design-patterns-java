from agent.tools import (
    get_lines,
    detect_patterns,
    check_singleton,
    check_factory,
    check_pr_size,
    check_class_count,
    check_naming
)


class CodeReviewAgent:
    def __init__(self):
        self.diff = ""
        self.issues = []
        self.score = 10
        self.patterns = []

    def observe(self, diff: str):
        self.diff = diff

    def think(self):
        self.issues = []
        self.score = 10

        if not self.diff.strip():
            self.issues.append("No changes detected")
            self.score -= 2
            return

        lines = get_lines(self.diff)

        # Tool usage
        self.patterns = detect_patterns(self.diff)

        # Each tool returns issues
        checks = [
            check_singleton(self.diff, lines),
            check_factory(self.diff, lines),
            check_pr_size(lines),
            check_class_count(lines),
            check_naming(lines),
        ]

        for result in checks:
            if result:
                self.issues.extend(result)
                self.score -= len(result)

        self.score = max(self.score, 0)

    def act(self):
        if not self.issues:
            return f"""### Code Review Agent

Score: {self.score}/10
Patterns: {', '.join(self.patterns) if self.patterns else 'None'}

No major issues detected.
"""

        formatted = "\n".join(f"- {i}" for i in self.issues)

        return f"""### Code Review Agent

Score: {self.score}/10
Patterns: {', '.join(self.patterns) if self.patterns else 'None'}

Issues:
{formatted}
"""
