import os

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import NullPool

Base = declarative_base()


def make_session() -> sessionmaker:
    database_url = os.environ['APP_DATABASE_URL']
    engine = create_async_engine(
        'postgresql+asyncpg://' + database_url, poolclass=NullPool
    )
    return sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
