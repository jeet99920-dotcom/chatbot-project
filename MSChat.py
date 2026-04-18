import streamlit as st

st.set_page_config(page_title="Test App")

st.title("✅ Chatbot is Working")

user_input = st.text_input("Enter something:")

if user_input:
    st.write("You said:", user_input)
