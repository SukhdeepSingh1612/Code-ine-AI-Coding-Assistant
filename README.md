# 🧠 Code-ine: Your AI Coding Assistant

Code-ine is a powerful AI-powered coding assistant built using Streamlit and the Groq API (powered by LLaMA3). It allows users to ask coding-related questions, get real-time answers with clean code snippets, and view chat history in a sleek, modern UI.

## 🚀 Features
- Built with **Streamlit** for a clean and interactive frontend.
- Uses **LLaMA3 via Groq API** for high-quality code responses.
- Supports **conversation history** using Streamlit session state.
- **Custom UI enhancements** using CSS for a better user experience.
- Handles errors gracefully and guides users effectively.

## 🧠 System Prompt Behavior
Code-ine is designed to:
- Help users understand programming concepts.
- Debug and write clean, production-level code.
- Explain code clearly using beginner-friendly language.
- Follow best practices and OOP principles.
- Stay strictly focused on coding topics.

## 🛠️ Technologies Used
- Python
- Streamlit
- Langchain + Groq API
- dotenv

## 📦 Installation

1. Clone this repo:
```bash
git clone https://github.com/yourusername/code-ine.git
cd code-ine
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Add your `.env` file:
```bash
GROQ_API_KEY=your_api_key_here
```

4. Run the app:
```bash
streamlit run app.py
```

## ✨ Sample Prompt

```
Can you build a mini task scheduler in Python that can:
- Add tasks with a priority level (High, Medium, Low),
- Automatically sort tasks by priority and due date,
- Allow marking tasks as completed,
- Save and load tasks from a local JSON file, and
- Display upcoming tasks within the next 3 days in a human-readable format?
Use OOP and clean code practices with comments.
```

## 💡 Creator
Made with ❤️ by **Sukhdeep**

---
