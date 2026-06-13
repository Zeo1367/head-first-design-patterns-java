def get_lines(diff: str):
    return diff.split("\n")


def detect_patterns(diff: str):
    patterns = []

    if "getInstance" in diff and "static" in diff:
        patterns.append("Singleton")

    if "Factory" in diff and "create" in diff:
        patterns.append("Factory")

    if "interface" in diff and "implements" in diff:
        patterns.append("Strategy/Interface-based")

    return patterns


def check_singleton(diff: str, lines):
    issues = []

    if "Singleton" in diff:
        has_private_constructor = any("private" in l and "()" in l for l in lines)
        has_static_instance = "static" in diff

        if not has_private_constructor or not has_static_instance:
            issues.append("Incorrect Singleton implementation")

    return issues


def check_factory(diff: str, lines):
    issues = []

    factory_lines = [l for l in lines if "Factory" in l]
    new_usage = [l for l in lines if "new " in l]

    if factory_lines and new_usage:
        issues.append("Factory pattern violation: direct object creation detected")

    return issues


def check_pr_size(lines):
    issues = []
    if len(lines) > 200:
        issues.append("Large PR — reduce size")
    return issues


def check_class_count(lines):
    issues = []
    class_count = sum(1 for l in lines if "class " in l)

    if class_count > 3:
        issues.append("Too many classes modified — possible SRP violation")

    return issues


def check_naming(lines):
    issues = []

    for l in lines:
        if "class " in l:
            parts = l.split()
            if len(parts) > 1:
                name = parts[1]
                if len(name) < 3:
                    issues.append(f"Poor class name: {name}")

    return issues
