from fastapi import FastAPI, HTTPException, Depends
from .schemas import TaskSchema
from datetime import datetime
from uuid import uuid4
import datetime as tz
from sqlalchemy.ext.asyncio import AsyncSession
from .db import get_db, engine, Base
from .services import create_task, get_task, get_tasks

app = FastAPI()


@app.get("/tasks", response_model=list[TaskSchema])
async def task_list(db: AsyncSession = Depends(get_db)):
    return await get_tasks(db=db)


@app.post("/tasks", response_model=TaskSchema)
async def create_task(task: TaskSchema, db: AsyncSession = Depends(get_db)):
    try:
        return await create_task(db, task)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/tasks/{TaskSchema_id}", response_model=TaskSchema)
async def task_detail(task_id: str, db: AsyncSession = Depends(get_db)):
    user = await get_task(db, task_id)
    if not user:
        raise HTTPException(status_code=404, detail="Task not found")
    return user


# @app.patch("/tasks/{TaskSchema_id}", response_model=TaskSchema)
# async def update_TaskSchema(TaskSchema_id: str, updated: TaskSchemaUpdate):
#     TaskSchema = get_TaskSchema(TaskSchema_id=TaskSchema_id)

#     if updated.title is not None:
#         TaskSchema.title = updated.title
#     if updated.description is not None:
#         TaskSchema.description = updated.description
#     if updated.status is not None:
#         TaskSchema.status = updated.status

#         if TaskSchema.status == TaskSchemaStatus.in_progress:
#             TaskSchema.started_at = datetime.now(tz.timezone.utc)
#         elif TaskSchema.status == TaskSchemaStatus.completed:
#             TaskSchema.completed_at = datetime.now(tz.timezone.utc)
#     return TaskSchema
