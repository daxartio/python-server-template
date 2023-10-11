import time
import uuid
from datetime import datetime, timedelta, timezone
from typing import NamedTuple, Protocol

from .password import Verifier

TOKEN_TYPE = 'Bearer'  # noqa:S105


class User(Protocol):
    id: uuid.UUID
    email: str
    password_hash: str


class UserTokenPayload(NamedTuple):
    id: uuid.UUID


class JWTPayload(NamedTuple):
    sub: str
    exp: int
    iat: int
    jti: str


class Token(NamedTuple):
    access_token: str
    refresh_token: str
    token_type: str
    expires: int


class Credentials(Protocol):
    username: str
    password: str


class Repo(Protocol):
    async def get_user_by_email(self, email: str) -> User | None:
        ...


class JWT(Protocol):
    def encode(self, payload: JWTPayload) -> str:
        ...

    def decode(self, token: str) -> JWTPayload | None:
        ...


class InvalidTokenError(Exception):
    pass


class AuthService:
    def __init__(
        self,
        repo: Repo,
        verify: Verifier,
        jwt: JWT,
    ) -> None:
        self._repo = repo
        self._verify = verify
        self._jwt = jwt
        self._access_lifetime = 3600
        self._refresh_lifetime = 3600

    def decode(self, token: str) -> UserTokenPayload:
        if payload := self._jwt.decode(token):
            return UserTokenPayload(id=uuid.UUID(payload.sub))
        raise ValueError

    async def issue_token(self, creds: Credentials) -> Token | None:
        if not creds.username or not creds.password:
            raise ValueError("creds is invalid")

        user = await self._repo.get_user_by_email(creds.username)
        if not user:
            return None

        if not self._verify(creds.password, user.password_hash):
            return None
        return self.create_token(user.id)

    def create_token(self, user_id: uuid.UUID) -> Token:
        now = datetime.now(tz=timezone.utc)
        payload = JWTPayload(
            sub=str(user_id),
            exp=int(
                time.mktime(
                    (now + timedelta(seconds=self._access_lifetime)).timetuple(),
                ),
            ),
            iat=int(time.mktime(now.timetuple())),
            jti=str(uuid.uuid4()),
        )

        return Token(
            access_token=self._jwt.encode(payload),
            refresh_token="",
            token_type=TOKEN_TYPE,
            expires=self._access_lifetime,
        )
