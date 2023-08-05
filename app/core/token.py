from functools import partial
from typing import Any, Callable

import jwt

ALGORITHM = 'HS256'


def encode(data: dict[str, Any], private_key: str) -> str:
    return jwt.encode(data, private_key, algorithm=ALGORITHM)


def make_encoder(private_key: str) -> Callable[[dict[str, Any]], str]:
    return partial(encode, private_key=private_key)
