FROM python:3.12-slim-bookworm AS base

WORKDIR /opt

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    PYTHONDONTWRITEBYTECODE=off \
    PYTHONFAULTHANDLER=on \
    PYTHONUNBUFFERED=on

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY pyproject.toml uv.lock ./
COPY packages packages

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=packages,target=packages \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

FROM base AS dev

WORKDIR /opt/dev

ENV PATH="/opt/.venv/bin:$PATH"

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --group migration --frozen --no-install-project

FROM python:3.12-slim-bookworm AS prod

WORKDIR /opt

ENV PATH="/opt/.venv/bin:$PATH"

COPY --from=base /opt/.venv .venv
COPY app app
COPY packages packages

CMD ["python", "-m", "app", "server", "up"]
