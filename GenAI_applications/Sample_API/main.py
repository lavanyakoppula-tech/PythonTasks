from flask import Flask, render_template, request, jsonify
import os

from dotenv import load_dotenv
from google import genai

# Load .env variables
load_dotenv()

# Read Gemini API Key
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# Create Gemini Client
client = genai.Client(
    api_key=GEMINI_API_KEY
)

# Create Flask App
app = Flask(__name__)


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# AI Response Route
@app.route("/ai-response", methods=["POST"])
def ai_response():

    try:

        # Read JSON data from frontend
        data = request.get_json()

        question = data.get("question")

        if not question:
            return jsonify({
                "response": "Please enter a question."
            })

        # Gemini API Call
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=question
        )

        return jsonify({
            "question": question,
            "response": response.text
        })

    except Exception as e:

        print("ERROR:", str(e))

        return jsonify({
            "response": f"Gemini API Error: {str(e)}"
        })


if __name__ == "__main__":
    app.run(debug=True)