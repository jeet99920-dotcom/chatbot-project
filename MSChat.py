import streamlit as st

st.set_page_config(page_title="Chatbot", layout="wide")

st.title("🤖 My Chatbot")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**🧑 You:** {msg['content']}")
    else:
        st.markdown(f"**🤖 Bot:** {msg['content']}")

# Chat input (better than text_input)
user_input = st.chat_input("Type your message...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display user message immediately
    st.markdown(f"**🧑 You:** {user_input}")

    # Generate bot reply
    bot_reply = f"You said: {user_input}"

    # Add bot message
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    # Display bot reply
    st.markdown(f"**🤖 Bot:** {bot_reply}")
