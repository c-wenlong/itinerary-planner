from datetime import datetime
from typing import List, Optional
from enum import Enum
from pydantic import BaseModel, Field, field_validator
from uuid import uuid4


class Category_Class(str, Enum):
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


class Physical_Intensity_Inferred_Class(str, Enum):
    UNCLASSIFIED = "UNCLASSIFIED"
    LOW = "LOW"
    MODERATE = "MODERATE"
    HIGH = "HIGH"


class Cost_Range_Inferred_Class(str, Enum):
    UNCLASSIFIED = "UNCLASSIFIED"
    FREE = "FREE"
    LOW = "LOW"
    MODERATE = "MODERATE"
    HIGH = "HIGH"
    LUXURY = "LUXURY"


class Social_Interaction_Inferred_Class(str, Enum):
    UNCLASSIFIED = "UNCLASSIFIED"
    INDIVIDUAL = "INDIVIDUAL"
    PAIR = "PAIR"
    GROUP = "GROUP"
    TEAM = "TEAM"


class Weather_Suitability_Class(str, Enum):
    UNCLASSIFIED = "UNCLASSIFIED"
    ALL_WEATHER = "ALL_WEATHER"
    SHELTERED = "SHELTERED"
    DRY_WEATHER = "DRY_WEATHER"


class Time_Of_Day(str, Enum):
    UNCLASSIFIED = "UNCLASSIFIED"
    ANY_TIME = "ANY_TIME"
    MORNING = "MORNING"
    EVENING = "EVENING"
    NIGHT = "NIGHT"


ID_Field: str = Field(
    default_factory=lambda: f"ACTIVITY-{uuid4().hex[:8].upper()}",
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
    default=Category_Class.UNCLASSIFIED, description="Category of the activity"
)

Duration_in_Hours = Field(
    ...,
    gt=0,
    lt=24,
    decimal_places=2,
    description="This represent the number of hours the activity will take, it can be in decimal places.",
)

Physical_Intensity_Field = Field(
    default=Physical_Intensity_Inferred_Class.UNCLASSIFIED,
    description="Physical intensity of participating in the activity",
)

Cost_Range_Field = Field(
    default=Cost_Range_Inferred_Class.UNCLASSIFIED,
    description="Cost range of the activity.",
)

Location_Field = Field()

Seasonality_List_Field = Field(
    default_factory=list, description="Seasonality of the activity"
)

Skills_List_Field = Field(
    default_factory=list, description="Skills needed or learnt through this activity"
)

Social_Interaction_Field = Field(
    default=Social_Interaction_Inferred_Class.UNCLASSIFIED,
    description="The level of social interaction required for the activity",
)


class Activity(BaseModel):
    # Required fields
    id: str = ID_Field

    name: str = Name_Field

    category: Category_Class = Category_Field

    duration = Duration_in_Hours

    # Optional fields
    description: str = Description_Field

    # Inferred fields
    physical_intensity: Physical_Intensity_Inferred_Class = Physical_Intensity_Field

    cost_range: Cost_Range_Inferred_Class = Cost_Range_Field

    social_interaction: Social_Interaction_Inferred_Class = Social_Interaction_Field
