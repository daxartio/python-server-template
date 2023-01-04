from fastapi import APIRouter, Depends

from app.api.dependencies import get_service
from app.api.exceptions import NotFoundError
from app.core.users import NewUser, UserService

router = APIRouter()


@router.get('/users/{user_id}')
async def get_users(
    user_id: int, user_service: UserService = Depends(get_service(UserService))
):
    user = await user_service.get(user_id)
    if not user:
        raise NotFoundError
    return {
        'id': user.id,
        'fullName': user.full_name,
        'email': user.email,
    }


@router.post('/users')
async def create_users(user_service: UserService = Depends(get_service(UserService))):
    user = await user_service.create(
        NewUser(
            full_name='danil',
            email='danil@example.com',
        )
    )
    return {
        'id': user.id,
        'fullName': user.full_name,
        'email': user.email,
    }
