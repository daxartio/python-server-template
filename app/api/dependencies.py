from typing import Callable, Type, TypeVar

from starlette.requests import Request

ServiceT = TypeVar('ServiceT')


def get_service(service_cls: Type[ServiceT]) -> Callable[[Request], ServiceT]:
    def _get_service_lazy(request: Request) -> ServiceT:
        return request.app.state.services[service_cls]

    return _get_service_lazy
