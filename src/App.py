import streamlit as st
from services import fetch_recommended_events, user_to_vectordb_prompt
from ui import create_event_card

def main():
    initalise_page_config()
    initialise_session_state()

    search, history = st.columns([3, 2])
    with search:
        st.markdown(
            "#### What you wanna do today sia????."
        )
        recommendation_engine()
    with history:
        display_history()


def initalise_page_config():
    st.set_page_config(
        layout="wide", initial_sidebar_state="collapsed", page_title="Kai Recommends"
    )


def initialise_session_state():
    if "query_history" not in st.session_state:
        st.session_state["query_history"] = []


def recommendation_engine():
    # Create input field
    prompt = st.text_input(
        "Try using the prompt below! \n\n I wanna plan a date with someone called kai."
    )

    # Add a submit button
    if st.button("Get Kai Recommendations"):
        if prompt:
            with st.spinner("Finding recommendations..."):
                improved_prompt = user_to_vectordb_prompt(prompt)
                response = fetch_recommended_events(improved_prompt)

                # Create cards for each recommendation
                for session in response:
                    with st.container():
                        st.markdown(
                            f"""
                            <div style="
                                padding: 20px;
                                border-radius: 10px;
                                margin: 10px 0px;
                                background-color: #f0f2f6;
                                border-left: 5px solid #ff4b4b;
                                box-shadow: 0 1px 2px rgba(0,0,0,0.1);">
                                <h3 style="margin: 0; color: #333;">{session}</h3>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )
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
                f"""
               <div style="
                   padding: 12px 0;
                   border-bottom: 1px solid #eee;">
                   <p style="margin: 0 0 8px 0; color: #666;">
                       {idx}. {prompt}
                   </p>
                   <div style="display: flex; flex-wrap: wrap; gap: 6px;">
                       {' '.join([
                           f'<span style="background: #f0f0f0; padding: 2px 8px; border-radius: 12px; font-size: 14px; font-weight: bold; color: #666;">{chip}</span>'
                           for chip in response
                       ])}
                   </div>
               </div>
               """,
                unsafe_allow_html=True,
            )
    else:
        st.info("No previous searches yet.")

def display_events(events_data):
    for event in events_data['events']:
        st.markdown(create_event_card(event), unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
