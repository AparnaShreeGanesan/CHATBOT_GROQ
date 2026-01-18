LangChain Chatbot with Chain of Verification

A chatbot that verifies its own answers before replying.

AI models can hallucinate facts or sound confident when they’re wrong.
This project fixes that by adding a self-verification step before every response.

✨ Features

🛡 Reduced hallucinations

🎯 Bias detection & correction

📊 Confidence scoring (High / Medium / Low)

🔄 Automatic answer refinement

👁 Transparent verification process

🧠 How It Works

User asks a question

AI generates an initial answer

AI reviews the response for accuracy & bias

Answer is refined if needed

Verified response is returned

⏱️ Average response time: 5–10 seconds

🛠 Tech Stack

LangChain

Groq API

Streamlit

Python 3.8+

🚀 Quick Start
git clone <your-repo-url>
cd Chatbot-Using-Langchain-main
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt


Create a .env file:

GROQ_API_KEY=your_api_key_here


Run the app:

streamlit run app.py


Open http://localhost:8501

📊 Confidence Levels

🟢 High – Verified and reliable

🟡 Medium – Mostly correct, some nuance

🔴 Low – Uncertain, auto-refined

📁 Project Structure
app.py
requirements.txt
.env
VERIFICATION_SYSTEM.md
TESTING_GUIDE.md
