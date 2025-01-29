import streamlit as st
from services import QdrantService, OpenAIService
from ui import create_event_card, create_history_card

st.set_page_config(
    page_title="Kai's Date Recommender",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def main():
    initialise_session_state()

    search, history = st.columns([3, 2])
    with search:
        st.markdown("#### What you wanna do today sia????.")
        recommendation_engine()
    with history:
        display_history()


def initialise_session_state():
    if "query_history" not in st.session_state:
        st.session_state["query_history"] = []


def recommendation_engine():
    qdrant = QdrantService()
    openai = OpenAIService()
    # Create input field
    prompt = st.text_input(
        "Try using the prompt below! \n\n I wanna plan a date with someone called kai."
    )

    # Add a submit button
    if st.button("Get Kai Recommendations"):
        if prompt:
            with st.spinner("Finding recommendations..."):
                # transform user input to a prompt that is better for the vector DB
                improved_prompt = openai.enhance_prompt(prompt)

                # fetch the recommendations from the vector DB
                events = qdrant.search_vector(improved_prompt)

                # Create cards for each recommendation
                for event in events:
                    event_card = create_event_card(event)
                    with st.container():
                        st.markdown(
                            event_card,
                            unsafe_allow_html=True,
                        )
            response = [event["name"] for event in events]
            st.session_state["query_history"].append(
                {"prompt": prompt, "response": response}
            )
        else:
            st.warning("Please enter your needs first.")


def display_history():
    # Display query history in a simple card
    if st.session_state.query_history:
        st.markdown("### Previous Searches")
        for idx, entry in enumerate(reversed(st.session_state.query_history), 1):
            prompt = entry["prompt"]
            response = entry["response"]
            st.markdown(
                create_history_card(idx, prompt, response),
                unsafe_allow_html=True,
            )
    else:
        st.info("No previous searches yet.")


def display_events(events_data):
    for event in events_data["events"]:
        st.markdown(create_event_card(event), unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
