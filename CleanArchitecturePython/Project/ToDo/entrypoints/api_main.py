from fastapi import FastAPI
from core.interfaces.api import task_router
from core.usecases.task_usecase import TaskUseCase
from core.infrastructure.persistence.file_repository import FileTaskRepository

app = FastAPI()

# اتصال وابستگی‌ها
repo = FileTaskRepository("tasks.json")
task_usecase = TaskUseCase(repo)
task_router.task_usecase = task_usecase  # تزریق وابستگی

app.include_router(task_router.router)
