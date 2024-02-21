# Project Template

This is a Python-based web application that uses Docker for containerization, Alembic for database migrations, and Poetry for dependency management.

## Features

- FastAPI
- Sqlalchemy
  - alembic
- Access token (RS256)
- Clean Architecture
- Json logging

## Structure

- `app` is where the main application code resides. It includes several modules such as adapters, `api`, `cli`, `core`, and `db`. The `settings.py` file contains configuration settings for the application, and `deps.py` manages project dependencies.

## Quickstart

```
docker-compose build app
docker-compose run --rm app poe migrate
docker-compose run --rm app poe cli -- users create username email password
docker-compose up app
```

## Contributing

[Contributing](CONTRIBUTING.md)
