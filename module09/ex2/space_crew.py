from pydantic import BaseModel, model_validator, Field, ValidationError
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
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field("planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def mission_validation(self):
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")
        has_leader = any(
            member.rank in (Rank.COMMANDER, Rank.CAPTAIN)
            for member in self.crew
        )
        if not has_leader:
            raise ValueError(
                "Crew must have at least one Commander or Captain"
            )
        if self.duration_days > 365:
            experienced = sum(
                member.years_experience >= 5 for member in self.crew
            )
            if experienced < len(self.crew) / 2:
                raise ValueError(
                    "Long missions (>365 days) need 50% experienced crew"
                )

        return self


def main():
    vm1 = {
        "member_id": "MID_001",
        "name": "Sarah Connor",
        "rank": Rank.COMMANDER,
        "age": "40",
        "specialization": "Mission Command",
        "years_experience": "16"
    }

    vm2 = {
        "member_id": "MID_002",
        "name": "John Smith",
        "rank": Rank.LIEUTENANT,
        "age": "18",
        "specialization": "Navigation",
        "years_experience": "1"
    }

    vm3 = {
        "member_id": "MID_003",
        "name": "Alice Johnson",
        "rank": Rank.OFFICER,
        "age": "30",
        "specialization": "Engineering",
        "years_experience": "10"
    }
    try:
        sarah = CrewMember(**vm1)
        john = CrewMember(**vm2)
        alice = CrewMember(**vm3)
    except (ValueError, ValidationError) as e:
        print(e)
        return

    valid_mission_data = {
        "mission_id": "M2024_MARS",
        "mission_name": "Mars Colony Establishment",
        "destination": "Mars",
        "duration_days": "900",
        "crew": [sarah, john, alice],
        "mission_status": "Planned",
        "budget_millions": "2500.0",
        "launch_date": "2026-04-09T10:00:00"
    }

    print("Space Mission Crew Validation")
    print("======================================")
    try:
        valid_mission = SpaceMission(**valid_mission_data)
    except ValidationError as e:
        print(f"Couldn't create mission: {e}")
        return
    print("Valid mission created:")
    print(f"Mission: {valid_mission.mission_name}")
    print(f"ID: {valid_mission.mission_id}")
    print(f"Destination: {valid_mission.destination}")
    print(f"Duration: {valid_mission.duration_days} days")
    print(f"Budget: ${valid_mission.budget_millions}M")
    print(f"Crew size: {len(valid_mission.crew)}")
    print("Crew members:")
    print(f"- {sarah.name} ({sarah.rank.value}) - {sarah.specialization}")
    print(f"- {john.name} ({john.rank.value}) - {john.specialization}")
    print(f"- {alice.name} ({alice.rank.value}) - {alice.specialization}")
    print("\n======================================")
    print("Expected validation error:")
    not_valid_mission_data = {
        "mission_id": "M2024_MARS",
        "mission_name": "Mars Colony Establishment",
        "destination": "Mars",
        "duration_days": "900",
        "crew": [john, alice],
        "mission_status": "Planned",
        "budget_millions": "2500.0",
        "launch_date": "2026-04-09T10:00:00"
    }
    try:
        SpaceMission(**not_valid_mission_data)
    except ValidationError as e:
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
