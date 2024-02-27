import uuid
from typing import Annotated

from app_core.auth import UserTokenPayload
from app_core.users import User, UserService
from fastapi import APIRouter, Depends
from fastapi_di import DependsDep

from app.api.dependencies.auth import get_current_user
from app.api.exceptions import NotFoundError
from app.api.users import schemas

router = APIRouter()


@router.get('/users/me', response_model=schemas.User)
async def get_my_user(
    current_user: Annotated[UserTokenPayload, Depends(get_current_user)],
    user_service: Annotated[UserService, DependsDep(UserService)],
) -> User:
    user = await user_service.get(current_user.id)
    if not user:
        raise NotFoundError

    return user


@router.get(
    '/users/{user_id}',
    response_model=schemas.User,
    dependencies=[Depends(get_current_user)],
)
async def get_user(
    user_id: uuid.UUID,
    user_service: Annotated[UserService, DependsDep(UserService)],
) -> User:
    user = await user_service.get(user_id)
    if not user:
        raise NotFoundError

    return user
