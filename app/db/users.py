import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker

from app.core.users import NewUser, User

from .database import Base


class DBUser(Base):
    __tablename__ = 'users'
    __mapper_args__ = {'eager_defaults': True}

    id: Column[uuid.UUID] = Column(UUID(as_uuid=True), primary_key=True)
    full_name: Column[str] = Column(String, nullable=False)
    email: Column[str] = Column(String, nullable=False, unique=True)
    password_hash: Column[str] = Column(String, nullable=False, unique=True)

    def __repr__(self) -> str:
        return f'User(id={self.id})'


class UserRepository:
    def __init__(self, session: sessionmaker[AsyncSession]) -> None:
        self._session = session

    async def get(self, user_id: uuid.UUID) -> User | None:
        stmt = select(DBUser).filter_by(id=user_id)
        async with self._session() as session:
            result = await session.execute(stmt)
        return result.scalars().first()

    async def create(self, user: NewUser, password_hash: str) -> DBUser:
        db_user = DBUser(
            id=uuid.uuid4(),
            full_name=user.full_name,
            email=user.email,
            password_hash=password_hash,
        )
        async with self._session() as session:
            async with session.begin():
                session.add(db_user)
            await session.commit()

        return db_user

    async def update(self, user: User) -> DBUser:
        raise NotImplementedError

    async def delete(self, user_id: uuid.UUID) -> None:
        raise NotImplementedError
