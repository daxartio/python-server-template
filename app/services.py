from typing import NamedTuple

from .core.auth import AuthService
from .core.password import hasher, verify
from .core.token import make_encoder
from .core.users import UserService
from .db.database import make_session
from .db.users import UserRepository
from .settings import AuthSettings, DBSettings


class Services(NamedTuple):
    user_service: UserService
    auth_service: AuthService


def make_services() -> Services:
    settings = DBSettings()
    auth_settings = AuthSettings()
    session = make_session(str(settings.url))
    user_repo = UserRepository(session)
    user_service = UserService(user_repo, hasher)
    auth_service = AuthService(
        user_repo, verify, make_encoder(auth_settings.private_key)
    )

    return Services(user_service, auth_service)
