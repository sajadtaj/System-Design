# core/entities/assignee.py

from dataclasses import dataclass

@dataclass
class Assignee:
    id: int
    name: str
    email: str
