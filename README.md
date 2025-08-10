
# Gemini LLM Q&A App

🚀 This is a Streamlit app that allows you to interact with Google's Gemini large language model (LLM) for Q&A tasks.

---

## Features

- Powered by Google Generative AI's `gemini-1.5-flash` model.
- Simple and clean UI built with Streamlit.
- User-friendly input field and response display.
- Shows model details and usage information.
- Uses environment variables to securely manage API keys.

---

## Getting Started

### Prerequisites

- Python 3.8 or above
- [Google Generative AI API key](https://aistudio.google.com/)
- [Streamlit](https://streamlit.io/)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/kbphys96/Project-1-Gemini-LLM-Q-A-App.git
   cd Project-1-Gemini-LLM-Q-A-App
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your Google API key:
   ```env
   GOOGLE_API_KEY=your_api_key_here
   ```

### Running the App

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`.

---

## Usage

- Enter your question in the input box.
- Click **"Ask the Question"**.
- The app queries the Gemini LLM and displays the response.

---

## Notes

- The app uses the `gemini-1.5-flash` model, which is optimized for fast responses.
- Make sure your API key has sufficient quota; free tier limits apply.
- Keep your `.env` file secret and do **not** commit it to GitHub.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgments

- [Google Generative AI](https://ai.google.com/)
- [Streamlit](https://streamlit.io/)
