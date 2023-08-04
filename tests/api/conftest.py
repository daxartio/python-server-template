from typing import NamedTuple

import pytest
import pytest_asyncio
from fastapi.testclient import TestClient

from app.api.app import create_app
from app.injector import inject


@pytest.fixture()
def client():
    with TestClient(app=create_app()) as _client:
        yield _client


@pytest.fixture()
def injector():
    return inject()


@pytest.fixture()
def user_service(injector):
    (user_service, *_) = injector
    return user_service


@pytest_asyncio.fixture()
async def user(user_service):
    class NewUser(NamedTuple):
        full_name: str
        email: str

    return await user_service.create(NewUser('user_name', "email@ex.com"), "123")
