import streamlit as st
from google import genai
from dotenv import load_dotenv
from templates.prompts import SYSTEM_PROMPT
import os

# --------------------
# Load Environment
# --------------------
load_dotenv()

# --------------------
# Gemini Client
# --------------------
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# --------------------
# Page Config
# --------------------
st.set_page_config(
    page_title="Library Management Bot",
    page_icon="📚",
    layout="wide"
)

# --------------------
# Load CSS
# --------------------
with open("static/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# --------------------
# Title
# --------------------
st.markdown(
    """
    <div class='main-title'>
        📚 Library Management ChatBot
    </div>
    """,
    unsafe_allow_html=True
)

# --------------------
# Sidebar
# --------------------
with st.sidebar:

    st.header("Library Assistant")

    st.write("""
    Ask questions related to:
    - Books
    - Authors
    - Categories
    - Members
    - Borrowed Books
    """)

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# --------------------
# Session History
# --------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------
# Display History
# --------------------
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --------------------
# User Input
# --------------------
question = st.chat_input(
    "Ask a Library Question..."
)

if question:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":question
        }
    )

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):

        with st.spinner(
            "Generating Response..."
        ):

            try:

                final_prompt = f"""
                {SYSTEM_PROMPT}

                User Question:
                {question}
                """

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=final_prompt
                )

                answer = response.text

                st.write(answer)

                st.session_state.messages.append(
                    {
                        "role":"assistant",
                        "content":answer
                    }
                )

            except Exception as e:

                error_msg = f"Error: {str(e)}"

                st.error(error_msg)

                st.session_state.messages.append(
                    {
                        "role":"assistant",
                        "content":error_msg
                    }
                )

# --------------------
# Footer
# --------------------
st.markdown(
"""
<div class='footer'>
Library Management System | Streamlit + Gemini
</div>
""",
unsafe_allow_html=True
)