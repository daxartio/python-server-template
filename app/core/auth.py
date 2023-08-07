import time
import uuid
from datetime import datetime, timedelta
from typing import Any, NamedTuple, Protocol

from .password import Verifier


class User(Protocol):
    id: uuid.UUID
    email: str
    password_hash: str


class UserPayload(NamedTuple):
    id: uuid.UUID


class Credentials(Protocol):
    username: str
    password: str


class Token(NamedTuple):
    access_token: str
    refresh_token: str
    token_type: str
    expires: int


class Repo(Protocol):
    async def get_user_by_email(self, email: str) -> User | None:
        ...


class JWT(Protocol):
    def encode(self, data: dict[str, Any]) -> str:
        ...

    def decode(self, token: str) -> dict[str, Any]:
        ...


class AuthService:
    def __init__(self, repo: Repo, verify: Verifier, jwt: JWT) -> None:
        self._repo = repo
        self._verify = verify
        self._jwt = jwt
        self._access_lifetime = 3600
        self._refresh_lifetime = 3600

    def decode(self, token: str) -> UserPayload:
        data = self._jwt.decode(token)
        return UserPayload(uuid.UUID(data["sub"]))

    async def issue_token(self, creds: Credentials) -> Token | None:
        user = await self._repo.get_user_by_email(creds.username)
        if not user:
            return None

        if not self._verify(creds.password, user.password_hash):
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
            access_token=self._jwt.encode(data),
            refresh_token="",
            token_type="Bearer",
            expires=3600,
        )
