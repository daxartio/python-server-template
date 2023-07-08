from fastapi import APIRouter

router = APIRouter()


@router.post('/auth/sign-in')
async def sign_in() -> None:
    pass
