import uuid

from fastapi import APIRouter

from .schemas import SignIn, SignUp, Token

router = APIRouter()


@router.post('/auth/sign-in')
async def sign_in(sign: SignIn) -> Token:
    return Token(access_token=str(uuid.uuid4()), refresh_token=str(uuid.uuid4()))


@router.post('/auth/sign-up')
async def sign_in(sign: SignUp) -> None:
    pass
