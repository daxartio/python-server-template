from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_PREFIX = "app_"


class DBSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix=f"{ENV_PREFIX}database_")

    url: PostgresDsn


class LoggingSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix=f"{ENV_PREFIX}logging_")

    level: str = "INFO"


class ServerSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix=f"{ENV_PREFIX}server_")

    reload: bool = False
    host: str = "0.0.0.0"
    port: int = 8080
    timeout_keep_alive: int = 70
    backlog: int = 2048


class AuthSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix=f"{ENV_PREFIX}auth_")
    private_key: bytes
    public_key: bytes
    access_token_lifetime: int = 1800
