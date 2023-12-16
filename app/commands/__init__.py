import asyncio
from typing import Callable

from app.db import async_session


def run(func: Callable) -> None:
    async def init() -> None:
        async with async_session() as session:
            async with session.begin():
                try:
                    await func(session)
                    await session.commit()
                except Exception as e:
                    await session.rollback()
                    raise e

    asyncio.run(init())
