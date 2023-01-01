from {{cookiecutter.app_name}}.core.users import NewUser, User
from sqlalchemy import Column, Integer, String

from ._database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    def __repr__(self):
        return f'User(id={self.id})'


class UserRepository:
    def __init__(self) -> None:
        pass

    def get(self, user_id: str) -> User:
        pass

    def create(self, user: NewUser) -> User:
        pass

    def update(self, user: User) -> User:
        pass

    def delete(self, user_id: str) -> None:
        pass
