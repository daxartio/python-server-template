import uuid
from typing import Protocol


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

    async def create(self, user: NewUser) -> User:
        pass

    async def update(self, user: User) -> User:
        pass

    async def delete(self, user_id: uuid.UUID) -> None:
        pass


class UserService:
    def __init__(self, repo: Repo) -> None:
        self._repo = repo

    async def get(self, user_id: uuid.UUID) -> User | None:
        return await self._repo.get(user_id)

    async def create(self, user: NewUser) -> User:
        return await self._repo.create(user)

    async def update(self, user: User) -> User:
        return await self._repo.update(user)

    async def delete(self, user_id: uuid.UUID) -> None:
        await self._repo.delete(user_id)
