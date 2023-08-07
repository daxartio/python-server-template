from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.api.dependencies.services import DependsService
from app.api.exceptions import AuthError
from app.core.auth import AuthService, InvalidTokenError, UserTokenPayload

http_bearer = HTTPBearer()


async def get_current_user(
    token: Annotated[HTTPAuthorizationCredentials, Depends(http_bearer)],
    auth_service: Annotated[AuthService, DependsService(AuthService)],
) -> UserTokenPayload:
    try:
        return auth_service.decode(token.credentials)
    except InvalidTokenError as err:
        raise AuthError from err
