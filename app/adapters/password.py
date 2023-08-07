import parol

from app.core.password import Hash, Password


def hasher(password: Password) -> Hash:
    return parol.Password(password.encode()).hash().decode()


def verify(password: Password, hash: Hash) -> bool:
    return parol.Password(password.encode()).verify(hash.encode())
