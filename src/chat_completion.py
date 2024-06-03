import json

import requests
import streamlit as st

nvidia_api_key = st.secrets["NVIDIA_API_KEY"]

def complete_chat(user_input, context, history):
    '''
    user_input : string
    context : string
    history : List

    Returns
    string
    '''
    combined_history = "\n".join(
        [f"{msg['role']}: {msg['content']}" for msg in history]
    )
    prompt_injected = f"""
        Here is some information about Suryakiran:\n{context}\n
        Based on this information and our previous conversation, answer the following question concisely and to the point:\n
        {combined_history}\n
        User: {user_input}\nAssistant:
    """

    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {nvidia_api_key}",
    }
    data = {
        "model": "meta/llama3-8b-instruct",
        "messages": [{"role": "user", "content": prompt_injected}],
        "temperature": 1,
        "top_p": 1,
        "max_tokens": 1024,
        "stream": False,
    }
    data = json.dumps(data)
    completion = requests.post(
        url = "https://integrate.api.nvidia.com/v1/chat/completions",
        headers = header,
        data = data,
        timeout=40
    )
    return completion.json()["choices"][0]["message"]["content"]
