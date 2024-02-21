import logging.config

import typer
import uvicorn

from app.api.app import create_app
from app.logging import make_config, setup_excepthook
from app.settings import LoggingSettings, ServerSettings

app = typer.Typer()


@app.command()
def up() -> None:
    logging_settings = LoggingSettings()

    setup_excepthook()
    logging.config.dictConfig(make_config(level=logging_settings.level))

    uvicorn.run(
        create_app,
        factory=True,
        log_config=None,
        access_log=True,
        **ServerSettings().model_dump()
    )
