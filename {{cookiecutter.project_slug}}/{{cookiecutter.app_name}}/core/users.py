from dataclasses import dataclass
from typing import Protocol


@dataclass
class NewUser:
    full_name: str
    email: str


@dataclass
class User:
    id: str
    full_name: str
    email: str


class Repo(Protocol):
    def get(self, user_id: str) -> User:
        pass

    def create(self, user: NewUser) -> User:
        pass

    def update(self, user: User) -> User:
        pass

    def delete(self, user_id: str) -> None:
        pass


class UserService:
    def __init__(self, repo: Repo) -> None:
        self._repo = repo

    def get(self, user_id: str) -> User:
        return self._repo.get(user_id)

    def create(self, user: NewUser) -> User:
        return self._repo.create(user)

    def update(self, user: User) -> User:
        return self._repo.update(user)

    def delete(self, user_id: str) -> None:
        self._repo.delete(user_id)
