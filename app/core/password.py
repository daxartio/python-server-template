import parol


def hasher(password: str, salt: str) -> str:
    return parol.Password(password, salt).hash
