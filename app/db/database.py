from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import NullPool

Base = declarative_base()


def make_session(database_url: str) -> sessionmaker[AsyncSession]:
    database_url = database_url.replace("postgresql://", 'postgresql+asyncpg://')
    engine = create_async_engine(database_url, poolclass=NullPool)
    return sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
