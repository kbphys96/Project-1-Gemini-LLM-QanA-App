
# 🤖 Gemini LLM Apps – Q&A + Image Search

🚀 A collection of **Streamlit** apps powered by **Google’s Gemini Large Language Model** (`gemini-1.5-flash`) for both text-based Q&A and image-based search & analysis.

---

## 📌 Features

### 1️⃣ Gemini LLM Q&A App
- Ask any question in **natural language** and get instant AI-generated answers.
- Powered by **Google Generative AI's `gemini-1.5-flash`** model.
- Clean, simple **Streamlit** interface.

### 2️⃣ Gemini Image Search & Analysis App
- Upload an image and **ask questions about it**.
- Supports **JPG, JPEG, PNG, WEBP** formats.
- Stylish, modern UI with **custom fonts, colors, and hover effects**.

---

## 🛠️ Getting Started

### **Prerequisites**
- Python **3.8+**
- [Google Generative AI API key](https://aistudio.google.com/)
- [Streamlit](https://streamlit.io/)

---

### **Installation**
```bash
# 1️⃣ Clone the repository
git clone https://github.com/kbphys96/Project-1-Gemini-LLM-Apps.git
cd Project-1-Gemini-LLM-Apps

# 2️⃣ Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Create a .env file and add your API key
GOOGLE_API_KEY=your_api_key_here
▶ Running the Apps
Run the Q&A App
bash
Copy
Edit
streamlit run app.py
Run the Image Search App
bash
Copy
Edit
streamlit run vision.py
🎯 Usage
Q&A App
Enter your question in the input box.

Click "Ask the Question".

View the AI-generated answer instantly.

Image Search & Analysis App
Upload an image (jpg, jpeg, png, webp).

Optionally type a prompt/question about the image.

Click "Tell me about the Image".

See detailed AI analysis or related information.

📂 Project Structure
bash
Copy
Edit
.
├── app.py              # Q&A App
├── vision.py           # Image Search App
├── requirements.txt    # Python dependencies
├── .env.example        # Example environment file
├── README.md           # Documentation
⚠ Notes
Both apps use the gemini-1.5-flash model for fast responses.

Your Google API key must be valid and not expired.

Free-tier API usage limits apply.

Never commit your .env file to GitHub.

📜 License
This project is licensed under the MIT License.

🙌 Acknowledgments
Google Generative AI

Streamlit

