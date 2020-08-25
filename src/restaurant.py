from dataclasses import dataclass, field
from typing import Dict, List, Set

from src.hours import Hours


@dataclass
class Restaurant:
    schedule: Dict[str, Hours] = field(default_factory=dict)
    weekdays: List[str] = field(default_factory=list)
    weekdays_const_time: Set[str] = field(default_factory=set)

    def __post_init__(self):
        self.weekdays: List[str] = [
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
            "sunday",
        ]
        self.weekdays_const_time: Set[str] = set(self.weekdays)
        self.schedule = {weekday: Hours() for weekday in self.weekdays}

    def __repr__(self):
        return "".join(
            [f"{day.title()}: {hours}\n" for day, hours in self.schedule.items()]
        )
