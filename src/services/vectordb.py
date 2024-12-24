import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from qdrant_client import QdrantClient

QDRANT_URL = st.secrets["QDRANT"]["QDRANT_URL"]
QDRANT_API_KEY = st.secrets["QDRANT"]["QDRANT_API_KEY"]
QDRANT_COLLECTION_NAME = st.secrets["QDRANT"]["COLLECTION_NAME"]

qdrant_client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
)

from openai import OpenAI

OPENAI_API_KEY = st.secrets["OPENAI"]["OPENAI_API_KEY"]
openai_client = OpenAI(api_key=OPENAI_API_KEY)


def text_to_embedding(text):
    embeddings = openai_client.embeddings.create(
        model="text-embedding-3-small", input=text, encoding_format="float"
    )
    return embeddings.data[0].embedding


def fetch_recommended_events(
    artist_profile, collection_name=QDRANT_COLLECTION_NAME, limit=5
):
    artist_embedding = text_to_embedding(artist_profile)
    similar_events = qdrant_client.search(
        collection_name=collection_name, query_vector=artist_embedding, limit=limit
    )
    return [event.payload for event in similar_events]



