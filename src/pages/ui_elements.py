import streamlit as st
from ui import create_event_card, create_history_card, test_elements

# Sidebar navigation
st.sidebar.title("UI Elements")
demo_section = st.sidebar.radio(
    "Navigate to",
    [
         "UI Overview",
        "Conversation History",
        "Event Card",
    ],
)

if demo_section == "UI Overview":
    st.header("UI Overview")
    st.write(
        """
    This is the testing environment for all UI components.
    """
    )

elif demo_section == "Conversation History":
    st.header("Conversation History")
    history = [
        {
            "prompt": "I wanna plan a date with someone called kai.",
            "response": ["Event 1", "Event 2", "Event 3", "Event 4", "Event 5"],
        },
        {
            "prompt": "I wanna plan a date with someone called kai.",
            "response": ["Event 1", "Event 2", "Event 3", "Event 4", "Event 5"],
        },
        {
            "prompt": "I wanna plan a date with someone called kai.",
            "response": ["Event 1", "Event 2", "Event 3", "Event 4", "Event 5"],
        },
    ]
    for idx, entry in enumerate(history, 1):
        st.markdown(
            create_history_card(idx, entry["prompt"], entry["response"]),
            unsafe_allow_html=True,
        )

elif demo_section == "Event Card":
    st.header("Event Card")
    event = {
        "name": "Monster Curry",
        "price_range": "$$",
        "description": "Grab a hearty meal at Monster Curry in the afternoon with Kai.",
        "location": "Tampines Mall, Level 1-32",
        "area": "Tampines",
        "duration_hours": 2,
        "tags": ["Food", "Spicy", "Mall"],
        "intensity_level": "low",
        "suitable_for": ["Beginners", "Intermediates"],
    }
    st.markdown(create_event_card(event), unsafe_allow_html=True)
    test_elements()
  