import streamlit as st
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain.schema import SystemMessage, HumanMessage

# --- Load environment variables ---
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# --- Set up LLM ---
llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model="llama3-8b-8192",
    temperature=1
)

# --- System prompt ---
SYSTEM_PROMPT = SystemMessage(
    content="""
You are Code-ine, an expert AI coding assistant created by Sukhdeep. 
Your role is to help users understand programming concepts, debug code, write clean and efficient code snippets, and explain code in a beginner-friendly yet technically accurate way.

Instructions:
- Use clear and concise language.
- Prefer Python as the default language unless specified otherwise.
- Always explain your answers with comments or step-by-step breakdowns when needed.
- Encourage best practices and write production-quality code.
- If a question is ambiguous, ask clarifying questions.
- Keep your tone helpful, friendly, and professional.

Only provide answers related to programming, software development, computer science theory, tools, or libraries.
If asked about anything else, politely redirect the user to stay on topic.
"""
)


# --- Streamlit setup ---
st.set_page_config(page_title="Code-ine - AI Coding Assistant", page_icon="🧠", layout="centered")

# --- Custom CSS for better UI ---
st.markdown("""
    <style>
        body {
            background-color: #f9f9f9;
            font-family: 'Segoe UI', sans-serif;
        }
        .stTextArea textarea {
            font-family: 'Fira Code', monospace;
            font-size: 16px;
            border-radius: 10px;
            background-color: #f3f3f3;
            padding: 10px;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
        }
        .stButton button:hover {
            background-color: #45a049;
        }
        .message-block {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }
        .user-msg {
            color: #333;
            font-weight: 600;
        }
        .bot-msg {
            color: #0b6e4f;
            font-weight: 600;
        }
    </style>
""", unsafe_allow_html=True)

# --- Title and Description ---
st.title("🧠 Code-ine: Your AI Coding Assistant")
st.markdown("""
<div style='margin-bottom: 30px; font-size: 18px;'>
Welcome to <strong>Code-ine</strong>, your AI-powered code assistant built on <code>Code Llama via Groq API</code>.  
Ask questions, get code, and learn effectively.
</div>
""", unsafe_allow_html=True)

# --- Init conversation memory ---
if "messages" not in st.session_state:
    st.session_state.messages = [SYSTEM_PROMPT]

# --- User Input Section ---
st.markdown("#### 💬 Ask a Coding Question")
prompt = st.text_area("", placeholder="e.g., Explain recursion with an example...", height=150)

# --- Generate and display response ---
if st.button("🚀 Generate Response"):
    if prompt.strip():
        user_msg = HumanMessage(content=prompt)
        st.session_state.messages.append(user_msg)

        with st.spinner("🧠 Code-ine is thinking..."):
            try:
                response = llm(st.session_state.messages)
                ai_reply = response.content
                st.session_state.messages.append(response)

                st.markdown("### 🤖 Code-ine's Response")
                st.code(ai_reply, language="python")
            except Exception as e:
                st.error(f"❌ Error: {e}")
    else:
        st.warning("Please enter a prompt before submitting.")

# --- Chat History Section ---
with st.expander("🕓 Chat History", expanded=False):
    for msg in st.session_state.messages[1:]:
        role = "🧑‍💻 You" if isinstance(msg, HumanMessage) else "🤖 Code-ine"
        css_class = "user-msg" if role == "🧑‍💻 You" else "bot-msg"
        st.markdown(f"""
        <div class='message-block'>
            <span class='{css_class}'><strong>{role}:</strong></span><br>
            <span>{msg.content}</span>
        </div>
        """, unsafe_allow_html=True)
