import pytest
from fastapi.testclient import TestClient
from app.api.app import create_app


@pytest.fixture()
def client():
    with TestClient(app=create_app()) as _client:
        yield _client
