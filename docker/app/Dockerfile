FROM python:3.11-slim-buster

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE=off
ENV PYTHONFAULTHANDLER=on
ENV PYTHONUNBUFFERED=on

RUN pip install poetry==1.6.1 \
    && poetry config virtualenvs.create false

COPY pyproject.toml ./

RUN poetry install --no-interaction --no-ansi --no-root --no-cache --all-extras

COPY app app
