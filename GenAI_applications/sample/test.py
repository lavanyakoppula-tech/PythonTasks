import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
print(os.getenv("GEMINI_API_KEY"))

def generate(question: str):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in .env file")

    client = genai.Client(api_key=api_key)

    model = "gemini-2.5-flash"

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=question,
    ):
        if chunk.text:
            print(chunk.text, end="")


if __name__ == "__main__":
    question = input("Enter your question: ")
    generate(question)