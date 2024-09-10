import logging
import time
from typing import Awaitable, Callable

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger(__name__)


class RequestLoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        start_time = time.monotonic()
        status_code = 500
        path = request.url.path

        try:
            response = await call_next(request)
            status_code = response.status_code
        finally:
            end_time = time.monotonic()
            total_time = end_time - start_time
            logger.info(
                "Request: %s %s",
                request.method,
                request.url,
                extra={
                    "latency": round(total_time, 6),
                    "status": status_code,
                    "path": path,
                },
            )

        return response
