from typing import List
import streamlit as st
from qdrant_client import QdrantClient, models
from uuid import UUID

from .OpenAIService import OpenAIService
from utils import setup_logger
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
        self.openai = OpenAIService()
        self.logger = setup_logger(__name__, "qdrant")

    #####################################
    ###############CREATE################
    #####################################
    def create_collection(
        self, size: int = 1536, distance: models.Distance = models.Distance.COSINE
    ):  # Creates qdrant vector database instance
        self.client.create_collection(
            collection_name=self.collection_name,
            vectors_config=models.VectorParams(size=size, distance=distance),
        )

    def create_vector(
        self, activity: Activity
    ) -> bool:  # fails if point already exists
        event_embedding = self.openai.text_to_embedding(activity)
        try:
            self.client.insert(
                collection_name=self.collection_name,
                payload=activity,
                vector=event_embedding,
            )
            self.logger.info(f"Successfully uploaded activity: {activity.id}")
            return True
        except Exception as e:
            self.logger.error(
                f"Failed to upload activity {activity.id}: {str(e)}", exc_info=True
            )
            st.error(f"Failed to upload event: {e}")
            return False

    #####################################
    ################READ#################
    #####################################
    def search_vector(
        self, query: str, limit: int = 5
    ) -> List[Activity]:  # Search for events
        self.logger.info(
            f"Fetching recommended events for query: {query[:50]}... with limit: {limit}"
        )
        try:
            query_embedding = self.openai.text_to_embedding(query)
            similar_entities = self.client.search(
                collection_name=self.collection_name,
                query_vector=query_embedding,
                limit=limit,
            )
            self.logger.info(
                f"Successfully fetched {len(similar_entities)} recommended events"
            )
            return [Activity(entity.payload) for entity in similar_entities]
        except Exception as e:
            self.logger.error(
                f"Error fetching recommended events: {str(e)}", exc_info=True
            )
            raise

    def fetch_all_vectors(self) -> List[Activity]:  # Fetch all events
        try:
            points = self.client.scroll(collection_name=self.collection_name, limit=100)
            self.logger.info(f"Successfully fetched {len(points[0])} events")
            return [Activity(point.payload) for point in points[0]]
        except Exception as e:
            self.logger.error(f"Error fetching all events: {str(e)}", exc_info=True)
            raise

    #####################################
    ###############UPDATE################
    #####################################

    def update_vector(self, point_id: int, updates: dict):
        # Direct update using point ID
        self.client.set_payload(
            collection_name=self.collection_name,
            payload=updates,
            points=[point_id.int],
            wait=True,
        )

    def upsert_vector(
        self, activity_data: dict
    ):  # updates if point already exists, creates if not
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
    ###############DELETE################
    #####################################
    def delete_point(self, id: int):
        self.logger.info(f"Attempting to delete point with ID: {id}")
        try:
            self.client.delete_vectors(
                self.collection_name,
            )
            self.logger.info(f"Successfully deleted point: {id}")
        except Exception as e:
            self.logger.error(f"Error deleting point {id}: {str(e)}", exc_info=True)
            raise
