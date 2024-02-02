import logging
from datetime import datetime
from typing import Any, Dict

from kontext import current_context
from pythonjsonlogger import jsonlogger


class LogFormatter(jsonlogger.JsonFormatter):
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
            log_record['ctx'] = current_context.copy().__dict__["data"]
        except Exception:  # pragma: no cover
            log_record["ctx"] = str(current_context.copy())
