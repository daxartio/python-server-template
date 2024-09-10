import typer

from .server import app as server
from .users import app as users

app = typer.Typer()
app.add_typer(server, name="server")
app.add_typer(users, name="users")
