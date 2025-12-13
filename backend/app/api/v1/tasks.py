from typing import List
from fastapi import APIRouter, HTTPException, status

from backend.app.schemas.task import TaskCreate, TaskUpdate, TaskResponse

router = APIRouter()

# "Base de datos" temporal en memoria
fake_tasks_db = []
task_id_counter = 1


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TaskResponse)
def create_task(payload: TaskCreate):
    global task_id_counter

    new_task = {
        "id": task_id_counter,
        "title": payload.title,
        "description": payload.description,
    }

    fake_tasks_db.append(new_task)
    task_id_counter += 1

    return new_task


@router.get("/", response_model=List[TaskResponse])
def list_tasks():
    return fake_tasks_db


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    for task in fake_tasks_db:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Task not found",
    )


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, payload: TaskUpdate):
    for task in fake_tasks_db:
        if task["id"] == task_id:
            if payload.title is not None:
                task["title"] = payload.title
            if payload.description is not None:
                task["description"] = payload.description
            return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Task not found",
    )


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    for index, task in enumerate(fake_tasks_db):
        if task["id"] == task_id:
            fake_tasks_db.pop(index)
            return

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Task not found",
    )
