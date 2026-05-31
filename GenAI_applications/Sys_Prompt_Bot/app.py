from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ---------------------------------------
# Library Keywords
# ---------------------------------------

LIBRARY_KEYWORDS = [
    "book",
    "books",
    "author",
    "authors",
    "member",
    "members",
    "borrow",
    "borrowed",
    "return",
    "returned",
    "library",
    "catalog",
    "availability",
    "issue",
    "issued"
]

# ---------------------------------------
# Question Classifier
# ---------------------------------------

def is_library_related(question):

    question = question.lower()

    for keyword in LIBRARY_KEYWORDS:

        if keyword in question:
            return True

    return False

# ---------------------------------------
# Library Assistant Response
# ---------------------------------------

def generate_response(question):

    question = question.lower()

    # Books

    if "books" in question or "book" in question:

        return """
📚 Library Books Information

Available Books:

1. Python Basics
   Author: Mark Lutz
   Copies Available: 5

2. Clean Code
   Author: Robert C. Martin
   Copies Available: 3

3. Java Programming
   Author: Herbert Schildt
   Copies Available: 4

4. Data Structures
   Author: Narasimha Karumanchi
   Copies Available: 6

5. Database Management Systems
   Author: Raghu Ramakrishnan
   Copies Available: 2

You can ask:
• Who borrowed a book?
• How many copies are available?
• Book author details
"""

    # Members

    elif "member" in question or "members" in question:

        return """
👨‍🎓 Library Member Information

Registered Members:

1. Sai Kumar
   Membership ID: M101

2. Swetha
   Membership ID: M102

3. Ramesh
   Membership ID: M103

4. Priya
   Membership ID: M104

5. Kiran
   Membership ID: M105

Members can:
• Borrow books
• Return books
• View issued books
"""

    # Authors

    elif "author" in question or "authors" in question:

        return """
✍️ Author Information

Available Authors:

• Robert C. Martin
   Book: Clean Code

• Mark Lutz
   Book: Python Basics

• Herbert Schildt
   Book: Java Programming

• Narasimha Karumanchi
   Book: Data Structures

• Raghu Ramakrishnan
   Book: Database Management Systems
"""

    # Borrowed Books

    elif "borrow" in question or "borrowed" in question:

        return """
📖 Borrowed Books

Current Issued Books:

Python Basics
→ Borrowed By: Sai Kumar

Clean Code
→ Borrowed By: Swetha

Java Programming
→ Borrowed By: Ramesh

Return Due Date:
Within 15 Days of Issue.
"""

    # Return Books

    elif "return" in question:

        return """
🔄 Book Return Policy

• Return period: 15 Days

• Fine:
₹5 per day after due date

• Books should be returned in good condition.

Contact librarian for renewal.
"""

    # Availability

    elif "available" in question or "availability" in question:

        return """
📚 Book Availability

Python Basics
→ 5 Copies Available

Clean Code
→ 3 Copies Available

Java Programming
→ 4 Copies Available

Data Structures
→ 6 Copies Available

Database Management Systems
→ 2 Copies Available
"""

    # Issue Books

    elif "issue" in question or "issued" in question:

        return """
📕 Book Issue Details

Issue Duration:
15 Days

Maximum Books Allowed:
3 Books Per Member

Required:
• Membership ID
• Available Book Copy

Issued Books:
Python Basics
Clean Code
Java Programming
"""

    else:

        return """
📚 Library Management Assistant

I can help you with:

• Books Information
• Authors Information
• Members Information
• Borrowed Books
• Available Books
• Book Return Policies
• Issued Books

Please ask a library-related question.
"""

# ---------------------------------------
# Routes
# ---------------------------------------

@app.route("/")
def home():

    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():

    data = request.json

    question = data["question"]

    if not is_library_related(question):

        return jsonify({
            "response":
            """
❌ I am currently designed to provide
responses only for Library Management
related queries.

Supported Topics:

• Books
• Authors
• Members
• Borrowed Books
• Returned Books
• Availability

Please ask a Library related question.
"""
        })

    answer = generate_response(question)

    return jsonify({
        "response": answer
    })


if __name__ == "__main__":

    app.run(
        debug=True
    )