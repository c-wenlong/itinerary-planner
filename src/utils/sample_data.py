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
from decimal import Decimal
from typing import List


def load_sample_activities() -> List[Activity]:
    """Generate a list of 10 sample activities"""

    activities = [
        Activity(
            name="Mountain hiking",
            category=Category_Enum.SPORTS,
            duration=Decimal("4.5"),
            description="A challenging hike up local mountain trails with stunning viewpoints. Includes steep inclines and natural terrain.",
            location=Location_Class(
                coordinates=Point(lat=47.6062, lon=-122.3321),
                full_address="Mountain Vista Trail, Mountain Park, WA 98001",
            ),
            physical_intensity=Physical_Intensity_Inferred_Enum.HIGH,
            cost_range=Cost_Range_Inferred_Enum.LOW,
            social_interaction=Social_Interaction_Inferred_Enum.GROUP,
            weather_suitability=Weather_Suitability_Enum.DRY_WEATHER,
            time_of_day=Time_Of_Day_Enum.MORNING,
            indoor_or_outdoor=Indoor_Or_Outdoor_Enum.OUTDOOR,
            skills=["hiking", "navigation", "endurance"],
            tags=["nature", "exercise", "scenic"],
        ),
        Activity(
            name="Pottery workshop",
            category=Category_Enum.CREATIVE,
            duration=Decimal("2.5"),
            description="Learn the basics of pottery making, including hand-building techniques and wheel throwing.",
            location=Location_Class(
                coordinates=Point(lat=47.6152, lon=-122.3421),
                full_address="Creative Arts Center, 123 Art Street, Seattle, WA 98102",
            ),
            physical_intensity=Physical_Intensity_Inferred_Enum.LOW,
            cost_range=Cost_Range_Inferred_Enum.MODERATE,
            social_interaction=Social_Interaction_Inferred_Enum.GROUP,
            weather_suitability=Weather_Suitability_Enum.SHELTERED,
            time_of_day=Time_Of_Day_Enum.ANY_TIME,
            indoor_or_outdoor=Indoor_Or_Outdoor_Enum.INDOOR,
            skills=["pottery", "crafting", "creativity"],
            tags=["arts", "indoor", "hands-on"],
        ),
        Activity(
            name="Beach volleyball",
            category=Category_Enum.SPORTS,
            duration=Decimal("2.0"),
            description="Casual beach volleyball games with mixed skill levels welcome. Great way to stay active and meet new people.",
            location=Location_Class(
                coordinates=Point(lat=47.5912, lon=-122.3521),
                full_address="Sunset Beach, 2001 Beach Drive, Seattle, WA 98116",
            ),
            physical_intensity=Physical_Intensity_Inferred_Enum.HIGH,
            cost_range=Cost_Range_Inferred_Enum.FREE,
            social_interaction=Social_Interaction_Inferred_Enum.TEAM,
            weather_suitability=Weather_Suitability_Enum.DRY_WEATHER,
            time_of_day=Time_Of_Day_Enum.EVENING,
            indoor_or_outdoor=Indoor_Or_Outdoor_Enum.OUTDOOR,
            skills=["volleyball", "teamwork", "coordination"],
            tags=["sports", "beach", "team activity"],
        ),
        Activity(
            name="Meditation session",
            category=Category_Enum.SOCIAL_WELLNESS,
            duration=Decimal("1.0"),
            description="Guided meditation session focusing on mindfulness and stress relief techniques.",
            location=Location_Class(
                coordinates=Point(lat=47.6182, lon=-122.3221),
                full_address="Zen Garden Center, 789 Peace Way, Seattle, WA 98105",
            ),
            physical_intensity=Physical_Intensity_Inferred_Enum.LOW,
            cost_range=Cost_Range_Inferred_Enum.LOW,
            social_interaction=Social_Interaction_Inferred_Enum.INDIVIDUAL,
            weather_suitability=Weather_Suitability_Enum.SHELTERED,
            time_of_day=Time_Of_Day_Enum.MORNING,
            indoor_or_outdoor=Indoor_Or_Outdoor_Enum.INDOOR,
            skills=["meditation", "mindfulness"],
            tags=["wellness", "relaxation", "mental health"],
        ),
        Activity(
            name="City photography walk",
            category=Category_Enum.CREATIVE,
            duration=Decimal("3.0"),
            description="Explore the city while learning urban photography techniques. Suitable for all camera types, including smartphones.",
            location=Location_Class(
                coordinates=Point(lat=47.6092, lon=-122.3421),
                full_address="Downtown District, Pike Place Market, Seattle, WA 98101",
            ),
            physical_intensity=Physical_Intensity_Inferred_Enum.MODERATE,
            cost_range=Cost_Range_Inferred_Enum.FREE,
            social_interaction=Social_Interaction_Inferred_Enum.GROUP,
            weather_suitability=Weather_Suitability_Enum.DRY_WEATHER,
            time_of_day=Time_Of_Day_Enum.ANY_TIME,
            indoor_or_outdoor=Indoor_Or_Outdoor_Enum.OUTDOOR,
            skills=["photography", "composition"],
            tags=["creative", "urban", "photography"],
        ),
    ]

    return activities
