import pytest
from httpx import AsyncClient

from app.api.app import create_app


@pytest.fixture()
async def client():
    async with AsyncClient(app=create_app(), base_url='http://test') as client:
        yield client
