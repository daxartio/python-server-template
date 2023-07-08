import logging
import logging.config
import sys
import traceback
from typing import Any, Dict, Optional, Union


def init_logger(config: Optional[Dict[str, Any]] = None) -> None:
    if not config:
        config = get_config()
    logging.config.dictConfig(config)
    setup_excepthook(logging.root)


def setup_excepthook(logger: logging.Logger) -> None:
    def exception_handler(  # type:ignore
        exctype, value, traceback_
    ):  # pragma: no cover
        logger.error(''.join(traceback.format_exception(exctype, value, traceback_)))

    sys.excepthook = exception_handler


def get_config(level: Union[str, int] = "INFO") -> Dict[str, Any]:
    return {
        'version': 1,
        'disable_existing_loggers': True,
        'root': {'handlers': ['console'], 'level': level},
        'handlers': {
            'console': {
                'formatter': 'sage',
                'class': 'logging.StreamHandler',
            }
        },
        'formatters': {
            'sage': {
                'format': '%(message)s',
                'class': 'pythonjsonlogger.jsonlogger.JsonFormatter',
            }
        },
    }
