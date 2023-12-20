from dataclasses import dataclass
from typing import Any

import pytest
import pytest_asyncio
from fastapi.testclient import TestClient

from app.api.app import create_app
from app.core.auth import AuthService
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


@pytest.fixture()
def auth_service(deps: Deps) -> AuthService:
    return deps.auth_service


@pytest.fixture()
def create_token(auth_service: AuthService) -> Any:
    return auth_service.create_token


@pytest_asyncio.fixture()
async def user(user_service: UserService) -> User:
    @dataclass
    class NewUser:
        full_name: str
        email: str

    async def _create_user(full_name: str, email: str, password: str) -> User:
        return await user_service.create(NewUser(full_name, email), password)

    return await _create_user("name", "example@email.com", "123")
