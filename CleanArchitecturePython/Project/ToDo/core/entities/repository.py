# core/entities/repository.py

from abc import ABC, abstractmethod
from typing import List
from .task import Task


class TaskRepository(ABC):
    """
    Interface for persisting and loading Tasks
    """

    @abstractmethod
    def save(self, tasks: List[Task]) -> None:
        ...

    @abstractmethod
    def load(self) -> List[Task]:
        ...
