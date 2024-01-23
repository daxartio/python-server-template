# Project Template

The repository is python server template for new project.

## Features

- FastAPI
- Sqlalchemy
  - alembic
- Access token (RS256)
- Clean Architecture

## Quickstart

```
docker-compose build app
docker-compose run --rm app poe migrate
docker-compose run --rm app poe cli -- users create username email password
docker-compose up app
```

## Contributing

[Contributing](CONTRIBUTING.md)
