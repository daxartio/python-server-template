from app.core.users import NewUser, User
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import AsyncSession

from ._database import Base, session


class DBUser(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    def __repr__(self):
        return f'User(id={self.id})'

    @classmethod
    def new_user(cls, user: NewUser) -> 'DBUser':
        return cls(
            full_name=user.full_name,
            email=user.email,
        )


class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get(self, user_id: str) -> User:
        pass

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


user_repository = UserRepository(session)
