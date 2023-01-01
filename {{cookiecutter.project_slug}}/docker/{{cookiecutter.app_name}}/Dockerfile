FROM python:3.10-slim-buster

WORKDIR /opt/base-project

RUN pip install poetry

COPY pyproject.toml ./

# RUN poetry install

COPY {{cookiecutter.app_name}} {{cookiecutter.app_name}}
