from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.users import NewUser, User

from .database import Base


class DBUser(Base):
    __tablename__ = 'users'
    __mapper_args__ = {'eager_defaults': True}

    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return f'User(id={self.id})'

    @classmethod
    def new_user(cls, user: NewUser) -> 'DBUser':
        return cls(
            full_name=user.full_name,
            email=user.email,
        )

    def to_user(self) -> User:
        return User(
            id=self.id,
            full_name=self.full_name,
            email=self.email,
        )


class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get(self, user_id: str) -> User | None:
        stmt = select(DBUser).filter_by(id=user_id)
        async with self._session() as session:
            result = await session.execute(stmt)
        user: DBUser | None = result.scalars().first()
        if not user:
            return
        return user.to_user()

    async def create(self, user: NewUser) -> User:
        async with self._session() as session:
            async with session.begin():
                session.add(DBUser.new_user(user))
            await session.commit()

        return User(
            id='',
            full_name=user.full_name,
            email=user.email,
        )

    async def update(self, user: User) -> User:
        pass

    async def delete(self, user_id: str) -> None:
        pass
