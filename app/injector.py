from .core.password import hasher
from .core.users import UserService
from .db.database import make_session
from .db.users import UserRepository
from .settings import DBSettings


def inject() -> tuple[UserService]:
    settings = DBSettings()
    session = make_session(str(settings.url))
    user_service = UserService(UserRepository(session), hasher)

    return (user_service,)
