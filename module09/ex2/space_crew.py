from pydantic import BaseModel, model_validator, Field
from enum import Enum
from datetime import datetime


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Enum = Field(...)
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(..., True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., ge=1, le=12)
    mission_status: str = Field("planned")
    budget_millions: float = Field(..., eg=1.0, le=10000.0)

    @model_validator(mode="after")
    def mission_validation(self):
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")
            if member.rank == Rank.COMMANDER or Rank.CAPTAIN:
                valid = True
            else:
                valid = False
            if not valid:
                raise ValueError(
                    "Crew must have at least one Commander or Captain")
        if self.duration_days > 365:
            crew_size = len(self.crew)
            for member in self.crew:
                i = 0
                if member.years_experience >= 5:
                    i += 1
            if i < (crew_size // 2):
                raise ValueError(
                    "Long missions (> 365 days) "
                    "need 50% experienced crew (5+ years)")