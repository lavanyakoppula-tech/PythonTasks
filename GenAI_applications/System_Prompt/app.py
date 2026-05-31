import os
from dotenv import load_dotenv
from templates.prompts import CLASSIFIER_PROMPT

# --------------------------
# Load Environment Variables
# --------------------------
load_dotenv()

# --------------------------
# Temporary Rule-Based Classifier
# (Works without Gemini errors)
# --------------------------

LIBRARY_KEYWORDS = [
    "book",
    "books",
    "author",
    "library",
    "member",
    "borrow",
    "return",
    "issued",
    "catalog",
    "availability"
]


def is_library_related(question):

    question = question.lower()

    for keyword in LIBRARY_KEYWORDS:

        if keyword in question:
            return True

    return False


def main():

    print("=" * 50)
    print("LIBRARY MANAGEMENT QUESTION CLASSIFIER")
    print("=" * 50)

    print("\nType 'exit' to stop")

    while True:

        question = input(
            "\nEnter Question: "
        )

        if question.lower() == "exit":
            print("\nApplication Closed")
            break

        print("\nSystem Prompt Loaded:")
        print(CLASSIFIER_PROMPT[:200] + "...")

        result = is_library_related(question)

        if result:

            print("\nClassifier Output : YES")
            print("Result : Library Related Question")

        else:

            print("\nClassifier Output : NO")
            print("Result : Not Library Related")


if __name__ == "__main__":
    main()