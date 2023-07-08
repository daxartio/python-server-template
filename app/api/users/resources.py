import uuid

from fastapi import APIRouter

from app.api.dependencies import DependsService
from app.api.exceptions import NotFoundError
from app.api.users import schemas
from app.core.users import UserService

router = APIRouter()


@router.get('/users/{user_id}')
async def get_users(
    user_id: uuid.UUID, user_service: UserService = DependsService(UserService)
) -> schemas.User:
    user = await user_service.get(user_id)
    if not user:
        raise NotFoundError

    return user


@router.post('/users')
async def create_users(
    user: schemas.NewUser,
    user_service: UserService = DependsService(UserService),
) -> schemas.User:
    return await user_service.create(user)
