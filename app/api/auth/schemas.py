from casers.pydantic import CamelAliases


class Login(CamelAliases):
    email: str
    password: str


class Token(CamelAliases):
    access_token: str
    refresh_token: str
    token_type: str
    expires: int
