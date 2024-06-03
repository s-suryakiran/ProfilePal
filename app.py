import streamlit as st

from src.chat_completion import complete_chat
from src.retrieval import get_context


st.title("ProfilePal")


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Ask anything about Surya.."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    if prompt.lower().strip() in ["hi", "hello", "hey"]:
        assistant_response = "Hello there! Feel free to ask me anything about Surya."
        with st.chat_message("assistant"):
            st.markdown(assistant_response)

    else:
        context = get_context(prompt)
        assistant_response = complete_chat(prompt, context, st.session_state.messages)
        with st.chat_message("assistant"):
            st.markdown(assistant_response)

    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_response}
    )
