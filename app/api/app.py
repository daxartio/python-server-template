from functools import partial

from fastapi import APIRouter, FastAPI

from app.injector import inject

from .auth.resources import router as auth_router
from .users.resources import router as users_router


def create_app() -> FastAPI:
    router = APIRouter()
    router.include_router(users_router, prefix='', tags=['Users'])
    router.include_router(auth_router, prefix='', tags=['Auth'])

    app = FastAPI(title='API', description='API documentation')
    app.include_router(router, prefix='/api')

    app.on_event('startup')(partial(startup, app))

    return app


async def startup(app: FastAPI) -> None:
    services = inject()
    app.state.services = {}
    for service in services:
        app.state.services[type(service)] = service
