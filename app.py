import streamlit as st

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖"
)

st.title(" Rule-Based AI Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Type your message")

if st.button("Send"):

    msg = user_input.lower()

    if msg in ["hi", "hello", "hey"]:
        response = "Hello! How can I help you today?"

    elif "name" in msg:
        response = "I am DecodeLabs AI Chatbot."

    elif "course" in msg:
        response = "You are currently working on Artificial Intelligence projects."

    elif "python" in msg:
        response = "Python is one of the most popular programming languages."

    elif msg in ["bye", "exit", "quit"]:
        response = "Goodbye! Have a great day."

    else:
        response = "Sorry, I don't understand that."

    st.session_state.messages.append(
        ("You", user_input)
    )

    st.session_state.messages.append(
        ("Bot", response)
    )

for sender, message in st.session_state.messages:

    if sender == "You":
        st.write(f"🧑 {message}")
    else:
        st.write(f"🤖 {message}")
