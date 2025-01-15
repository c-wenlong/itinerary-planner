from openai import OpenAI
import streamlit as st
import logging

from .prompts import RECOMMENDER_SYSTEM, STRUTURED_OUTPUT_SYSTEM
from entities import Activity_Inferred_Fields

OPENAI_API_KEY = st.secrets["OPENAI"]["OPENAI_API_KEY"]
openai_client = OpenAI(api_key=OPENAI_API_KEY)


def user_to_vectordb_prompt(user_prompt) -> str:
    completion = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": RECOMMENDER_SYSTEM},
            {"role": "user", "content": user_prompt},
        ],
    )
    return completion.choices[0].message.content


def text_to_embedding(text):
    embeddings = openai_client.embeddings.create(
        model="text-embedding-3-small", input=text, encoding_format="float"
    )
    return embeddings.data[0].embedding


def text_to_structured_output(activity_prompt):
    try:
        structured_output = (
            openai_client.beta.chat.completions.parse(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": STRUTURED_OUTPUT_SYSTEM},
                    {
                        "role": "user",
                        "content": activity_prompt,
                    },
                ],
                response_format=Activity_Inferred_Fields,
            )
            .choices[0]
            .message
        )
        if structured_output.parsed:
            return structured_output.parsed
        elif structured_output.refusal:
            raise ValueError(f"OpenAI refused to process: {structured_output.refusal}")
    except Exception as e:
        # Log the error for debugging
        logging.error(f"Error processing structured output: {str(e)}")
        logging.error(f"Input prompt: {activity_prompt}")


if __name__ == "__main__":
    # test text_to_structured_output
    activity_prompt = "Name: Hiking\nCategory: Outdoor\nDuration: 2.5\nDescription: Hiking is a great way to explore the outdoors and get some exercise."
    structured_output = text_to_structured_output(activity_prompt)
    print(structured_output)
