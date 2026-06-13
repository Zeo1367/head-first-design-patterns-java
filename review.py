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
        self.score = 10  # start perfect, reduce on issues
    
        if not self.diff.strip():
            self.issues.append("No changes detected in PR")
            self.score -= 2
            return
    
        lines = self.diff.split("\n")
    
        # --- Rule 1: Singleton correctness ---
        if "Singleton" in self.diff:
            has_private_constructor = any("private" in l and "()" in l for l in lines)
            has_static_instance = "static" in self.diff
    
            if not has_private_constructor or not has_static_instance:
                self.issues.append("Incorrect Singleton implementation (missing private constructor or static instance)")
                self.score -= 2
    
        # --- Rule 2: Factory misuse ---
        factory_lines = [l for l in lines if "Factory" in l]
        new_usage = [l for l in lines if "new " in l]
    
        if factory_lines and new_usage:
            self.issues.append("Factory pattern violation: direct object creation detected")
            self.score -= 2
    
        # --- Rule 3: Large PR ---
        if len(lines) > 200:
            self.issues.append("Large PR — reduce size for better reviewability")
            self.score -= 1
    
        # --- Rule 4: Too many responsibilities ---
        class_count = sum(1 for l in lines if "class " in l)
        if class_count > 3:
            self.issues.append("Too many classes changed — possible SRP violation")
            self.score -= 1
    
        # --- Rule 5: Missing abstraction ---
        if "class " in self.diff and "interface " not in self.diff:
            self.issues.append("No interface usage — may violate abstraction principles")
            self.score -= 1
    
        # --- Rule 6: Naming issues ---
        for l in lines:
            if "class " in l and len(l.split()) > 1:
                name = l.split()[1]
                if len(name) < 3:
                    self.issues.append(f"Poor class name detected: {name}")
                    self.score -= 1
    
        # clamp score
        self.score = max(self.score, 0)
        self.patterns = self.detect_patterns()

    def detect_patterns(self):
        patterns = []
    
        if "getInstance" in self.diff and "static" in self.diff:
            patterns.append("Singleton")
    
        if "create" in self.diff and "Factory" in self.diff:
            patterns.append("Factory")
    
        if "interface" in self.diff and "implements" in self.diff:
            patterns.append("Strategy/Interface-based")
    
        return patterns

    # Step 3: Act
    def act(self) -> str:
        if not self.issues:
            return f"""### Code Review Agent
    
    Score: {self.score}/10
    
    No major issues detected.
    Patterns Detected: {', '.join(self.patterns) if self.patterns else 'None'}
    """
    
        formatted_issues = "\n".join(f"- {issue}" for issue in self.issues)
    
        return f"""### Code Review Agent
    
    Score: {self.score}/10
    
    Patterns Detected: {', '.join(self.patterns) if self.patterns else 'None'}
    
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
