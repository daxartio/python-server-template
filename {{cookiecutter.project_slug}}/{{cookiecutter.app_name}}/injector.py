from .core.users import UserService
from .db.database import make_session
from .db.users import UserRepository


def inject():
    session = make_session()
    user_service = UserService(UserRepository(session))

    return (user_service,)
