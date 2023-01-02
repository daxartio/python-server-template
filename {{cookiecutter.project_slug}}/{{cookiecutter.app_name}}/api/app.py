from fastapi import APIRouter, FastAPI

from .users.resources import router as users_router


def create_app() -> FastAPI:
    router = APIRouter()
    router.include_router(users_router, prefix='', tags=['Users'])

    app = FastAPI(title='API', description='API documentation')
    app.include_router(router, prefix='/api')

    return app
