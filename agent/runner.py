from agent.agent import CodeReviewAgent


def read_diff():
    try:
        with open("diff.txt", "r") as f:
            return f.read()
    except Exception as e:
        return str(e)


def main():
    diff = read_diff()

    agent = CodeReviewAgent()
    agent.observe(diff)
    agent.think()
    review = agent.act()

    with open("review.txt", "w") as f:
        f.write(review)


if __name__ == "__main__":
    main()
