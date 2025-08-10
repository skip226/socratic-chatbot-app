import random
import re


STOPWORDS = {
    'the', 'is', 'a', 'an', 'and', 'or', 'but', 'if', 'in', 'on', 'to',
    'with', 'of', 'for', 'as', 'at', 'by', 'be', 'this', 'that'
}


def extract_keywords(text: str) -> str:
    """Return a simplified string of key words from user input."""
    words = re.findall(r"\b\w+\b", text.lower())
    keywords = [w for w in words if w not in STOPWORDS]
    if not keywords:
        return text.strip()
    # Use up to last three keywords to keep context short
    return " ".join(keywords[-3:])


def socratic_prompt(text: str) -> str:
    """Generate a Socratic-style question with a mentor tone."""
    key = extract_keywords(text)
    templates = [
        "Why do you think {key}?",
        "What leads you to believe {key}?",
        "How does {key} fit into the bigger picture?",
        "What would change if {key} were different?",
        "Can you think of an example that illustrates {key}?",
        "What might be the consequences of {key}?",
        "How might someone else view {key}?"
    ]
    template = random.choice(templates)
    return f"Hmm. {template.format(key=key)}"


def main() -> None:
    print("Wise Mentor: Greetings, seeker. How may I assist you today?")
    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()  # move to next line
            user_input = "exit"
        if user_input.lower() in {"exit", "quit"}:
            print("Wise Mentor: Farewell. Continue your journey with curiosity.")
            break
        response = socratic_prompt(user_input)
        print(f"Wise Mentor: {response}")


if __name__ == "__main__":
    main()
