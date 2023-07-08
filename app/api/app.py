from fastapi import APIRouter, FastAPI

from app.injector import inject

from .auth.resources import router as auth_router
from .dependencies import inject_services
from .users.resources import router as users_router


def create_app() -> FastAPI:
    router = APIRouter()
    _include_router(router)

    app = FastAPI(title='API', description='API documentation')
    app.include_router(router, prefix='/api')

    inject_services(app, inject())

    return app


def _include_router(router: APIRouter) -> None:
    router.include_router(users_router, prefix='', tags=['Users'])
    router.include_router(auth_router, prefix='', tags=['Auth'])
