from collections import deque
from datetime import time
from typing import Dict, List, Deque, Tuple


class Parser:
    __slots__ = [
        "json_in",
        "openings",
        "closings",
        "merged"
    ]

    def __init__(self, json_in: Dict[str, List[Dict[str, str]]]):
        self.json_in = json_in
        self.openings: Deque[Tuple[time, str]] = deque()
        self.closings: Deque[Tuple[time, str]] = deque()
        self.merged: Deque[Tuple[time, str]] = deque()

    def parse_json_in(self) -> Dict[str, Deque[Tuple[time, str]]]:
        for day, events in self.json_in.items():
            for event in events:
                event_type = event.get("type")
                event_value = event.get("value")
                new_time = self.to_time(value=event_value)
                if event_type == "open":
                    self.openings.append((new_time, day))
                elif event_type == "close":
                    self.closings.append((new_time, day))
                else:
                    raise RuntimeError("Unknown event type provided.")

        monday_openings = len(
            [event for event in self.openings if event[1].lower() == "monday"]
        )
        monday_closings = len(
            [event for event in self.closings if event[1].lower() == "monday"]
        )
        if monday_closings > monday_openings:
            # one of the closings is for Sunday, it will be the first one
            # make it the last one
            self.closings.append(self.closings.popleft())

        return {key: getattr(self, key, None) for key in self.__slots__}

    def to_time(self, value: str) -> time:
        if not value:
            raise RuntimeError("Event value (time) required. Can't be null.")

        seconds = int(value)
        self.validate_seconds(value=seconds)

        hours = self.get_hours_from_seconds(seconds)
        minutes = self.get_minutes_from_seconds(seconds) - hours * 60

        return time(hour=hours, minute=minutes)

    @staticmethod
    def validate_seconds(value: int) -> None:
        if 0 > value:
            raise RuntimeError("Seconds cannot be less than 0.")
        if value > 86399:
            raise RuntimeError("Seconds cannot be greater than 86399.")

    def get_hours_from_seconds(self, seconds: int) -> int:
        return self.get_minutes_from_seconds(seconds) // 60

    @staticmethod
    def get_minutes_from_seconds(seconds: int) -> int:
        return seconds // 60
