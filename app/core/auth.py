from typing import Callable, Protocol


class User(Protocol):
    email: str
    password_hash: str
    salt: str


class SignIn(Protocol):
    email: str
    password: str


class Repo(Protocol):
    async def get_user_by_email(self, email: str) -> User | None:
        pass


class AuthService:
    def __init__(self, repo: Repo, hasher: Callable[[str, str], str]) -> None:
        self._repo = repo
        self._hasher = hasher

    async def validate(self, sign_in: SignIn) -> bool:
        user = await self._repo.get_user_by_email(sign_in.email)
        if not user:
            return False

        return self._hasher(sign_in.password, user.salt) == user.password_hash

    def issue_token(self) -> str:
        raise NotImplementedError
