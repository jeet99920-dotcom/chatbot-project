import streamlit as st

st.set_page_config(page_title="Chatbot", layout="wide")

st.title("🤖 My Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    st.write(f"{msg['role']}: {msg['content']}")

# User input
user_input = st.text_input("Type your message")

if user_input:
    # Save user message
    st.session_state.messages.append({"role": "User", "content": user_input})

    # Simple bot reply
    bot_reply = "This is a test reply"

    st.session_state.messages.append({"role": "Bot", "content": bot_reply})

    st.rerun()
