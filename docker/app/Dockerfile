FROM python:3.12-slim-bullseye AS base

WORKDIR /opt

ENV PYTHONDONTWRITEBYTECODE=off
ENV PYTHONFAULTHANDLER=on
ENV PYTHONUNBUFFERED=on

RUN pip install poetry==1.7.1 \
    && poetry config virtualenvs.create true \
    && poetry config virtualenvs.in-project true

COPY pyproject.toml poetry.lock ./

RUN poetry install --only main --no-interaction --no-ansi --no-root --no-cache

FROM base AS dev

WORKDIR /opt/dev

ENV PATH="/opt/.venv/bin:$PATH"

RUN poetry install --no-interaction --no-ansi --no-root --no-cache \
    && poetry config virtualenvs.create false

FROM python:3.12-slim-bullseye AS prod

WORKDIR /opt

ENV PATH="/opt/.venv/bin:$PATH"

COPY --from=base /opt/.venv .venv
COPY app app

CMD ["python", "-m", "app", "server", "up"]
