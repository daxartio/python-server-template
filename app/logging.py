import logging
import logging.config
import sys
import traceback
from typing import Any, Dict, Optional, Union


def setup_excepthook(logger: Optional[logging.Logger] = None) -> None:
    logger = logger or logging.root

    def exception_handler(  # type:ignore
        exctype, value, traceback_
    ):  # pragma: no cover
        logger.error(''.join(traceback.format_exception(exctype, value, traceback_)))

    sys.excepthook = exception_handler


def make_config(
    level: Union[str, int] = "INFO",
    disable_existing_loggers: bool = False,
    static_fields: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    static_fields = static_fields or {}

    return {
        'version': 1,
        'disable_existing_loggers': disable_existing_loggers,
        'root': {'handlers': ['console'], 'level': level},
        'handlers': {
            'console': {
                'formatter': 'main',
                'class': 'logging.StreamHandler',
            }
        },
        'formatters': {
            'main': {
                'format': '%(message)s',
                'static_fields': static_fields,
                '()': 'app.formatter.LogFormatter',
            }
        },
    }
