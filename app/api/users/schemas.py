import uuid

from casers.pydantic import CamelAliases


class NewUser(CamelAliases):
    full_name: str
    email: str


class User(CamelAliases):
    id: uuid.UUID
    full_name: str
    email: str
