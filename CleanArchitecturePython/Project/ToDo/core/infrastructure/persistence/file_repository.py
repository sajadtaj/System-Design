import json
import os
from datetime import datetime
from typing import List
from core.entities.task import Task
from core.entities.repository import TaskRepository
from core.entities.assignee import Assignee


class FileTaskRepository(TaskRepository):
    def __init__(self, file_path: str = "tasks.json"):
        self.file_path = file_path

    def save(self, tasks: List[Task]) -> None:
        try:
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump(
                    [self._task_to_dict(task) for task in tasks],
                    f,
                    indent=4,
                    ensure_ascii=False
                )
        except Exception as e:
            raise RuntimeError(f"خطا در ذخیره‌سازی فایل: {e}")

    def load(self) -> List[Task]:
        if not os.path.exists(self.file_path):
            return []

        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if not content:
                    return []  # اگر فایل خالی بود، آرایه‌ی خالی برگردان
                data = json.loads(content)
                return [
                    Task(
                        id=item["id"],
                        title=item["title"],
                        description=item["description"],
                        created_at=datetime.fromisoformat(item["created_at"]),
                        done=item["done"],
                        assignee=Assignee(**item["assignee"]) if item.get("assignee") else None
                    )
                    for item in data
                ]
        except Exception as e:
            raise RuntimeError(f"خطا در بارگذاری فایل: {e}")


    def _task_to_dict(self, task: Task) -> dict:
        return {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "created_at": task.created_at.isoformat(),
            "done": task.done,
            "assignee": {
                "id": task.assignee.id,
                "name": task.assignee.name,
                "email": task.assignee.email,
            } if task.assignee else None
        }
