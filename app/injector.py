from typing import NamedTuple

from .core.auth import AuthService
from .core.password import hasher
from .core.users import UserService
from .db.database import make_session
from .db.users import UserRepository
from .settings import DBSettings


class Services(NamedTuple):
    user_service: UserService
    auth_service: AuthService


def make_services() -> Services:
    settings = DBSettings()
    session = make_session(str(settings.url))
    user_repo = UserRepository(session)
    user_service = UserService(user_repo, hasher)
    auth_service = AuthService(user_repo, hasher)

    return Services(user_service, auth_service)
