import streamlit as st
from pydantic import ValidationError

from schemas import Activity, Category_Enum, Duration_in_Hours_Field, Description_Field
from services import text_to_structured_output

"""
test_activity = Activity(
    name="Test Activity",
    category="Test Category",
    Physical_Intensity_Field="High",
    Cost_Range_Field="Low",
    Social_Interaction_Field="High",
    Location_Field="Test Location",
    Time_Of_Day_Field="Morning",
    Weather_Suitability_Field="Sunny",
    Skills_List_Field=["Test Skill 1", "Test Skill 2"],
    Tags_Field=["Test Tag 1", "Test Tag 2"],
)
"""


def show_activity_form():
    # We're adding activities via an `st.form` and some input widgets. If widgets are used
    # in a form, the app will only rerun once the submit button is pressed.
    with st.form("add_activity_form"):
        required, optional = st.columns(2)
        with required:
            # Required Fields
            name = st.text_input("Name of the activity")
            description = st.text_area("Describe the activity!", height=80)
            category = st.selectbox(
                "Category", [category.value for category in Category_Enum]
            )
            duration = st.number_input(
                "Duration in hours (will be rounded to nearest 0.5)",
                min_value=0.0,
                step=0.5,
            )

        with optional:
            # Optional Fields
            location = st.text_input("Location (optional)")
            skills_input = st.text_input(
                "Skills (optional) - Separate multiple skills with commas",
                placeholder="e.g., navigation, photography, teamwork",
            )
            tags_input = st.text_input(
                "Tags (optional) - Separate multiple tags with commas",
                placeholder="e.g., outdoor, nature, exercise",
            )

        submitted = st.form_submit_button("Submit")

    if submitted:
        # Validate required fields
        if not all([name, description, category, duration]):
            st.error("Please fill in all required fields marked with *")
            return

        # Process optional fields
        skills = (
            [skill.strip() for skill in skills_input.split(",")] if skills_input else []
        )
        tags = [tag.strip() for tag in tags_input.split(",")] if tags_input else []

        # Make a dataframe for the new ticket and append it to the dataframe in session
        # state.
        try:
            activity = Activity(
                name=name,
                category=category,
                duration=duration,
                description=description,
                location=location if location else None,
                skills=skills,
                tags=tags,
            )

            # Here you would typically save the activity
            st.success("Activity added successfully!")
            # Display both activity and inferred fields as formatted JSON
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Activity Data")
                st.json(activity.model_dump())

            with col2:
                st.subheader("Inferred Fields")
                inferred_fields = text_to_structured_output(activity.model_dump_json())
                st.json(inferred_fields)

        except ValidationError as e:
            st.error(f"Validation error: {str(e)}")

        # Activity.model_validate(activity).model_dump_json(indent=2)


if __name__ == "__main__":
    show_activity_form()
