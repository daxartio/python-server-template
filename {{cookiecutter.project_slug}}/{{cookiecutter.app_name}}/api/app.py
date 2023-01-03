from fastapi import APIRouter, FastAPI

from app.injector import inject

from .dependencies import store
from .users.resources import router as users_router


def create_app() -> FastAPI:
    router = APIRouter()
    router.include_router(users_router, prefix='', tags=['Users'])

    app = FastAPI(title='API', description='API documentation')
    app.include_router(router, prefix='/api')

    @app.on_event('startup')
    async def startup_event():
        services = inject()
        for service in services:
            store[type(service)] = service

    # shutdown

    return app
