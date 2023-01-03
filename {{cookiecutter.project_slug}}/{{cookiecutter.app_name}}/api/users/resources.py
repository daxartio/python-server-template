from app.db.users import NewUser, user_repository
from fastapi import APIRouter

router = APIRouter()


@router.get('/users')
async def get_users():
    pass


@router.post('/users')
async def get_users():
    user = await user_repository.create(
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
