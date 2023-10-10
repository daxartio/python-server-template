from typing import NamedTuple

from .adapters import password, token
from .core.auth import AuthService
from .core.users import UserService
from .db.database import make_session
from .db.users import UserRepository
from .settings import AuthSettings, DBSettings


class Deps(NamedTuple):
    user_service: UserService
    auth_service: AuthService


def make_deps() -> Deps:
    settings = DBSettings()
    auth_settings = AuthSettings()
    session = make_session(str(settings.url))
    user_repo = UserRepository(session)
    user_service = UserService(user_repo, password.hasher)
    auth_service = AuthService(
        user_repo,
        password.verify,
        token.JWT(auth_settings.private_key, auth_settings.public_key),
    )

    return Deps(user_service, auth_service)