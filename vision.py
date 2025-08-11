from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import io




# Load environment variables
load_dotenv()

# Configure Google API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro Model and get responses
model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(prompt,image):

    # Convert PIL image to bytes
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format="JPEG")
    img_bytes = img_byte_arr.getvalue()

    if prompt != "":
     response = model.generate_content([prompt,image])
    else:
      response = model.generate_content(image) 
    
    return response.text

# Streamlit app setup
st.set_page_config(page_title="Image Search", layout="wide")
st.header("Gemini Image Search App")

# User input
user_input = st.text_input("Enter your question:", key="image")

# App title
st.title("🚀 Image Search App")
st.write("Welcome! This is my  Streamlit app for testing Google Generative AI.")

# File uploader
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png", "webp"])

if uploaded_file is not None:
    # Open the image
    image = Image.open(uploaded_file)
     

    #Submlt Button
    submit=st.button("Tell me about the Image")

    #If Submit is Clicked
    if submit:
        response = get_gemini_response(user_input,image)
        st.subheader("The Response is :")
        st.write(response)

    # Display the image
    st.image(image, caption="Uploaded Image", width=300)

    