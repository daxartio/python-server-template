from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPBearer

from app.api.dependencies.services import DependsService
from app.core.auth import AuthService, UserPayload

http_bearer = HTTPBearer()


async def get_current_user(
    token: Annotated[str, Depends(http_bearer)],
    auth_service: Annotated[AuthService, DependsService(AuthService)],
) -> UserPayload:
    return auth_service.decode(token)
