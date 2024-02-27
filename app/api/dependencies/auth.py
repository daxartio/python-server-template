from typing import Annotated

from app_core.auth import AuthService, InvalidTokenError, UserTokenPayload
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi_di import DependsDep

from app.api.exceptions import AuthError

http_bearer = HTTPBearer()


async def get_current_user(
    token: Annotated[HTTPAuthorizationCredentials, Depends(http_bearer)],
    auth_service: Annotated[AuthService, DependsDep(AuthService)],
) -> UserTokenPayload:
    try:
        return auth_service.decode(token.credentials)
    except InvalidTokenError as err:
        raise AuthError from err
