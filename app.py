from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Model and get responses
MODEL_NAME = "gemini-1.5-flash"
model = genai.GenerativeModel(MODEL_NAME)

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Streamlit page config
st.set_page_config(page_title="Gemini Q&A", page_icon="💡", layout="centered")

# Header section
st.markdown(
    f"""
    <div style="text-align: center;">
        <h1>Gemini LLM Q&A App</h1>
        <p style="font-size:18px;">Ask anything, powered by <b>{MODEL_NAME}</b> — Google's lightning-fast large language model!</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Model info card
with st.expander("ℹ About This Model"):
    st.markdown(
        f"""
        **Model Name:** `{MODEL_NAME}`  
        **Provider:** Google DeepMind  
        **Description:** Gemini 1.5 Flash is optimized for **fast, interactive responses** with low latency.  
        Ideal for Q&A, brainstorming, and real-time chat apps.  
        **Free Tier Limits:** ~15 requests/minute, ~1500/day (may vary).  
        **Learn more:** [Gemini API Docs](https://ai.google.dev/)
        """
    )

# Input section
st.subheader("💬 Ask Your Question")
user_input = st.text_input("Type your question below:", key="input", placeholder="e.g., Explain quantum computing in simple terms")

# Button & Response
if st.button("✨ Get Answer"):
    if user_input.strip():
        with st.spinner("Thinking... 🤖"):
            response = get_gemini_response(user_input)
        st.success("Here’s your answer:")
        st.write(response)
    else:
        st.warning("⚠ Please enter a question before submitting.")

# Footer
st.markdown(
    """
    ---
    <div style="text-align: center; font-size: 14px;">
        Built with ❤️ using Streamlit & Google Gemini API
    </div>
    """,
    unsafe_allow_html=True
)


'''
from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro Model and get responses
model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Streamlit app setup
st.set_page_config(page_title="Q&A", layout="wide")
st.header("Gemini LLM App")

# User input
user_input = st.text_input("Enter your question:", key="input")

# App title
st.title("🚀 Gemini LLM App")
st.write("Welcome! This is my first Streamlit app for testing Google Generative AI.")

# Submit button
if st.button("Ask the Question"):
    if user_input.strip() != "":
        response = get_gemini_response(user_input)
        st.write(response)
    else:
        st.warning("Please enter a question before submitting.")  

        
'''        