import uuid

from fastapi import APIRouter

from app.api.dependencies.services import DependsService
from app.api.exceptions import AuthError
from app.core.auth import AuthService

from .schemas import SignIn, SignUp, Token

router = APIRouter()


@router.post('/auth/sign-in')
async def sign_in(
    sign_in: SignIn, auth_service: AuthService = DependsService(AuthService)
) -> Token:
    if not await auth_service.validate(sign_in):
        raise AuthError
    return Token(access_token=str(uuid.uuid4()), refresh_token=str(uuid.uuid4()))


@router.post('/auth/sign-up')
async def sign_up(sign_up: SignUp) -> None:
    pass
