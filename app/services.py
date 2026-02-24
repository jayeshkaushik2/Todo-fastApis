# services.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import User
from schemas import UserCreate


async def create_user(db: AsyncSession, user_data: UserCreate):
    result = await db.execute(select(User).where(User.email == user_data.email))
    existing_user = result.scalars().first()

    if existing_user:
        raise ValueError("Email already registered")

    new_user = User(name=user_data.name, email=user_data.email)

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user


async def get_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalars().first()
