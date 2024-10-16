from dataclasses import dataclass
from queue import Queue

@dataclass
class Publisher:
    id: int
    topic: str


@dataclass
class Subscriber:
    id: int
    name: str
    subscriptions: list[Publisher] | None
