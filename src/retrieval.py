import streamlit as st
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer

# streamlit secrets
pinecone_api_key = st.secrets["PINECONE_API_KEY"]
index_name = st.secrets["INDEX_NAME"]

# Initialize the embedding model
embed_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Initialize Pinecone
pc = Pinecone(api_key=pinecone_api_key)
index = pc.Index(index_name)


def get_context(query):
    """
    query : string

    Returns
    string
    """
    res = embed_model.encode(query)
    ans = index.query(vector=res.tolist(), top_k=2, include_metadata=True)
    context = ""
    for match in ans["matches"]:
        context += match["metadata"]["text"] + " "

    return context
