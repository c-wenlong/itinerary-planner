import streamlit as st
from pydantic import ValidationError
from datetime import datetime, timezone

from entities import Activity, Activity_Inferred_Fields, Category_Enum
from services import text_to_structured_output, upload_activity
from .google_maps_search import show_google_maps_search


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

            date = st.date_input("Date (optional)", value=None)

            url = st.text_input("URL (optional)")

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
                # REQUIRED
                name=name,
                category=category,
                duration=duration,
                description=description,
                # OPTIONAL
                location=location if location else None,
                date=(
                    datetime.combine(date, datetime.min.time()).replace(
                        tzinfo=timezone.utc
                    )
                    if date
                    else None
                ),
                url=url if url else None,
                skills=skills if skills else [],
                tags=tags if tags else [],
            )

            # Here you would typically save the activity
            st.success("Activity added successfully!")

            # REMOVE IN PROD
            visualise_output_json(activity=activity)
            # upload_activity(activity) ## uploads onto qdrant db

        except ValidationError as e:
            st.error(f"Validation error: {str(e)}")


def visualise_output_json(activity: Activity):
    # Display both activity and inferred fields as formatted JSON
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Activity Data")
        st.json(activity.model_dump())

    with col2:
        st.subheader("Inferred Fields")
        inferred_fields = text_to_structured_output(activity.model_dump_json())
        st.json(inferred_fields)

    st.subheader("Merged Activity")
    full_activity = merge_inferred_fields(activity, inferred_fields)
    st.json(full_activity.model_dump())


def merge_inferred_fields(
    activity: Activity, inferred_fields: Activity_Inferred_Fields
):
    physical = inferred_fields.physical_intensity
    cost = inferred_fields.cost_range
    social = inferred_fields.social_interaction
    weather = inferred_fields.weather_suitability
    time = inferred_fields.time_of_day
    indoor_or_outdoor = inferred_fields.indoor_or_outdoor

    activity.physical_intensity = physical
    activity.cost_range = cost
    activity.social_interaction = social
    activity.weather_suitability = weather
    activity.time_of_day = time
    activity.indoor_or_outdoor = indoor_or_outdoor

    return activity


if __name__ == "__main__":
    show_activity_form()
