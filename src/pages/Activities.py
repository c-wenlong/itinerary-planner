import streamlit as st

from services import QdrantService
from components import Table
from entities import Activity
from utils import load_sample_activities

st.set_page_config(
    page_title="Singapore Event Assistant",
    page_icon=":cityscape:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

if "activities" not in st.session_state:
    st.session_state.activities = load_sample_activities()

table = Table(st.session_state.activities)
table.render_table()
