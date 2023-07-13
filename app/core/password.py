import hashlib


def hasher(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()
