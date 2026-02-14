# core/entities/task.py

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from .assignee import Assignee


@dataclass
class Task:
    id: int
    title: str
    description: Optional[str] = ''
    created_at: datetime = field(default_factory=datetime.utcnow)
    done: bool = False
    assignee: Optional[Assignee] = None 

    def mark_done(self) -> None:
        self.done = True

    def mark_undone(self) -> None:
        self.done = False
