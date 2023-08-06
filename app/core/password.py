from typing import Callable

import parol

Password = str
Hash = str

Hasher = Callable[[Password], Hash]
Verifier = Callable[[Password, Hash], bool]


def hasher(password: Password) -> Hash:
    return parol.Password(password.encode()).hash().decode()


def verify(password: Password, hash: Hash) -> bool:
    return parol.Password(password.encode()).verify(hash.encode())
