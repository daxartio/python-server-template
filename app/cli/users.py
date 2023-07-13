import asyncio

import typer
from pydantic import BaseModel

from app.core.users import User as CreatedUser
from app.injector import inject

app = typer.Typer()


@app.command()
def create(full_name: str, email: str, password: str) -> None:
    result = asyncio.run(_create(full_name, email, password))
    typer.echo(str(result))


class User(BaseModel):
    full_name: str
    email: str


async def _create(full_name: str, email: str, password: str) -> CreatedUser:
    (user_service,) = inject()
    user = User(full_name=full_name, email=email)
    return await user_service.create(user, password)
