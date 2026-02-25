# models.py
import uuid
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID
from .db import Base
from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func


class TimeStampMixin:
    created = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    updated = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
