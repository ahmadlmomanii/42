from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import Self


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank = Field(...)
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validation(self) -> Self:
        if self.mission_id[0] != "M":
            raise ValueError("Mission ID must start with 'M'")
        x = False
        for i in self.crew:
            if i.rank == Rank.CAPTAIN or i.rank == Rank.COMMANDER:
                x = True
        if not x:
            raise ValueError("Must have at least one Commander or Captain")
        if self.duration_days > 365:
            counter = 0
            for i in self.crew:
                if i.years_experience >= 5:
                    counter += 1
            if counter < len(self.crew) / 2:
                raise ValueError(
                        "Long missions (> 365 days)"
                        " need 50% experienced crew (5+ years)"
                        )
        for i in self.crew:
            if not i.is_active:
                raise ValueError("All crew members must be active")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    crew1 = CrewMember(
            member_id="001",
            name="Ahmad",
            rank=Rank.COMMANDER,
            age=20,
            specialization="AI Engineer",
            years_experience=19
            )
    crew2 = CrewMember(
            member_id="002",
            name="Lana",
            rank=Rank.LIEUTENANT,
            age=19,
            specialization="Assistant for Ahmad",
            years_experience=3
            )
    crew3 = CrewMember(
            member_id="003",
            name="ahmad-diabat",
            rank=Rank.OFFICER,
            age=18,
            specialization="Head Chef",
            years_experience=7
            )
    print("Valid mission created:")
    mission = SpaceMission(
            mission_id="M28-11-2006",
            mission_name="Ahmad's Mission",
            destination="42Irbid",
            launch_date=datetime.now(),
            duration_days=11,
            crew=[crew1, crew2, crew3],
            budget_millions=1000
            )
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days}")
    print(f"Budget: {mission.budget_millions}")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for i in mission.crew:
        print(f"- {i.name} ({i.rank.value}) - {i.specialization}")
    print("\n=========================================")
    print("Expected validation error:")
    try:
        SpaceMission(
                mission_id="28-11-2006",
                mission_name="Ahmad's Mission",
                destination="42Aqaba",
                launch_date=datetime.now(),
                duration_days=11,
                crew=[crew1, crew2, crew3],
                budget_millions=1000
                )
    except ValidationError as e:
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
