import uuid

from casers.pydantic import CamelAliases


class User(CamelAliases):
    id: uuid.UUID
    full_name: str
    email: str
