# Python Server Template

## Features

- [x] MIT/Apache License
- [x] Task runner
  - [x] [Poe the Poet](https://github.com/nat-n/poethepoet)
- [x] [Poetry](https://python-poetry.org/) (python packaging and dependency management made easy)
- [x] Formatting
  - [x] ruff
  - [x] black
  - [x] isort
  - [x] autoflake
  - [x] unify
- [x] Linters
  - [x] ruff
  - [x] flake8
  - [x] pylint
  - [x] bandit
  - [x] black
  - [x] mypy
- [x] Pytest
- [x] Documentation with [mkdocs](https://www.mkdocs.org/)
- [x] [Conventional Commits](https://www.conventionalcommits.org/)
  - [x] git-changelog
  - [x] gitlint
- [x] Github Actions

## Quickstart

Install the latest Cookiecutter

```
pip install -U cookiecutter
```

Generate a Python project:

```
cookiecutter https://github.com/daxartio/python-server-template.git
```

Then:

```bash
cd ./your-project

docker-compose up
```
