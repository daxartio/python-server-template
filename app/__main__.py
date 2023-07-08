import uvicorn

from .api.app import create_app
from .logging import get_config, init_logger

init_logger()
uvicorn.run(create_app(), host="0.0.0.0", port=8080, log_config=get_config())
