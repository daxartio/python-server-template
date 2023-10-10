import parol

from app.core.password import Hash, Password


def hasher(password: Password) -> Hash:
    return parol.Password(password.encode()).hash().decode()


def verify(password: Password, password_hash: Hash) -> bool:
    return parol.Password(password.encode()).verify(password_hash.encode())


def generate() -> Password:
    return parol.Password.gen().password.decode()
