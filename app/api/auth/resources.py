from typing import Annotated

from fastapi import APIRouter
from fastapi.security import HTTPBasicCredentials

from app.api.dependencies.services import DependsService
from app.api.exceptions import AuthError
from app.core.auth import AuthService, Token

from . import schemas

router = APIRouter()


@router.post('/auth/token', response_model=schemas.Token)
async def login_for_access_token(
    creds: HTTPBasicCredentials,
    auth_service: Annotated[AuthService, DependsService(AuthService)],
) -> Token:
    if token := await auth_service.issue_token(creds):
        return token
    raise AuthError
