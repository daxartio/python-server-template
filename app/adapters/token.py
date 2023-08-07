from typing import Any

import jwt
from jwt.exceptions import InvalidTokenError

from app.core import auth

ALGORITHM = 'HS256'


class JWT:
    def __init__(self, private_key: str) -> None:
        self._private_key = private_key

    def encode(self, data: dict[str, Any]) -> str:
        return jwt.encode(data, self._private_key, algorithm=ALGORITHM)

    def decode(self, token: str) -> dict[str, Any]:
        try:
            return jwt.decode(token, self._private_key, algorithms=[ALGORITHM])
        except InvalidTokenError as err:
            raise auth.InvalidTokenError from err
