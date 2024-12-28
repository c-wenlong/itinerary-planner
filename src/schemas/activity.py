from datetime import datetime, timezone
from typing import List, Optional
from enum import Enum
from pydantic import BaseModel, Field, field_validator
from uuid import uuid4, UUID
from decimal import Decimal


# CLASSES
class Category_Enum(str, Enum):
    UNCLASSIFIED = "UNCLASSIFIED"
    OUTDOOR = "OUTDOOR"
    INDOOR = "INDOOR"
    CULTURAL = "CULTURAL"
    SPORTS = "SPORTS"
    ENTERTAINMENT = "ENTERTAINMENT"
    EDUCATIONAL = "EDUCATIONAL"
    SOCIAL_WELLNESS = "SOCIAL WELLNESS"
    ADVENTURE = "ADVENTURE"
    CREATIVE = "CREATIVE"


class Physical_Intensity_Inferred_Enum(str, Enum):
    UNCLASSIFIED = "UNCLASSIFIED"
    LOW = "LOW"
    MODERATE = "MODERATE"
    HIGH = "HIGH"


class Cost_Range_Inferred_Enum(str, Enum):
    UNCLASSIFIED = "UNCLASSIFIED"
    FREE = "FREE"
    LOW = "LOW"
    MODERATE = "MODERATE"
    HIGH = "HIGH"
    LUXURY = "LUXURY"


class Social_Interaction_Inferred_Enum(str, Enum):
    UNCLASSIFIED = "UNCLASSIFIED"
    INDIVIDUAL = "INDIVIDUAL"
    PAIR = "PAIR"
    GROUP = "GROUP"
    TEAM = "TEAM"


class Weather_Suitability_Enum(str, Enum):
    UNCLASSIFIED = "UNCLASSIFIED"
    ALL_WEATHER = "ALL_WEATHER"
    SHELTERED = "SHELTERED"
    DRY_WEATHER = "DRY_WEATHER"


class Time_Of_Day_Enum(str, Enum):
    UNCLASSIFIED = "UNCLASSIFIED"
    ANY_TIME = "ANY_TIME"
    MORNING = "MORNING"
    EVENING = "EVENING"
    NIGHT = "NIGHT"


# FIELDS
ID_Field: UUID = Field(
    default_factory=uuid4,
    description="Unique identifier for the activity",
)

Name_Field = Field(
    ...,  # ... means required
    min_length=1,
    max_length=50,
    description="Name of the activity",
)

Description_Field = Field(
    ..., min_length=1, description="Detailed description of the issue or feature"
)

Category_Field = Field(
    default=Category_Enum.UNCLASSIFIED, description="Category of the activity"
)

Duration_in_Hours_Field = Field(
    ...,
    gt=0,
    lt=24,
    decimal_places=1,
    description="This represent the number of hours the activity will take, it can be in decimal places.",
)

# INFERRED FIELDS
Physical_Intensity_Field = Field(
    default=Physical_Intensity_Inferred_Enum.UNCLASSIFIED,
    description="Physical intensity of participating in the activity",
)

Cost_Range_Field = Field(
    default=Cost_Range_Inferred_Enum.UNCLASSIFIED,
    description="Cost range of the activity.",
)

Social_Interaction_Field = Field(
    default=Social_Interaction_Inferred_Enum.UNCLASSIFIED,
    description="The level of social interaction required for the activity",
)

Created_At_Field = Field(
    default_factory=lambda: datetime.now(timezone.utc),
    description="Timestamp when the activity was created",
)

Updated_At_Field = Field(
    default_factory=lambda: datetime.now(timezone.utc),
    description="Timestamp when the activity was last updated",
)

# OPTIONAL FIELDS
Location_Field = Field(
    default=None, min_length=1, description="Location where the activity takes place"
)

Time_Of_Day_Field = Field(
    default=Time_Of_Day_Enum.UNCLASSIFIED,
    description="Time of day the activity is suitable for",
)

Weather_Suitability_Field = Field(
    default=Weather_Suitability_Enum.UNCLASSIFIED,
    description="Weather conditions suitable for the activity",
)

Skills_List_Field = Field(
    default_factory=list, description="Skills needed or learnt through this activity"
)


Tags_Field = Field(
    default_factory=list, description="Tags associated with the activity"
)

class Activity_Inferred_Fields(BaseModel):
    physical_intensity: Physical_Intensity_Inferred_Enum
    cost_range: Cost_Range_Inferred_Enum
    social_interaction: Social_Interaction_Inferred_Enum
    weather_suitability: Weather_Suitability_Enum
    time_of_day: Time_Of_Day_Enum
    

class Activity(BaseModel):
    # System field
    id: UUID = ID_Field

    # Required fields
    name: str = Name_Field
    category: Category_Enum = Category_Field
    duration: Decimal = Duration_in_Hours_Field
    description: str = Description_Field

    # Optional fields
    location: Optional[str] = Location_Field
    skills: Optional[List[str]] = Skills_List_Field
    tags: Optional[List[str]] = Tags_Field

    # Inferred fields from description
    physical_intensity: Physical_Intensity_Inferred_Enum = Physical_Intensity_Field
    cost_range: Cost_Range_Inferred_Enum = Cost_Range_Field
    social_interaction: Social_Interaction_Inferred_Enum = Social_Interaction_Field

    # Inferred fields from category
    time_of_day: Time_Of_Day_Enum = Time_Of_Day_Field
    weather_suitability: Weather_Suitability_Enum = Weather_Suitability_Field

    # System fields
    created_at: datetime = Created_At_Field
    updated_at: datetime = Updated_At_Field

    @field_validator("name")
    def clean_name(cls, value: str) -> str:
        return " ".join(value.split()).capitalize()

    @field_validator("skills", "tags")
    def clean_lists(cls, value: List[str]) -> List[str]:
        # Remove duplicates and clean strings
        return list(set(item.strip().lower() for item in value if item.strip()))

    @field_validator("description")
    def infer_fields_from_description(cls, value: str, info) -> str:
        description = value.lower()

        # Infer physical intensity
        intensity_keywords = {
            "high": ["intense", "vigorous", "challenging"],
            "moderate": ["active", "walking", "moderate"],
            "low": ["relaxing", "casual", "gentle"],
        }

        for intensity, keywords in intensity_keywords.items():
            if any(keyword in description for keyword in keywords):
                info.data["physical_intensity"] = Physical_Intensity_Inferred_Enum(
                    intensity.upper()
                )
                break

        # Similar inference for cost_range and social_interaction
        return value

    @field_validator("duration")
    def round_to_half_hour(cls, v):
        # Convert to float for easier manipulation
        hours = float(v)
        # Round to nearest 0.5
        rounded = round(hours * 2) / 2
        # Convert back to Decimal
        return Decimal(str(rounded))

    def update(self, **kwargs):
        """Update the activity and automatically update the updated_at timestamp"""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now(timezone.utc)
        return self

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": "ACTIVITY-12345678",
                "name": "Hiking",
                "category": Category_Enum.OUTDOOR,
                "duration": 2.5,
                "description": "Hiking is a great way to explore the outdoors and get some exercise.",
                "location": "MacRitchie Reservoir",
                "physical_intensity": Physical_Intensity_Inferred_Enum.MODERATE,
                "cost_range": Cost_Range_Inferred_Enum.LOW,
                "skills": ["Endurance", "Navigation"],
                "social_interaction": Social_Interaction_Inferred_Enum.INDIVIDUAL,
                "weather_suitability": Weather_Suitability_Enum.DRY_WEATHER,
                "time_of_day": Time_Of_Day_Enum.MORNING,
                "created_at": "2024-03-28T10:00:00",
                "updated_at": "2024-03-28T10:00:00",
            }
        }
        json_encoders = {
            UUID: str,  # Convert UUID to string in JSON
            datetime: lambda v: v.isoformat(),  # Handle datetime serialization
            Decimal: float,  # Convert Decimal to float in JSON
        }


if __name__ == "__main__":
    activity = Activity(
        name="hiking",
        category="OUTDOOR",
        duration=("2.5"),
        description="Hiking is a great way to explore the outdoors and get some exercise.",
    )
    print(Activity.model_validate(activity).model_dump_json(indent=2))
