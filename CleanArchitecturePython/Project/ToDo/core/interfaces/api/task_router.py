from fastapi import APIRouter, HTTPException,Path
from core.usecases.task_usecase import TaskUseCase
from core.entities.assignee import Assignee
from pydantic import BaseModel, Field
from typing import Optional, List

router = APIRouter()

class AssigneeCreate(BaseModel):
    id: int
    name: str
    email: str

# مدل ورودی
class TaskCreate(BaseModel):
    title: str
    description: str
    assignee_id: Optional[int] = None


# مدل خروجی
class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    created_at: str
    done: bool
    assignee_id: Optional[int] = None


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    done: Optional[bool] = Field(None)


def convert_to_out(task) -> TaskOut:
    return TaskOut(
        id=task.id,
        title=task.title,
        description=task.description,
        created_at=task.created_at.isoformat(),
        done=task.done,
        assignee_id=task.assignee.id if task.assignee else None
    )


# وابستگی تزریق‌شده بعداً اضافه می‌شود
task_usecase: TaskUseCase = None


@router.post("/tasks", response_model=TaskOut)
def create_task(data: TaskCreate):
    assignee = None
    if data.assignee:
        assignee = Assignee(
            id=data.assignee.id,
            name=data.assignee.name,
            email=data.assignee.email
        )

    try:
        task = task_usecase.create_task(
            title=data.title,
            description=data.description,
            assignee=assignee
        )
        return convert_to_out(task)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@router.get("/tasks", response_model=List[TaskOut])
def list_tasks():
    try:
        tasks = task_usecase.list_tasks()
        return [convert_to_out(t) for t in tasks]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@router.put("/tasks/{task_id}", response_model=TaskOut)
def update_task(task_id: int, data: TaskUpdate):
    try:
        task = task_usecase.update_task(
            task_id=task_id,
            title=data.title,
            description=data.description,
            done=data.done
        )
        return convert_to_out(task)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/tasks/{task_id}")
def delete_task(task_id: int = Path(..., title="Task ID to delete")):
    try:
        task_usecase.delete_task(task_id)
        return {"message": "Task deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))