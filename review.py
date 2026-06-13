import os

USE_LLM = False

def read_diff():
    try:
        with open("diff.txt", "r") as f:
            return f.read()
    except Exception as e:
        return f"Error reading diff: {str(e)}"


def basic_review(diff):
    if not diff.strip():
        return "No changes detected in PR."

    return f"""
### AI Code Review (Basic)

- Diff length: {len(diff)} characters

Observations:
- Changes detected in repository
- Review logic not yet enabled

Next Steps:
- Integrate LLM analysis
- Add pattern validation
"""


def llm_review(diff):
    try:
        from openai import OpenAI

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        prompt = f"""
You are a senior backend engineer reviewing design pattern implementations.

Focus:
- Correct use of design patterns
- SOLID principles
- Code clarity
- Over-engineering

Code diff:
{diff}
"""

        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=[{"role": "user", "content": prompt}],
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"LLM Error:\n{str(e)}"


def main():
    diff = read_diff()

    if USE_LLM:
        review = llm_review(diff)
    else:
        review = basic_review(diff)

    # CRITICAL: always create this file
    try:
        with open("review.txt", "w") as f:
            f.write(review)
        print("review.txt created successfully")
    except Exception as e:
        print(f"Failed to write review.txt: {str(e)}")


if __name__ == "__main__":
    main()
