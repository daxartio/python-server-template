from casers.pydantic import CamelAliases


class SignUp(CamelAliases):
    pass


class SignIn(CamelAliases):
    email: str
    password: str


class Token(CamelAliases):
    access_token: str
    refresh_token: str
    token_type: str = "Bearer"
    expires: int = 3600
