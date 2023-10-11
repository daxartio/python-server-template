import asyncio
from typing import Any

import pytest

pytest_plugins = ['tests.database']


@pytest.fixture(scope='session')
def event_loop() -> Any:
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()
