import jwt
from app_core import auth
from jwt.exceptions import InvalidTokenError
from pydantic import BaseModel, ConfigDict

ALGORITHM = 'RS256'


class JWTPayload(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    sub: str
    exp: int
    iat: int
    jti: str


class JWT:
    def __init__(self, private_key: bytes, public_key: bytes) -> None:
        self._private_key = private_key
        self._public_key = public_key

    def encode(self, payload: auth.JWTPayload) -> str:
        return jwt.encode(
            JWTPayload.model_validate(payload).model_dump(),
            self._private_key,
            algorithm=ALGORITHM,
        )

    def decode(self, token: str) -> auth.JWTPayload | None:
        try:
            payload = jwt.decode(token, self._public_key, algorithms=[ALGORITHM])
        except InvalidTokenError:
            return None

        return auth.JWTPayload(**JWTPayload.model_validate(payload).model_dump())
