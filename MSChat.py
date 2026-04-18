import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(page_title="AI Chatbot", layout="wide")

st.title("🤖 AI Chatbot")

# HuggingFace client
client = InferenceClient(
    model="mistralai/Mistral-Nemo-Instruct-2407",
    token="YOUR_HF_TOKEN"   # replace this with your HuggingFace token
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**🧑 You:** {msg['content']}")
    else:
        st.markdown(f"**🤖 Bot:** {msg['content']}")

# Input box
user_input = st.chat_input("Type your message...")

if user_input:
    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    st.markdown(f"**🧑 You:** {user_input}")

    # Call HuggingFace Chat API
    with st.spinner("Thinking... 🤔"):
        try:
            response = client.chat_completion(
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful assistant."
                    },
                    *st.session_state.messages
                ],
                max_tokens=150
            )

            bot_reply = response.choices[0].message["content"]

        except Exception as e:
            bot_reply = f"Error: {str(e)}"

    # Save bot response
    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_reply
    })

    st.markdown(f"**🤖 Bot:** {bot_reply}")
