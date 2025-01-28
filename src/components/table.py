import streamlit as st

from entities import (
    Activity,
    Category_Enum,
    Cost_Range_Inferred_Enum,
    Physical_Intensity_Inferred_Enum,
    Social_Interaction_Inferred_Enum,
    Time_Of_Day_Enum,
    Weather_Suitability_Enum,
    Indoor_Or_Outdoor_Enum,
    Location_Class,
    Point,
)


def Table():
    def init(self):
        pass

    def show_activity_table(activities: list[Activity]):
        st.header("Existing Activities")
        st.write(f"Number of activities: `{len(activities)}`")
        st.info(
            "You can edit the activities by double clicking on a cell. Note how the plots below "
            "update automatically! You can also sort the table by clicking on the column headers.",
            icon="✍️",
        )

        # Convert activities to a format suitable for display
        activities_data = []
        for activity in activities:
            """
            # Format location as a string if it exists
            location_str = ""
            if activity.location:
                location_str = f"{activity.location.full_address} ({activity.location.coordinates.lat}, {activity.location.coordinates.lon})"
            """
            activities_data.append(
                {
                    # Hidden system fields (stored but not displayed)
                    "_id": activity.id,
                    "_created_at": activity.created_at,
                    "_updated_at": activity.updated_at,
                    # Visible fields
                    "Name": activity.name,
                    "Category": activity.category,
                    "Duration (hrs)": float(activity.duration),
                    "Description": activity.description,
                    # "Location": location_str,
                    "Physical Intensity": activity.physical_intensity,
                    "Cost Range": activity.cost_range,
                    "Social Interaction": activity.social_interaction,
                    "Indoor/Outdoor": activity.indoor_or_outdoor,
                    "Weather Suitability": activity.weather_suitability,
                    "Time of Day": activity.time_of_day,
                    "Skills": ", ".join(activity.skills) if activity.skills else "",
                    "Tags": ", ".join(activity.tags) if activity.tags else "",
                }
            )

        # Define visible columns and their configuration
        column_config = {
            "Name": st.column_config.TextColumn(
                "Name",
                help="Activity name",
                width="medium",
                required=True,
            ),
            "Category": st.column_config.SelectboxColumn(
                "Category",
                help="Activity category",
                options=[category.value for category in Category_Enum],
                required=True,
            ),
            "Physical Intensity": st.column_config.SelectboxColumn(
                "Physical Intensity",
                help="Physical intensity level",
                options=[
                    intensity.value for intensity in Physical_Intensity_Inferred_Enum
                ],
                required=True,
            ),
            "Cost Range": st.column_config.SelectboxColumn(
                "Cost Range",
                help="Cost range",
                options=[cost.value for cost in Cost_Range_Inferred_Enum],
                required=True,
            ),
            "Social Interaction": st.column_config.SelectboxColumn(
                "Social Interaction",
                help="Social interaction level",
                options=[
                    interaction.value
                    for interaction in Social_Interaction_Inferred_Enum
                ],
                required=True,
            ),
            "Indoor/Outdoor": st.column_config.SelectboxColumn(
                "Indoor/Outdoor",
                help="Whether the activity is indoor or outdoor",
                options=[status.value for status in Indoor_Or_Outdoor_Enum],
                required=True,
            ),
            "Weather Suitability": st.column_config.SelectboxColumn(
                "Weather Suitability",
                help="Weather suitability",
                options=[weather.value for weather in Weather_Suitability_Enum],
                required=True,
            ),
            "Time of Day": st.column_config.SelectboxColumn(
                "Time of Day",
                help="Suitable time of day",
                options=[time.value for time in Time_Of_Day_Enum],
                required=True,
            ),
            "Duration (hrs)": st.column_config.NumberColumn(
                "Duration (hrs)",
                help="Activity duration in hours",
                min_value=0,
                max_value=24,
                step=0.5,
                required=True,
            ),
            "Description": st.column_config.TextColumn(
                "Description",
                help="Activity description",
                width="large",
                required=True,
            ),
            "Location": st.column_config.TextColumn(
                "Location",
                help="Activity location (address and coordinates)",
                width="large",
            ),
            "Skills": st.column_config.TextColumn(
                "Skills",
                help="Comma-separated list of skills",
                width="medium",
            ),
            "Tags": st.column_config.TextColumn(
                "Tags",
                help="Comma-separated list of tags",
                width="medium",
            ),
        }

        # Display the table with data_editor, hiding system fields with underscore prefix
        edited_data = st.data_editor(
            activities_data,
            use_container_width=True,
            hide_index=True,
            column_config=column_config,
            column_order=list(column_config.keys()),  # Only show configured columns
        )

        return edited_data
