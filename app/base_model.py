# models.py
import uuid
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID
from .db import Base
from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func

# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.future import select


class BaseModel(Base):
    __abstract__ = True  # THIS is how SQLAlchemy knows it's abstract
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)

    # @classmethod
    # async def all(cls, db: AsyncSession):
    #     result = await db.execute(select(cls))
    #     return result.scalars().first()
