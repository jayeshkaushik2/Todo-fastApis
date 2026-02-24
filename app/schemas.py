from pydantic import BaseModel, EmailStr
from datetime import datetime
from enum import Enum
from typing import Optional


class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"


class User(BaseModel):
    name: str
    email: EmailStr
    is_active: bool = True


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None


class Task(BaseModel):
    id: str | None = None
    title: str
    description: str
    status: TaskStatus = TaskStatus.pending
    started_at: datetime | None = None
    completed_at: datetime | None = None
