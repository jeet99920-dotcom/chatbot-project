import streamlit as st
from groq import Groq
st.write("Key loaded:", st.secrets["GROQ_API_KEY"][:10])
st.set_page_config(page_title="AI Chatbot", layout="wide")
st.title("🤖 Real AI Chatbot (Groq)")

# Put your API key here OR use secrets
client = Groq(api_key="YOUR_GROQ_API_KEY")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# Display chat history (skip system message)
for msg in st.session_state.messages:
    if msg["role"] != "system":
        if msg["role"] == "user":
            st.markdown(f"**🧑 You:** {msg['content']}")
        else:
            st.markdown(f"**🤖 Bot:** {msg['content']}")

# Input box
user_input = st.chat_input("Type your message...")

if user_input:
    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    st.markdown(f"**🧑 You:** {user_input}")

    with st.spinner("Thinking... 🤔"):
        try:
            response = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=st.session_state.messages,
                temperature=0.7,
                max_tokens=200
            )

            bot_reply = response.choices[0].message.content

        except Exception as e:
            bot_reply = f"Error: {str(e)}"

    # Save bot response
    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_reply
    })

    st.markdown(f"**🤖 Bot:** {bot_reply}")
