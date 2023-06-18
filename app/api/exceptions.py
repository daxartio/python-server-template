from http import HTTPStatus

from fastapi import HTTPException


class NotFoundError(HTTPException):
    def __init__(self) -> None:
        super().__init__(HTTPStatus.NOT_FOUND, 'Not Found')
