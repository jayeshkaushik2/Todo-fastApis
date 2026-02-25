from pydantic import BaseModel, EmailStr
from datetime import datetime
from enum import Enum


class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"


class User(BaseModel):
    name: str
    email: EmailStr
    is_active: bool = True


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: TaskStatus | None = None


class TaskSchema(BaseModel):
    id: str | None = None
    title: str
    description: str
    status: TaskStatus = TaskStatus.pending
    started_at: datetime | None = None
    completed_at: datetime | None = None
