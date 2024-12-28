import streamlit as st

from services import fetch_all_events
from components import show_activity_table, generate_sample_activities
from schemas import Activity

st.set_page_config(
    page_title="Singapore Event Assistant",
    page_icon=":cityscape:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

if "activities" not in st.session_state:
    st.session_state.activities = generate_sample_activities()

activities: list[Activity] = show_activity_table(st.session_state.activities)
