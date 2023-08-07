import uuid
from typing import Annotated

from fastapi import APIRouter, Depends

from app.api.dependencies.services import DependsService
from app.api.dependencies.auth import get_current_user
from app.api.exceptions import NotFoundError
from app.api.users import schemas
from app.core.users import User, UserService

router = APIRouter()


@router.get('/users/{user_id}', response_model=schemas.User)
async def get_users(
    user_id: uuid.UUID,
    user_service: Annotated[UserService, DependsService(UserService)],
) -> User:
    user = await user_service.get(user_id)
    if not user:
        raise NotFoundError

    return user
