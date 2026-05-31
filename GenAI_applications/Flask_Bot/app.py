from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json.get("message", "").lower()

    if "hello" in user_message:
        response = "Hello! Welcome to Library Management System."

    elif "book" in user_message:
        response = "Available books: Python, Java, SQL, Flask, AI, Data Science."

    elif "python" in user_message:
        response = "Python Programming book is available in Rack A1."

    elif "java" in user_message:
        response = "Java Programming book is available in Rack A2."

    elif "issue" in user_message:
        response = "Books can be issued using your student ID."

    elif "return" in user_message:
        response = "Books must be returned within 15 days."

    elif "fine" in user_message:
        response = "Fine is Rs.10 per day after due date."

    elif "timing" in user_message:
        response = "Library is open from 9 AM to 6 PM."

    elif "contact" in user_message:
        response = "Contact Librarian at library@college.com"

    else:
        response = "Sorry, I can help with books, issue, return, timing, fine and contact information."

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)