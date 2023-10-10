from typing import Literal

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="app_database_")

    url: PostgresDsn


class LoggingSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="app_logging_")

    level: str = "INFO"


class ServerSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="app_server_")

    workers: int = 1
    reload: bool = False
    loop: Literal['none', 'auto', 'asyncio', 'uvloop'] = 'auto'
    host: str = '0.0.0.0'
    port: int = 8080
    timeout_keep_alive: int = 70
    backlog: int = 2048


class AuthSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="app_auth_")
    private_key: bytes
    public_key: bytes
    access_token_lifetime: int = 1800
