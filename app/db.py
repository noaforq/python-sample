from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.configs import DB_URL, settings

async_engine = create_async_engine(
    DB_URL,
    echo=settings.db_echo,
)
async_session = sessionmaker(async_engine, class_=AsyncSession)  # type: ignore


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        async with session.begin():
            try:
                yield session
                await session.commit()
            except Exception:
                await session.rollback()
