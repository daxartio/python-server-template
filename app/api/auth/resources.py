from fastapi import APIRouter

from app.api.dependencies.services import DependsService
from app.api.exceptions import AuthError
from app.core.auth import AuthService, Token

from . import schemas

router = APIRouter()


@router.post('/auth/login', response_model=schemas.Token)
async def login(
    login: schemas.Login, auth_service: AuthService = DependsService(AuthService)
) -> Token:
    if token := await auth_service.issue_token(login):
        return token
    raise AuthError
