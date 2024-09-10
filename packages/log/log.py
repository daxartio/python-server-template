import logging
import logging.config
import sys
import traceback
from datetime import datetime
from typing import Any, Dict, Optional, Union

from kontext import current_context
from pythonjsonlogger import jsonlogger


def setup_excepthook(logger: Optional[logging.Logger] = None) -> None:
    logger = logger or logging.root

    def exception_handler(  # type:ignore
        exctype, value, traceback_
    ):  # pragma: no cover
        logger.error(
            "Unhandled exception",
            extra={
                "error": "".join(
                    traceback.format_exception(exctype, value, traceback_)
                ),
            },
        )

    sys.excepthook = exception_handler


def make_config(
    level: Union[str, int] = "INFO",
    static_fields: Optional[Dict[str, Any]] = None,
    exclude_fields: Optional[list[str]] = None,
) -> Dict[str, Any]:
    static_fields = static_fields or {}

    return {
        "version": 1,
        "disable_existing_loggers": False,
        "root": {"handlers": ["default"], "level": level},
        "handlers": {
            "default": {
                "formatter": "default",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            }
        },
        "formatters": {
            "default": {
                "format": "%(message)s",
                "static_fields": static_fields,
                "exclude_fields": exclude_fields or [],
                "()": "log.Formatter",
            }
        },
    }


class Formatter(jsonlogger.JsonFormatter):
    def __init__(self, *args: Any, **kwargs: Any):
        self._exclude_fields: list[str] = kwargs.pop("exclude_fields", [])
        super().__init__(*args, **kwargs)

    def add_fields(
        self,
        log_record: Dict[str, Any],
        record: logging.LogRecord,
        message_dict: Dict[str, Any],
    ) -> None:
        super().add_fields(log_record, record, message_dict)

        if not log_record.get("timestamp"):  # pragma: no cover
            now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            log_record["timestamp"] = now

        if log_record.get("level"):  # pragma: no cover
            log_record["level"] = log_record["level"].upper()
        else:
            log_record["level"] = record.levelname

        try:
            log_record["ctx"] = current_context.copy().__dict__["data"]
        except Exception:  # pragma: no cover
            log_record["ctx_error"] = str(current_context.copy())

        for field in self._exclude_fields:
            log_record.pop(field, None)
