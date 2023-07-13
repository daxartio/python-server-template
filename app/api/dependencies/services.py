from typing import Any, Callable, Iterable, Type, TypeVar

from fastapi import Depends, FastAPI
from starlette.requests import Request

ServiceT = TypeVar('ServiceT')


def inject_services(app: FastAPI, services: Iterable[ServiceT]) -> None:
    @app.on_event('startup')
    async def _startup() -> None:
        app.state.services = {}
        for service in services:
            app.state.services[type(service)] = service


def get_service(service_cls: Type[ServiceT]) -> Callable[[Request], ServiceT]:
    def _get_service_lazy(request: Request) -> ServiceT:
        return request.app.state.services[service_cls]

    return _get_service_lazy


def depends_service(service_cls: Type[ServiceT]) -> Any:
    return Depends(get_service(service_cls))


DependsService = depends_service
