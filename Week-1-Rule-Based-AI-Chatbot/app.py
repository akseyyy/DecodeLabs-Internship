import streamlit as st
from datetime import datetime, date

st.set_page_config(page_title="Rule-Based AI Chatbot", page_icon="🤖")

st.title("🤖 Rule-Based AI Chatbot")
st.write("Ask me a question!")

user = st.text_input("You:")

if st.button("Send"):

    message = user.lower().strip()
    user = user.lower()

    if message == "hello":
        st.success("Bot: Hello! How can I help you?")

    elif message == "hi":
        st.success("Bot: Hi! Nice to meet you.")

    elif message == "how are you":
        st.success("Bot: I am fine. Thanks for asking!")

    elif message == "what is your name":
        st.success("Bot: My name is AI Bot.")

    elif message == "what is ai":
        st.success("Bot: AI stands for Artificial Intelligence.")

    elif message == "who created you":
        st.success("Bot: I am created by Syeda Aksezehra Zaidi")

    elif message == "tell me a joke":
        st.success("Bot: Why do programmers prefer dark mode? Because light attracts bugs!")

    elif message == "what is the date":
        st.success(f"Bot: Today's date is {date.today()}")

    elif message == "what is the time":
        st.success(f"Bot: Current time is {datetime.now().strftime('%I:%M %p')}")

    elif message == "bye":
        st.success("Bot: Goodbye! Have a nice day.")

    else:
        st.error("Bot: Sorry, I don't understand.")

# after running, write the command given below in the terminal:

# streamlit run app.py (with whatever file name you have saved)      