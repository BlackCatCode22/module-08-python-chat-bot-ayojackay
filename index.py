from ChatBot import generate_response
import streamlit as st

st.set_page_config(
    page_title="Home Page",
    page_icon="👋"
)
containerOne = st.container()

with containerOne:
    st.header("Chat Bot - Assignment")
    st.subheader("Python, 5.12.24", divider="rainbow", anchor=False)
    st.write("I learned about using API keys and frameworks. Personally, I've never heard of **Streamlit** before this assignment. I enjoyed working on this project overall and definitely will continue playing around with Streamlit and APIs.")
    st.write("Well, enjoy chatting!!")

messages = st.container(height=400)
prompt = st.chat_input("Python student question")
if "chat_logs" not in st.session_state:
    st.session_state["chat_logs"] = []
if prompt:
    response = generate_response(prompt)
    t = {
        "role": "user", "content": prompt
    }
    e = {
        "role": "assistant", "content": response.content
    }
    st.session_state["chat_logs"].append(t)
    st.session_state["chat_logs"].append(e)

for log in st.session_state["chat_logs"]:
    with messages.chat_message(name=log["role"]):

        st.write(log['content'])
        st.markdown('''
            <style>
                 [data-testid="stChatMessage"]:nth-child(even) {
                    padding-left: 2rem;
                }
            </style>
        ''', unsafe_allow_html=True)





