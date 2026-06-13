import os


class CodeReviewAgent:
    def __init__(self):
        self.diff = ""
        self.issues = []

    # Step 1: Observe
    def observe(self, diff: str):
        self.diff = diff

    # Step 2: Think
    def think(self):
        self.issues = []

        if not self.diff.strip():
            self.issues.append("No changes detected in PR")
            return

        # Rule 1: Singleton pattern check
        if "Singleton" in self.diff:
            if "private static" not in self.diff:
                self.issues.append("Singleton pattern may be incorrectly implemented")

        # Rule 2: Factory pattern misuse
        if "Factory" in self.diff and "new " in self.diff:
            self.issues.append("Possible violation of Factory pattern (direct instantiation found)")

        # Rule 3: Large change warning
        if len(self.diff) > 3000:
            self.issues.append("Large PR detected — consider breaking into smaller commits")

        # Rule 4: General structure
        if "class " in self.diff and "interface " not in self.diff:
            self.issues.append("Consider using interfaces for better abstraction (SOLID)")

    # Step 3: Act
    def act(self) -> str:
        if not self.issues:
            return "### Code Review Agent\n\nNo major issues detected."

        formatted_issues = "\n".join(f"- {issue}" for issue in self.issues)

        return f"""### Code Review Agent

Issues Found:
{formatted_issues}
"""


def read_diff():
    try:
        with open("diff.txt", "r") as f:
            return f.read()
    except Exception as e:
        return f"Error reading diff: {str(e)}"


def main():
    diff = read_diff()

    agent = CodeReviewAgent()

    agent.observe(diff)
    agent.think()
    review = agent.act()

    # MUST exist for GitHub Action
    with open("review.txt", "w") as f:
        f.write(review)

    print("Review generated successfully")


if __name__ == "__main__":
    main()
