import uuid
from typing import Protocol

from .password import Hasher


class NewUser(Protocol):
    full_name: str
    email: str


class User(Protocol):
    id: uuid.UUID
    full_name: str
    email: str


class Repo(Protocol):
    async def get(self, user_id: uuid.UUID) -> User | None:
        pass

    async def create(self, user: NewUser, password_hash: str) -> User:
        pass

    async def update(self, user: User) -> User:
        pass

    async def delete(self, user_id: uuid.UUID) -> None:
        pass


class UserService:
    def __init__(self, repo: Repo, hasher: Hasher) -> None:
        self._repo = repo
        self._hasher = hasher

    async def get(self, user_id: uuid.UUID) -> User | None:
        return await self._repo.get(user_id)

    async def create(self, user: NewUser, password: str) -> User:
        return await self._repo.create(user, self._hasher(password))

    async def update(self, user: User) -> User:
        return await self._repo.update(user)

    async def delete(self, user_id: uuid.UUID) -> None:
        await self._repo.delete(user_id)
