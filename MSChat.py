import streamlit as st

st.set_page_config(page_title="AI Chatbot", layout="wide")
st.title("🤖 Simple Working Chatbot")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**🧑 You:** {msg['content']}")
    else:
        st.markdown(f"**🤖 Bot:** {msg['content']}")

# Input
user_input = st.chat_input("Type your message...")

# Simple response engine
def get_response(text):
    text = text.lower()

    if "hello" in text or "hi" in text:
        return "Hello! 👋 How can I help you today?"

    elif "name" in text:
        return "I am your simple AI chatbot 🤖"

    elif "time" in text:
        return "I cannot fetch real-time data yet ⏰"

    elif "python" in text:
        return "Python is a programming language used for AI, web, automation 🚀"

    elif "help" in text:
        return "I can answer basic questions. Try asking something simple 🙂"

    else:
        return "I'm still learning 🤖 — but I understood your message!"

if user_input:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.markdown(f"**🧑 You:** {user_input}")

    # Bot response
    bot_reply = get_response(user_input)

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    st.markdown(f"**🤖 Bot:** {bot_reply}")
