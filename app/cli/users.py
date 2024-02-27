import asyncio

import typer
from app_core.users import User as CreatedUser
from pydantic import BaseModel

from app.deps import make_deps

app = typer.Typer()


@app.command()
def create(full_name: str, email: str, password: str) -> None:
    result = asyncio.run(_create(full_name, email, password))
    typer.echo(str(result))


class User(BaseModel):
    full_name: str
    email: str


async def _create(full_name: str, email: str, password: str) -> CreatedUser:
    deps = make_deps()
    user = User(full_name=full_name, email=email)
    return await deps.user_service.create(user, password)
