from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Function to load Gemini Pro Model
MODEL_NAME = "gemini-1.5-flash"
model=genai.GenerativeModel(MODEL_NAME)

chat=model.start_chat(history=[])

def get_gemini_response(question):
    response=chat.send_message(question,stream=True)
    return response
    
# Streamlit page config
st.set_page_config(page_title="Gemini Q&A", page_icon="💡", layout="centered")



# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    #st.session_state['chat_history'] = []

st.title("💬 Chatbot with History")

# User input box
user_input = st.text_input("You:", "")

# When user sends a message
if st.button("Send"):
    if user_input.strip():
        # Append user message
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        
        # Example AI response (replace with actual model call)
        bot_response = ""
        for chunk in get_gemini_response(user_input):
         bot_response += chunk.text

        st.session_state.chat_history.append({"role": "assistant", "content": bot_response})
        
# Display chat history
for message in st.session_state.chat_history:
    if message["role"] == "user":
        st.markdown(f"**You:** {message['content']}")
    else:
        st.markdown(f"**Bot:** {message['content']}")