import streamlit as st

from components import Form

# Show app title and description.
st.set_page_config(
    page_title="Create Activity",
    page_icon="🎲",
    initial_sidebar_state="collapsed",
    layout="wide",
)

st.title("🎲 Add a New Activity Here")
st.write(
    """
    Hey Baby Banana! 🍌🍌🍌 \n
    Add a new activity to the list below. \n
    """
)

form = Form()
form.render_form()
