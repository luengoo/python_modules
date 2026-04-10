from pydantic import BaseModel, model_validator, Field, ValidationError
from enum import Enum
from datetime import datetime
from typing import Optional, List


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_recieved: Optional[str] = Field(None, max_length=500)
    is_verified: bool = False

    messages: Optional[List[str]] = None

    @model_validator(mode="after")
    def check_business_rules(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if self.contact_type == ContactType.TELEPATHIC and \
           self.witness_count < 3:
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")

        if self.signal_strength > 7.0 and not self.message_recieved:
            raise ValueError(
                "Strong signals (>7.0) must include received messages")

        return self


def main():
    print("Alien Contact Log Validation")
    print("======================================")
    valid_data = {
        "contact_id": "AC_2024_001",
        "timestamp": "2026-04-09T10:00:00",
        "location": "Area 51, Nevada",
        "contact_type": ContactType.RADIO,
        "signal_strength": "8.5",
        "duration_minutes": "45",
        "witness_count": "5",
        "message_recieved": "'Greetings from Zeta Reticuli'",
        "is_verified": True
    }
    try:
        valid = AlienContact(**valid_data)
        print("Valid contact report:")
        print(f"ID: {valid.contact_id}")
        print(f"Type: {valid.contact_type.value}")
        print(f"Location: {valid.location}")
        print(f"Signal: {valid.signal_strength}/10")
        print(f"Duration: {valid.duration_minutes} minutes")
        print(f"Witnesses: {valid.witness_count}")
        print(f"Message: {valid.message_recieved}")
    except ValidationError as e:
        print(f"Error: {e}")

    print("\n========================================")
    print("Excpected validation error:")
    not_valid_data = {
        "contact_id": "AC_2024_001",
        "timestamp": "2026-04-09T10:00:00",
        "location": "Area 51, Nevada",
        "contact_type": ContactType.TELEPATHIC,
        "signal_strength": "8.5",
        "duration_minutes": "45",
        "witness_count": "2",
        "message_recieved": "'Greetings from Zeta Reticuli'",
        "is_verified": True
    }
    try:
        AlienContact(**not_valid_data)
    except (ValueError, ValidationError) as e:
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
