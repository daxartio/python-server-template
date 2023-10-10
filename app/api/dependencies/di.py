from typing import Any, Callable, Iterable, Type, TypeVar

from fastapi import Depends, FastAPI
from starlette.requests import Request

DepT = TypeVar('DepT')


def inject_deps(app: FastAPI, deps: Iterable[DepT]) -> None:
    @app.on_event('startup')
    async def _startup() -> None:
        app.state.deps = {}
        for service in deps:
            app.state.deps[type(service)] = service


def get_dep(service_cls: Type[DepT]) -> Callable[[Request], DepT]:
    def _get_dep_lazy(request: Request) -> DepT:
        return request.app.state.deps[service_cls]

    return _get_dep_lazy


def depends_deps(service_cls: Type[DepT]) -> Any:
    return Depends(get_dep(service_cls))


DependsDep = depends_deps
