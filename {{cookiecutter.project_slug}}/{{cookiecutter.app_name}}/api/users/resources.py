from fastapi import APIRouter, Depends

from app.api.dependencies import get_service
from app.core.users import NewUser, UserService

router = APIRouter()


@router.get('/users')
async def get_users():
    pass


@router.post('/users')
async def get_users(user_service: UserService = Depends(get_service(UserService))):
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
