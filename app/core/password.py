from typing import Callable

import parol

Password = str
Salt = str
Hash = str

Hasher = Callable[[Password, Salt], Hash]


def hasher(password: str, salt: str) -> str:
    return parol.Password(password, salt).hash
