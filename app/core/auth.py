import time
import uuid
from datetime import datetime, timedelta
from typing import Any, Callable, NamedTuple, Protocol

from .password import Hasher


class User(Protocol):
    id: uuid.UUID
    email: str
    password_hash: str
    salt: str


class Login(Protocol):
    email: str
    password: str


class Token(NamedTuple):
    access_token: str
    refresh_token: str
    token_type: str
    expires: int


class Repo(Protocol):
    async def get_user_by_email(self, email: str) -> User | None:
        pass


class AuthService:
    def __init__(
        self, repo: Repo, hasher: Hasher, encoder: Callable[[dict[str, Any]], str]
    ) -> None:
        self._repo = repo
        self._hasher = hasher
        self._encoder = encoder
        self._access_lifetime = 3600
        self._refresh_lifetime = 3600

    async def issue_token(self, login: Login) -> Token | None:
        user = await self._repo.get_user_by_email(login.email)
        if not user:
            return None

        if not self._hasher(login.password, user.salt) == user.password_hash:
            return None

        now = datetime.utcnow()
        data = {
            "sub": str(user.id),
            "exp": int(
                time.mktime(
                    (now + timedelta(seconds=self._access_lifetime)).timetuple()
                )
            ),
            "iat": int(time.mktime(now.timetuple())),
            "jti": str(uuid.uuid4()),
        }

        return Token(
            access_token=self._encoder(data),
            refresh_token="",
            token_type="Bearer",
            expires=3600,
        )
