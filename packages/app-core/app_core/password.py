from typing import Callable

Password = str
Hash = str

Hasher = Callable[[Password], Hash]
Verifier = Callable[[Password, Hash], bool]
