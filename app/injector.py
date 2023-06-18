from .core.users import UserService
from .db.database import make_session
from .db.users import UserRepository
from .settings import Settings


def inject():
    settings = Settings()
    session = make_session(settings.DATABASE_URL)
    user_service = UserService(UserRepository(session))

    return (user_service,)
