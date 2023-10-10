from typing import Any, NamedTuple

import pytest
import pytest_asyncio
from fastapi.testclient import TestClient

from app.api.app import create_app
from app.core.users import User, UserService
from app.deps import Deps, make_deps


@pytest.fixture()
def client() -> Any:
    with TestClient(app=create_app()) as _client:
        yield _client


@pytest.fixture()
def deps() -> Deps:
    return make_deps()


@pytest.fixture()
def user_service(deps: Deps) -> UserService:
    return deps.user_service


@pytest_asyncio.fixture()
async def user(user_service: UserService) -> User:
    class NewUser(NamedTuple):
        full_name: str
        email: str

    return await user_service.create(NewUser('user_name', "email@ex.com"), "123")
