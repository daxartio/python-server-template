import os

from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.pool import NullPool

database_url = os.environ["APP_DATABASE_URL"]

engine = create_async_engine("postgresql+asyncpg://" + database_url, poolclass=NullPool)

Base = declarative_base()


async def execute(sql):
    async with engine.connect() as conn:
        return list(await conn.execute(text(sql)))
