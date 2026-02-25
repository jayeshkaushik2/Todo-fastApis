# services.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .models import Task
from .schemas import TaskSchema


async def create_task(db: AsyncSession, data: TaskSchema):
    new_row = Task(title=data.title, description=data.description, status=data.status)
    db.add(new_row)
    await db.commit()
    await db.refresh(new_row)
    return new_row


async def get_task(db: AsyncSession, task_id: str):
    result = await db.execute(select(Task).where(Task.id == task_id))
    return result.scalars().first()


async def get_tasks(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Task).offset(skip).limit(limit))
    return result.scalars().all()
