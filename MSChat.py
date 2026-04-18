import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(page_title="AI Chatbot", layout="wide")

st.title("🤖 AI Chatbot")

# Initialize client (free)
client = InferenceClient()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**🧑 You:** {msg['content']}")
    else:
        st.markdown(f"**🤖 Bot:** {msg['content']}")

# Input
user_input = st.chat_input("Type your message...")

if user_input:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    st.markdown(f"**🧑 You:** {user_input}")

    # Build conversation context
    context = "You are a helpful assistant.\n"
    for msg in st.session_state.messages:
        context += f"{msg['role']}: {msg['content']}\n"

    # Get AI response
    with st.spinner("Thinking... 🤔"):
        try:
            response = client.text_generation(
                context,
                max_new_tokens=150
            )
            bot_reply = response
        except Exception as e:
            bot_reply = f"Error: {str(e)}"

    # Save bot reply
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    st.markdown(f"**🤖 Bot:** {bot_reply}")
