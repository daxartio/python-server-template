import uuid
from typing import Awaitable, Callable

from fastapi import Request, Response
from kontext import Context, current_context
from starlette.middleware.base import BaseHTTPMiddleware

REQUEST_ID = 'X-Request-ID'
TRACE_ID = 'X-Trace-ID'


class RequestIdMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        request_id = request.headers.get(REQUEST_ID, str(uuid.uuid4()))
        trace_id = request.headers.get(TRACE_ID, str(uuid.uuid4()))

        with Context():
            current_context['request_id'] = request_id
            current_context['trace_id'] = trace_id

            response = await call_next(request)

        response.headers[REQUEST_ID] = request_id
        response.headers[TRACE_ID] = trace_id

        return response
