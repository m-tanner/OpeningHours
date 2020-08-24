from collections import deque
from datetime import time
from typing import Dict, List, Deque, Tuple

from src.pair import Pair
from src.restaurant import Restaurant


class Parser:
    def __init__(self, json_in: Dict[str, List[Dict[str, str]]]):
        self.json_in = json_in
        self.openings: Deque[Tuple[time, str]] = deque()
        self.closings: Deque[Tuple[time, str]] = deque()
        self.merged: Deque[Tuple[time, str]] = deque()

    def flatten_to_string(self) -> str:
        return str(self.flatten_to_restaurant())

    def flatten_to_restaurant(self) -> Restaurant:
        self.parse_json_in()

        while self.openings or self.closings:
            self.merged.append(self.openings.popleft())
            self.merged.append(self.closings.popleft())

        restaurant = Restaurant()
        while self.merged:
            opening = self.merged.popleft()
            closing = self.merged.popleft()
            weekday: str = opening[1].lower()
            restaurant.schedule[weekday].pairs.append(
                Pair(opening=opening[0], closing=closing[0])
            )

        return restaurant

    def parse_json_in(self) -> None:
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
        if monday_openings != monday_closings:
            # one of the closings is for Sunday, it will be the first one
            # make it the last one
            self.closings.append(self.closings.popleft())

    def to_time(self, value: str) -> time:
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
