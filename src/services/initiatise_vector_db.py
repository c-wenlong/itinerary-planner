from qdrant_client import QdrantClient, models
import streamlit as st
from services.vectordb import text_to_embedding

import json
from pathlib import Path

QDRANT_URL = st.secrets["QDRANT"]["QDRANT_URL"]
QDRANT_API_KEY = st.secrets["QDRANT"]["QDRANT_API_KEY"]
QDRANT_COLLECTION_NAME = st.secrets["QDRANT"]["COLLECTION_NAME"]

qdrant_client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
)

# Creates qdrant vector database instance
qdrant_client.create_collection(
    collection_name="singapore_events",
    vectors_config=models.VectorParams(size=1536, distance=models.Distance.COSINE)
)

def read_json(file_path=Path("src/assets/datasets/singapore.json")):
    with open(file_path, "r") as file:
        sessions = json.load(file)
    return sessions

# Convert the session metadata into embeddings
event_embeddings = {}
events_data = read_json()

# Iterate through each event
for event in events_data['events']:
        # Convert event data to string for embedding
        event_text = f"""
        Name: {event['name']}
        Category: {event['category']}
        Subcategory: {event['subcategory']}
        Description: {event['description']}
        Location: {event['location']}
        Area: {event['area']}
        Price Range: {event['price_range']}
        Duration: {event['duration_hours']} hours
        Suitable For: {', '.join(event['suitable_for'])}
        Intensity Level: {event['intensity_level']}
        Tags: {', '.join(event['tags'])}
        """
        
        # Get embedding
        embedding = text_to_embedding(event_text)
        
        # Store result
        event_embeddings[event['id']] = {
            'metadata': event,
            'embedding': embedding
        }
    
# Upload vector embeddings into QDRANT DB
from datetime import datetime

for idx, (session_name, session_data) in  enumerate(event_embeddings.items()):
	qdrant_client.upsert(
		collection_name=QDRANT_COLLECTION_NAME,
		points=[
			models.PointStruct(
				id=idx,
				payload={
					"session_name":session_name,
					"metadata":session_data["metadata"],
					"created_at":datetime.now().isoformat()
				},
				vector=session_data["embedding"]
			)
		]
	)
