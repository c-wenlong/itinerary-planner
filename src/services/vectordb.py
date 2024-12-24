import streamlit as st
from dotenv import load_dotenv
from qdrant_client import QdrantClient

load_dotenv()

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


def fetch_recommended_events(query, collection_name=QDRANT_COLLECTION_NAME, limit=5):
    query_embedding = text_to_embedding(query)
    similar_entities = qdrant_client.search(
        collection_name=collection_name, query_vector=query_embedding, limit=limit
    )
    return [entity.payload for entity in similar_entities]


def fetch_all_events(collection_name=QDRANT_COLLECTION_NAME):
    points = qdrant_client.scroll(
        collection_name=collection_name, limit=100
    )
    return [point.payload for point in points[0]]
