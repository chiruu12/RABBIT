
Conversation opened. 1 read message.

Skip to content
Using BITS Pilani University Mail with screen readers

1 of 10,375
FINALITO
Inbox

Swayam Agrawal
1:11 AM (3 minutes ago)
to me

import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
api_host = os.environ.get("PATHWAY_REST_CONNECTOR_HOST", "127.0.0.1")
api_port = int(os.environ.get("PATHWAY_REST_CONNECTOR_PORT", 8080))

# Set page config with a relevant background image
st.set_page_config(page_title='🐰 RABBIT - Resourceful Academic Book-Based Interactive Tutor', layout='centered', initial_sidebar_state='auto')

# Custom CSS for background image and styling
st.markdown(
    """
    <style>
    body {
        background-image: url('https://scsmh.education.uiowa.edu/wp-content/themes/uiowa-school-mental-health-theme/assets/images/background-maze-dark.png');
        background-size: 360px 270px;
        background-position: center;
        font-family: 'Arial', sans-serif;
    }
    .stApp {
        padding: 15px;
        border-radius: 5px;
        background-image: url('https://scsmh.education.uiowa.edu/wp-content/themes/uiowa-school-mental-health-theme/assets/images/background-maze-dark.png');
        background-size: 360px 270px;
        background-position: center;
    }
    .stButton>button {
        background-color: #007BFF;
        color: white;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #0056b3;
    }
    .stTextInput>div>div>input {
        border-radius: 5px;
        border: 1px solid #ccc;
        padding: 10px;
        font-size: 18px;
    }
    .stTextInput>div {
        display: flex;
        justify-content: center;
        margin-top: 80px; /* Adjust the value to move the input box downwards */
    }
    .stSidebar > div {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 15px;
        border-radius: 5px;
    }
    .sidebar-emoji {
        text-align: center;
    }
    .sidebar-emoji img {
        width: 2in;
        height: 2in;
    }
    .chat-message {
        font-size: 18px;
        font-weight: bold;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App title and description
st.title('🐰 Resourceful Academic Book-Based Interactive Tutor')
st.write("Welcome to RABBIT, your personal academic assistant. Ask any questions you have about your studies and get detailed explanations and answers.")


# Sidebar instructions
st.sidebar.markdown('<div class="sidebar-emoji"><img src="https://emojipedia-us.s3.amazonaws.com/source/skype/289/rabbit_1f407.png" alt="Rabbit Emoji"></div>', unsafe_allow_html=True)
st.sidebar.title('🐰 RABBIT')

st.sidebar.header("Instructions")
st.sidebar.write("""
1. Enter your question or doubt in the text input box below.
2. Click 'Enter'
3. The RABBIT will provide a detailed answer based on your query.
""")

input_text = st.text_input("Please feel free to ask any doubts! 📝")
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(f'<div class="message">{message["content"]}</div>', unsafe_allow_html=True)

if input_text:
    with st.chat_message("user"):
        st.markdown(f'<div class="message">{input_text}</div>', unsafe_allow_html=True)

    st.session_state.messages.append({"role": "user", "content": input_text})

    for message in st.session_state.messages:
        if message["role"] == "user":
            st.sidebar.text(f"📩 {message['content']}")

    url = f"http://{api_host}:{api_port}/"
    data = {"query": input_text, "user": "user"}

    response = requests.post(url, json=data)

    if response.status_code == 200:
        response = response.json()
        with st.chat_message("assistant"):
            st.markdown(f'<div class="message">{response}</div>', unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": response})
    else:
        st.error(f"Failed to send data. Status code: {response.status_code}")

Success!Thanks a lot.Thanks, I'll check it out.
