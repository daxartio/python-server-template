from typing import NamedTuple

import pytest
import pytest_asyncio
from fastapi.testclient import TestClient

from app.api.app import create_app
from app.services import make_services


@pytest.fixture()
def client():
    with TestClient(app=create_app()) as _client:
        yield _client


@pytest.fixture()
def services():
    return make_services()


@pytest.fixture()
def user_service(services):
    return services.user_service


@pytest_asyncio.fixture()
async def user(user_service):
    class NewUser(NamedTuple):
        full_name: str
        email: str

    return await user_service.create(NewUser('user_name', "email@ex.com"), "123", "123")
