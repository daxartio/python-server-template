from http import HTTPStatus

from fastapi import HTTPException


class AuthError(HTTPException):
    def __init__(self) -> None:
        super().__init__(HTTPStatus.UNAUTHORIZED, 'Auth Error')


class NotFoundError(HTTPException):
    def __init__(self) -> None:
        super().__init__(HTTPStatus.NOT_FOUND, 'Not Found')
