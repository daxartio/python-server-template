from typing import Callable, Type, TypeVar

ServiceT = TypeVar('ServiceT')

store: dict[Type[ServiceT], ServiceT] = {}


def get_service(service_cls: Type[ServiceT]) -> Callable[[], ServiceT]:
    def _get_service_lazy():
        return store[service_cls]

    return _get_service_lazy
