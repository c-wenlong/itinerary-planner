from typing import List
import streamlit as st
from qdrant_client import QdrantClient, models
from uuid import UUID

from .OpenAIService import text_to_embedding
from entities import Activity

QDRANT_URL = st.secrets["QDRANT"]["QDRANT_URL"]
QDRANT_API_KEY = st.secrets["QDRANT"]["QDRANT_API_KEY"]
QDRANT_COLLECTION_NAME = st.secrets["QDRANT"]["COLLECTION_NAME"]


class QdrantService:
    def __init__(self, collection_name: str = QDRANT_COLLECTION_NAME):
        self.client = QdrantClient(
            url=QDRANT_URL,
            api_key=QDRANT_API_KEY,
        )
        self.collection_name = collection_name
        self.logger = logger()

    #####################################
    ###############CREATE################
    #####################################
    def upload_activity(self, activity: Activity) -> bool:
        event_embedding = text_to_embedding(activity)
        try:
            self.client.insert(
                collection_name=self.collection_name,
                payload=activity,
                vector=event_embedding,
            )
            return True
        except Exception as e:
            st.error(f"Failed to upload event: {e}")
            return False

    def upsert_activity(self, activity_data: dict):
        # Extract the UUID from the id field and convert to string
        point_id = UUID(activity_data["id"].split("'")[1])

        # Create the point
        point = models.PointStruct(
            id=point_id.int,  # Qdrant uses integers for IDs
            payload=activity_data,
            vector=[0.0] * 1,  # Placeholder vector if needed
        )

        # Upsert the point
        self.client.upsert(
            collection_name=self.collection_name,
            points=[point],
            wait=True,  # Ensure the operation is complete before returning
        )

        return point_id

    #####################################
    ################READ#################
    #####################################
    def fetch_recommended_events(self, query: str, limit: int = 5) -> List[Activity]:
        query_embedding = text_to_embedding(query)
        similar_entities = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_embedding,
            limit=limit,
        )
        return [entity.payload for entity in similar_entities]

    def fetch_all_events(self) -> List[Activity]:
        points = self.client.scroll(collection_name=self.collection_name, limit=100)
        return [point.payload for point in points[0]]

    #####################################
    ###############UPDATE################
    #####################################

    def update_activity(self, point_id: int, updates: dict):
        # Direct update using point ID
        self.client.set_payload(
            collection_name=self.collection_name,
            payload=updates,
            points=[point_id.int],
            wait=True,
        )

    #####################################
    ###############DELETE################
    #####################################
    def delete_point(self, id: int):
        self.client.delete_vectors(
            self.collection_name,
        )
