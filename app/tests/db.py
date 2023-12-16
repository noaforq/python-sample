from typing import AsyncGenerator

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_scoped_session, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.configs import DB_URL

TEST_DB_URL = DB_URL.set(database="test")
TEST_DB_URL_BASE = TEST_DB_URL.set(database="")

async_engine = create_async_engine(TEST_DB_URL)
async_session = sessionmaker(async_engine, class_=AsyncSession)  # type: ignore
session_factory = async_scoped_session(async_session, lambda: True)


async def get_test_session() -> AsyncGenerator:
    await session_factory().flush()
    async with session_factory().begin_nested() as s:
        try:
            yield s.session
            await s.session.flush()
        except Exception:
            await s.rollback()


async def create_test_database() -> None:
    engine = create_async_engine(TEST_DB_URL_BASE, isolation_level="AUTOCOMMIT")
    async with engine.connect() as conn:
        await conn.exec_driver_sql("CREATE DATABASE test;")


async def drop_test_database() -> None:
    engine = create_async_engine(TEST_DB_URL_BASE, isolation_level="AUTOCOMMIT")
    async with engine.connect() as conn:
        await conn.exec_driver_sql("DROP DATABASE IF EXISTS test;")


async def reset_sequence(session: AsyncSession) -> None:
    results = await session.execute(text("SELECT s.sequencename AS sequence_name FROM pg_sequences AS s WHERE s.last_value IS NOT null;"))
    for result in results.all():
        sequence_name = result[0]
        await session.execute(text(f"SELECT SETVAL ('{sequence_name}', 1, false);"))
