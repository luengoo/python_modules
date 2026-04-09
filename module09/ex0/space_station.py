from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(True)
    notes: Optional[str] = Field(None, max_length=200)


def main():
    print("Space Station Data Validation")
    print("===========================================")
    valid_data = {
        "station_id": "ISS001",
        "name": "International Space Station",
        "crew_size": "6",
        "power_level": "85.5",
        "oxygen_level": "92.3",
        "last_maintenance": "2026-04-09T10:00:00",
        "is_operational": True
    }
    valid = SpaceStation(**valid_data)
    if valid:
        if valid.is_operational:
            operational = "Operational"
        else:
            operational = "Not Operational"
        print("Valid station created:")
        print(f"ID: {valid.station_id}")
        print(f"Name: {valid.name}")
        print(f"Crew: {valid.crew_size} people")
        print(f"Power: {valid.power_level}%")
        print(f"Oxygen: {valid.oxygen_level}%")
        print(f"Status: {operational}\n")

    print("============================================")
    print("Expected validation error")
    not_valid_data = {
        "station_id": "ISS001",
        "name": "International Space Station",
        "crew_size": "38",
        "power_level": "85.5",
        "oxygen_level": "92.3",
        "last_maintenance": "2026-04-09T10:00:00",
        "is_operational": True
    }
    try:
        SpaceStation(**not_valid_data)
    except ValidationError:
        print("Input should be less than or equal to 20")


if __name__ == "__main__":
    main()
