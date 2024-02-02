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
        try:
            response = await call_next(request)
        finally:
            end_time = time.monotonic()
            total_time = end_time - start_time
            logger.info(
                'Request: %s %s',
                request.method,
                request.url,
                extra={'latency': total_time},
            )

        return response
