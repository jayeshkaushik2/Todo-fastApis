from fastapi import FastAPI, HTTPException
from .schemas import Task, TaskStatus, TaskUpdate
from datetime import datetime
from uuid import uuid4
import datetime as tz

app = FastAPI()
TASKS: list[Task] = []


def get_task(task_id: str):
    for task in TASKS:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.get("/tasks", response_model=list[Task])
async def tasks_list():
    return TASKS


@app.post("/tasks", response_model=Task)
async def create_task(
    task: Task,
):
    global TASKS
    task.id = uuid4().hex
    TASKS.append(task)
    return task


@app.get("/tasks/{task_id}", response_model=Task)
async def task_detail(task_id: str):
    return get_task(task_id)


@app.patch("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: str, updated: TaskUpdate):
    task = get_task(task_id=task_id)

    if updated.title is not None:
        task.title = updated.title
    if updated.description is not None:
        task.description = updated.description
    if updated.status is not None:
        task.status = updated.status

        if task.status == TaskStatus.in_progress:
            task.started_at = datetime.now(tz.timezone.utc)
        elif task.status == TaskStatus.completed:
            task.completed_at = datetime.now(tz.timezone.utc)
    return task
