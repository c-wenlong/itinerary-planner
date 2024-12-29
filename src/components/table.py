import streamlit as st
from decimal import Decimal
from typing import List

from schemas import (
    Activity,
    Category_Enum,
    Cost_Range_Inferred_Enum,
    Physical_Intensity_Inferred_Enum,
    Social_Interaction_Inferred_Enum,
    Time_Of_Day_Enum,
    Weather_Suitability_Enum,
)


def generate_sample_activities() -> List[Activity]:
    """Generate a list of 10 sample activities"""

    activities = [
        Activity(
            name="Mountain hiking",
            category=Category_Enum.OUTDOOR,
            duration=Decimal("4.5"),
            description="A challenging hike up local mountain trails with stunning viewpoints. Includes steep inclines and natural terrain.",
            location="Mountain Vista Trail",
            physical_intensity=Physical_Intensity_Inferred_Enum.HIGH,
            cost_range=Cost_Range_Inferred_Enum.LOW,
            social_interaction=Social_Interaction_Inferred_Enum.GROUP,
            weather_suitability=Weather_Suitability_Enum.DRY_WEATHER,
            time_of_day=Time_Of_Day_Enum.MORNING,
            skills=["hiking", "navigation", "endurance"],
            tags=["nature", "exercise", "scenic"],
        ),
        Activity(
            name="Pottery workshop",
            category=Category_Enum.CREATIVE,
            duration=Decimal("2.5"),
            description="Learn the basics of pottery making, including hand-building techniques and wheel throwing.",
            location="Creative Arts Center",
            physical_intensity=Physical_Intensity_Inferred_Enum.LOW,
            cost_range=Cost_Range_Inferred_Enum.MODERATE,
            social_interaction=Social_Interaction_Inferred_Enum.GROUP,
            weather_suitability=Weather_Suitability_Enum.SHELTERED,
            time_of_day=Time_Of_Day_Enum.ANY_TIME,
            skills=["pottery", "crafting", "creativity"],
            tags=["arts", "indoor", "hands-on"],
        ),
        Activity(
            name="Beach volleyball",
            category=Category_Enum.SPORTS,
            duration=Decimal("2.0"),
            description="Casual beach volleyball games with mixed skill levels welcome. Great way to stay active and meet new people.",
            location="Sunset Beach",
            physical_intensity=Physical_Intensity_Inferred_Enum.HIGH,
            cost_range=Cost_Range_Inferred_Enum.FREE,
            social_interaction=Social_Interaction_Inferred_Enum.TEAM,
            weather_suitability=Weather_Suitability_Enum.DRY_WEATHER,
            time_of_day=Time_Of_Day_Enum.EVENING,
            skills=["volleyball", "teamwork", "coordination"],
            tags=["sports", "beach", "team activity"],
        ),
        Activity(
            name="Meditation session",
            category=Category_Enum.SOCIAL_WELLNESS,
            duration=Decimal("1.0"),
            description="Guided meditation session focusing on mindfulness and stress relief techniques.",
            location="Zen Garden Center",
            physical_intensity=Physical_Intensity_Inferred_Enum.LOW,
            cost_range=Cost_Range_Inferred_Enum.LOW,
            social_interaction=Social_Interaction_Inferred_Enum.INDIVIDUAL,
            weather_suitability=Weather_Suitability_Enum.SHELTERED,
            time_of_day=Time_Of_Day_Enum.MORNING,
            skills=["meditation", "mindfulness"],
            tags=["wellness", "relaxation", "mental health"],
        ),
        Activity(
            name="City photography walk",
            category=Category_Enum.CREATIVE,
            duration=Decimal("3.0"),
            description="Explore the city while learning urban photography techniques. Suitable for all camera types, including smartphones.",
            location="Downtown District",
            physical_intensity=Physical_Intensity_Inferred_Enum.MODERATE,
            cost_range=Cost_Range_Inferred_Enum.FREE,
            social_interaction=Social_Interaction_Inferred_Enum.GROUP,
            weather_suitability=Weather_Suitability_Enum.DRY_WEATHER,
            time_of_day=Time_Of_Day_Enum.ANY_TIME,
            skills=["photography", "composition"],
            tags=["creative", "urban", "photography"],
        ),
        Activity(
            name="Cooking class",
            category=Category_Enum.EDUCATIONAL,
            duration=Decimal("3.0"),
            description="Learn to cook authentic Italian dishes with a professional chef. Ingredients provided.",
            location="Culinary Institute",
            physical_intensity=Physical_Intensity_Inferred_Enum.LOW,
            cost_range=Cost_Range_Inferred_Enum.HIGH,
            social_interaction=Social_Interaction_Inferred_Enum.GROUP,
            weather_suitability=Weather_Suitability_Enum.SHELTERED,
            time_of_day=Time_Of_Day_Enum.EVENING,
            skills=["cooking", "food preparation"],
            tags=["culinary", "learning", "food"],
        ),
        Activity(
            name="Rock climbing",
            category=Category_Enum.ADVENTURE,
            duration=Decimal("2.5"),
            description="Indoor rock climbing session with instruction for beginners. All equipment provided.",
            location="Peak Climbing Gym",
            physical_intensity=Physical_Intensity_Inferred_Enum.HIGH,
            cost_range=Cost_Range_Inferred_Enum.MODERATE,
            social_interaction=Social_Interaction_Inferred_Enum.PAIR,
            weather_suitability=Weather_Suitability_Enum.SHELTERED,
            time_of_day=Time_Of_Day_Enum.ANY_TIME,
            skills=["climbing", "strength", "balance"],
            tags=["adventure", "fitness", "indoor sport"],
        ),
        Activity(
            name="Board game night",
            category=Category_Enum.ENTERTAINMENT,
            duration=Decimal("3.0"),
            description="Social evening playing various modern board games. Games provided, beginners welcome.",
            location="Meeple Board Game Cafe",
            physical_intensity=Physical_Intensity_Inferred_Enum.LOW,
            cost_range=Cost_Range_Inferred_Enum.LOW,
            social_interaction=Social_Interaction_Inferred_Enum.GROUP,
            weather_suitability=Weather_Suitability_Enum.SHELTERED,
            time_of_day=Time_Of_Day_Enum.EVENING,
            skills=["strategy", "social skills"],
            tags=["games", "social", "entertainment"],
        ),
        Activity(
            name="Museum tour",
            category=Category_Enum.CULTURAL,
            duration=Decimal("2.0"),
            description="Guided tour of the city's historical museum, focusing on local history and artifacts.",
            location="City Historical Museum",
            physical_intensity=Physical_Intensity_Inferred_Enum.LOW,
            cost_range=Cost_Range_Inferred_Enum.LOW,
            social_interaction=Social_Interaction_Inferred_Enum.GROUP,
            weather_suitability=Weather_Suitability_Enum.SHELTERED,
            time_of_day=Time_Of_Day_Enum.ANY_TIME,
            skills=["history knowledge"],
            tags=["cultural", "educational", "history"],
        ),
        Activity(
            name="Night kayaking",
            category=Category_Enum.ADVENTURE,
            duration=Decimal("2.0"),
            description="Guided kayaking experience under the stars. Equipment and safety briefing provided.",
            location="Marina Bay",
            physical_intensity=Physical_Intensity_Inferred_Enum.MODERATE,
            cost_range=Cost_Range_Inferred_Enum.HIGH,
            social_interaction=Social_Interaction_Inferred_Enum.GROUP,
            weather_suitability=Weather_Suitability_Enum.DRY_WEATHER,
            time_of_day=Time_Of_Day_Enum.NIGHT,
            skills=["kayaking", "water safety"],
            tags=["water sports", "adventure", "night activity"],
        ),
    ]

    return activities


def show_activity_table(activities: list[Activity]):
    # Show section to view and edit existing tickets in a table.
    st.header("Existing Activities")
    st.write(f"Number of activities: `{len(activities)}`")
    st.info(
        "You can edit the tickets by double clicking on a cell. Note how the plots below "
        "update automatically! You can also sort the table by clicking on the column headers.",
        icon="✍️",
    )

    # Convert activities to a format suitable for display
    activities_data = []
    for activity in activities:
        activities_data.append(
            {
                "ID": activity.id,
                "Name": activity.name,
                "Category": activity.category,
                "Duration (hrs)": float(activity.duration),
                "Description": activity.description,
                "Location": activity.location or "",
                "Physical Intensity": activity.physical_intensity,
                "Cost Range": activity.cost_range,
                "Social Interaction": activity.social_interaction,
                "Weather Suitability": activity.weather_suitability,
                "Time of Day": activity.time_of_day,
                "Skills": ", ".join(activity.skills) if activity.skills else "",
                "Tags": ", ".join(activity.tags) if activity.tags else "",
                "Created At": activity.created_at.strftime("%Y-%m-%d %H:%M"),
                "Updated At": activity.updated_at.strftime("%Y-%m-%d %H:%M"),
            }
        )

    # Display the table with data_editor
    edited_data = st.data_editor(
        activities_data,
        use_container_width=True,
        hide_index=True,
        column_config={
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
        },
        # Disable editing of system fields
        disabled=["ID", "Created At", "Updated At"],
    )

    return edited_data
