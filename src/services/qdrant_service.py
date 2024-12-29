import streamlit as st
from qdrant_client import QdrantClient, models
from uuid import UUID

from .openai_service import text_to_embedding
from schemas import Activity

QDRANT_URL = st.secrets["QDRANT"]["QDRANT_URL"]
QDRANT_API_KEY = st.secrets["QDRANT"]["QDRANT_API_KEY"]
QDRANT_COLLECTION_NAME = st.secrets["QDRANT"]["COLLECTION_NAME"]

qdrant_client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
)


def fetch_recommended_events(query, collection_name=QDRANT_COLLECTION_NAME, limit=5):
    query_embedding = text_to_embedding(query)
    similar_entities = qdrant_client.search(
        collection_name=collection_name, query_vector=query_embedding, limit=limit
    )
    return [entity.payload for entity in similar_entities]


def fetch_all_events(collection_name=QDRANT_COLLECTION_NAME):
    points = qdrant_client.scroll(collection_name=collection_name, limit=100)
    return [point.payload for point in points[0]]


def upload_activity(activity: Activity, collection_name=QDRANT_COLLECTION_NAME):
    event_embedding = text_to_embedding(activity)
    try:
        qdrant_client.insert(
            collection_name=collection_name, payload=activity, vector=event_embedding
        )
        return True
    except Exception as e:
        st.error(f"Failed to upload event: {e}")
        return False


def upsert_activity(activity_data: dict, collection_name=QDRANT_COLLECTION_NAME):
    # Extract the UUID from the id field and convert to string
    point_id = UUID(activity_data["id"].split("'")[1])

    # Create the point
    point = models.PointStruct(
        id=point_id.int,  # Qdrant uses integers for IDs
        payload=activity_data,
        vector=[0.0] * 1,  # Placeholder vector if needed
    )

    # Upsert the point
    qdrant_client.upsert(
        collection_name=collection_name,
        points=[point],
        wait=True,  # Ensure the operation is complete before returning
    )

    return point_id


def update_activity(
    self, point_id: UUID, updates: dict, collection_name=QDRANT_COLLECTION_NAME
):
    # Direct update using point ID
    self.client.set_payload(
        collection_name=collection_name,
        payload=updates,
        points=[point_id.int],
        wait=True,
    )
