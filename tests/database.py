import os

import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlalchemy.pool import NullPool

from app.db.models import Base


@pytest.fixture(scope='session')
def database_url() -> str:
    return os.environ['APP_DATABASE_URL']


@pytest.fixture(scope='session')
def engine(database_url: str) -> AsyncEngine:
    return create_async_engine(
        str(database_url.replace('postgresql://', 'postgresql+asyncpg://')),
        poolclass=NullPool,
    )


@pytest_asyncio.fixture(autouse=True, scope='session')
async def _create_db(engine: AsyncEngine) -> None:
    async with engine.begin() as session:
        await session.run_sync(Base.metadata.create_all)


@pytest_asyncio.fixture(autouse=True)
async def _clean_db(engine: AsyncEngine) -> None:
    async with engine.begin() as session:
        for table in reversed(Base.metadata.sorted_tables):
            await session.execute(table.delete())
