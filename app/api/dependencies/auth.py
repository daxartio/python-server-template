from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.api.dependencies.di import DependsDep
from app.api.exceptions import AuthError
from app.core.auth import AuthService, InvalidTokenError, UserTokenPayload

http_bearer = HTTPBearer()


async def get_current_user(
    token: Annotated[HTTPAuthorizationCredentials, Depends(http_bearer)],
    auth_service: Annotated[AuthService, DependsDep(AuthService)],
) -> UserTokenPayload:
    try:
        return auth_service.decode(token.credentials)
    except InvalidTokenError as err:
        raise AuthError from err
