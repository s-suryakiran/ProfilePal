from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone

# Load environment variables from .env file
load_dotenv()

nvidia_api_key = os.getenv("NVIDIA_API_KEY")
pinecone_api_key = os.getenv("PINECONE_API_KEY")
index_name = os.getenv("INDEX_NAME")

# Initialize Pinecone
pc = Pinecone(api_key=pinecone_api_key)
index = pc.Index(index_name)

# Initialize the embedding model
embed_model = SentenceTransformer('BAAI/bge-large-en-v1.5')

st.title("ProfilePal")

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=nvidia_api_key,
)

def get_context(query):
    res = embed_model.encode(query)
    ans = index.query(vector=res.tolist(), top_k=2, include_metadata=True)
    context = ""
    for match in ans['matches']:
        context += match['metadata']['text'] + " "
    return context


def chatter(user_input, context, history):
    combined_history = "\n".join([f"{msg['role']}: {msg['content']}" for msg in history])
    prompt = (
        f"Here is some information about Suryakiran:\n{context}\n"
        "Based on this information and our previous conversation, answer the following question concisely and to the point:\n"
        f"{combined_history}\n"
        f"User: {user_input}\nAssistant:"
    )
    completion = client.chat.completions.create(
        model="meta/llama3-8b-instruct",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        temperature=1,
        top_p=1,
        max_tokens=1024,
        stream=True,
    )

    return completion

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Ask anything about Surya.."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role":"user", "content": prompt})

    if prompt.lower() in ["hi", "hello", "hey"]:
        assistant_response = "Hello there! Feel free to ask me anything about Surya."
        with st.chat_message("assistant"):
            st.markdown(assistant_response)

    else:
        context = get_context(prompt)
        response_stream = chatter(prompt, context, st.session_state.messages)

        assistant_response = ""
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            for chunk in response_stream:
                if chunk.choices[0].delta.content is not None:
                    assistant_response += chunk.choices[0].delta.content
                    response_placeholder.markdown(assistant_response)

    
    st.session_state.messages.append({"role":"assistant", "content": assistant_response})