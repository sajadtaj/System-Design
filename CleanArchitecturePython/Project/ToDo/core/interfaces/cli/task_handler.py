# core/interfaces/cli/task_handler.py
from typing import Optional
import argparse
import sys
from core.usecases.task_usecase import TaskUseCase
from core.entities.assignee import Assignee


class TaskHandler:
    def __init__(self, usecase: TaskUseCase):
        self.usecase = usecase

    def create_task(self, title: str, description: str,
                    assignee_id: Optional[int] = None,
                    assignee_name: Optional[str] = None,
                    assignee_email: Optional[str] = None):
        
        assignee = None
        if assignee_id and assignee_name and assignee_email:
            assignee = Assignee(
                id=assignee_id,
                name=assignee_name,
                email=assignee_email
            )

        try:
            task = self.usecase.create_task(title, description, assignee)
        except Exception as e:
            print("❌ خطا در ایجاد تسک:", e)
            sys.exit(1)

        print(f"✅ تسک ایجاد شد: {task}")



    def list_tasks(self):
        try:
            tasks = self.usecase.list_tasks()
        except Exception as e:
            print("❌ خطا در بارگذاری تسک‌ها:", e)
            sys.exit(1)

        if not tasks:
            print("❕ هیچ تسکی موجود نیست.")
            return

        for task in tasks:
            print(f"📝 ID: {task.id} | عنوان: {task.title} | توضیحات: {task.description} | وضعیت: {task.done} | مسول {task.assignee}")

    def delete_task(self, task_id: int):
        try:
            self.usecase.delete_task(task_id)
            print(f"🗑️ تسک با شناسه {task_id} حذف شد.")
        except Exception as e:
            print("❌ خطا در حذف تسک:", e)
            sys.exit(1)

            
    def update_task(self, task_id: int, title: str, description: str,
                    assignee_id: Optional[int] = None,
                    assignee_name: Optional[str] = None,
                    assignee_email: Optional[str] = None):
        assignee = None
        if assignee_id and assignee_name and assignee_email:
            assignee = Assignee(
                id=assignee_id,
                name=assignee_name,
                email=assignee_email
            )

        try:
            task = self.usecase.update_task(task_id, title, description, assignee)
            print(f"✏️ تسک ویرایش شد: {task}")
        except Exception as e:
            print("❌ خطا در ویرایش تسک:", e)
            sys.exit(1)
