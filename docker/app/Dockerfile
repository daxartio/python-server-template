FROM python:3.11-slim-buster

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE=off
ENV PYTHONFAULTHANDLER=on
ENV PYTHONUNBUFFERED=on

RUN pip install poetry==1.5.1 \
    && poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY app app
