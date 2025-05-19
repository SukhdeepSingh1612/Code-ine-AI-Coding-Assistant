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
    content="""You are a code teaching assistant named Code-ine created by Sukhdeep. 
Answer all the code related questions being asked."""
)

# --- Streamlit setup ---
st.set_page_config(page_title="Code-ine - AI Coding Assistant", page_icon="🧠", layout="centered")
st.title("🧠 Code-ine: Your AI Coding Assistant")
st.markdown("""
Welcome to **Code-ine**, your AI-powered code assistant built on **Code Llama via Groq API**.  
Ask questions, request code, and learn effectively.
""")

# --- Init conversation memory ---
if "messages" not in st.session_state:
    st.session_state.messages = [SYSTEM_PROMPT]

# --- User input ---
prompt = st.text_area("💬 Your Coding Question", placeholder="e.g., Explain recursion with an example...", height=150)

# --- Generate and display response ---
if st.button("🚀 Generate Response"):
    if prompt.strip():
        user_msg = HumanMessage(content=prompt)
        st.session_state.messages.append(user_msg)

        with st.spinner("Thinking..."):
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


with st.expander("🕓 Chat History"):
    for msg in st.session_state.messages[1:]: 
        role = "🧑‍💻 You" if isinstance(msg, HumanMessage) else "🤖 Code-ine"
        st.markdown(f"**{role}:** {msg.content}")
