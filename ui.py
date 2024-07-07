import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
api_host = os.environ.get("HOST", "127.0.0.1")
api_port = int(os.environ.get("PORT", 8080))

# Set page config with a relevant background image
st.set_page_config(page_title='🐰 RABBIT - Resourceful Academic Book-Based Interactive Tutor', layout='centered', initial_sidebar_state='auto')

# Custom CSS for background image and styling
st.markdown(
    """
    <style>
    body {
        background-image: url('https://img.freepik.com/premium-photo/library-building-room-containing-collections-ai-generated_866663-6300.jpg');
        background-size: cover;
        background-position: center;
        font-family: 'Arial', sans-serif;
    }
    .stApp {
        background-image: url('https://img.freepik.com/premium-photo/library-building-room-containing-collections-ai-generated_866663-6300.jpg');
        padding: 15px;
        border-radius: 5px;
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
    }
    .stSidebar > div {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 15px;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App title and description
st.sidebar.title('RABBIT 📚')
st.sidebar.write("Resourceful Academic Book-Based Interactive Tutor")