FROM python:3.10-slim-buster

WORKDIR /opt/base-project

RUN apt-get update && apt-get install -y --no-install-recommends \
    make \
    && apt-get autoclean && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && pip install poetry==1.3.1 \
    && poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY {{cookiecutter.app_name}} {{cookiecutter.app_name}}
