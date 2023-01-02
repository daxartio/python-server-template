import os

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import NullPool

database_url = os.environ["APP_DATABASE_URL"]

engine = create_async_engine("postgresql+asyncpg://" + database_url, poolclass=NullPool)
session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

Base = declarative_base()
