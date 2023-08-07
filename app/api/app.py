from fastapi import APIRouter, FastAPI

from app.services import make_services

from .auth.resources import router as auth_router
from .dependencies.services import inject_services
from .probes.resources import router as probes_router
from .users.resources import router as users_router


def create_app() -> FastAPI:
    app = FastAPI(
        title='Application API',
        description='API documentation',
        version="1.0.0",
    )
    app.include_router(_include_api_router(APIRouter()), prefix='/api')
    app.include_router(_include_tech_router(APIRouter()), prefix='')

    inject_services(app, make_services())

    return app


def _include_api_router(router: APIRouter) -> APIRouter:
    router.include_router(auth_router, tags=['Auth'])
    router.include_router(users_router, tags=['Users'])
    return router


def _include_tech_router(router: APIRouter) -> APIRouter:
    router.include_router(probes_router, tags=['Probes'])
    return router
