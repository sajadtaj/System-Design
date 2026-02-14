# core/usecases/task_usecase.py

from core.entities.task import Task
from core.entities.repository import TaskRepository
from datetime import datetime
from typing import List
from core.entities.assignee import Assignee
from typing import Optional


class TaskUseCase:
    def __init__(self, repo: TaskRepository):
        self.repo = repo

    def create_task(self, title: str, description: str, assignee: Optional[Assignee] = None) -> Task:
        tasks = self.repo.load()

        # تولید ID جدید
        new_id = max((task.id for task in tasks), default=0) + 1

        task = Task(
            id=new_id,
            title=title,
            description=description,
            created_at=datetime.utcnow(),
            done=False,
            assignee=assignee  # 🆕

        )

        tasks.append(task)
        self.repo.save(tasks)

        return task

    def list_tasks(self) -> List[Task]:
        return self.repo.load()
    
    def delete_task(self, task_id: int) -> None:

        tasks = self.repo.load()

        # حذف با فیلتر
        updated_tasks = [t for t in tasks if t.id != task_id]

        if len(updated_tasks) == len(tasks):
            raise ValueError(f"Task with id={task_id} not found")

        self.repo.save(updated_tasks)

    def update_task(self, task_id: int, title: str, description: str,
                    assignee: Optional[Assignee] = None) -> Task:
        tasks = self.repo.load()

        for i, task in enumerate(tasks):
            if task.id == task_id:
                task.title = title
                task.description = description
                task.assignee = assignee
                tasks[i] = task
                self.repo.save(tasks)
                return task

        raise ValueError(f"Task with id {task_id} not found")
