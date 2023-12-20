from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import APIRouter, FastAPI

from app.deps import make_deps

from .auth.resources import router as auth_router
from .dependencies.di import inject_deps
from .probes.resources import router as probes_router
from .users.resources import router as users_router


def create_app() -> FastAPI:
    app = FastAPI(
        title='Application API',
        description='API documentation',
        version="1.0.0",
        lifespan=_lifespan,
    )
    app.include_router(_include_api_router(APIRouter()), prefix='/api')
    app.include_router(_include_tech_router(APIRouter()), prefix='')

    return app


@asynccontextmanager
async def _lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    inject_deps(app, make_deps())
    yield


def _include_api_router(router: APIRouter) -> APIRouter:
    router.include_router(auth_router, tags=['Auth'])
    router.include_router(users_router, tags=['Users'])
    return router


def _include_tech_router(router: APIRouter) -> APIRouter:
    router.include_router(probes_router, tags=['Probes'])
    return router
