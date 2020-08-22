from dataclasses import dataclass, field
from typing import Dict

from src.hours import Hours


@dataclass
class Restaurant:
    schedule: Dict[str, Hours] = field(default_factory=dict)

    def __post_init__(self):
        self.schedule = {
            "monday": Hours(),
            "tuesday": Hours(),
            "wednesday": Hours(),
            "thursday": Hours(),
            "friday": Hours(),
            "saturday": Hours(),
            "sunday": Hours(),
        }

    def __repr__(self):
        return "".join(
            [f"{day.title()}: {hours}\n" for day, hours in self.schedule.items()]
        )
