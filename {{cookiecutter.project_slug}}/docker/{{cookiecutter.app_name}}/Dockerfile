FROM python:3.10-slim-buster

WORKDIR /opt/base-project

RUN pip install poetry==1.3.1 \
    && poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY {{cookiecutter.app_name}} {{cookiecutter.app_name}}
