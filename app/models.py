from sqlalchemy import Column, String, Enum as SAEnum
from .base_model import BaseModel
from .model_mixins import TimeStampMixin
from enum import Enum


class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"


class Task(TimeStampMixin, BaseModel):
    __tablename__ = "tasks"

    name = Column(String, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(
        SAEnum(TaskStatus, name="task_status_enum"),
        nullable=False,
        default=TaskStatus.pending,
        server_default=TaskStatus.pending.value,
    )
