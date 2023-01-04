from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_prefix = 'APP_'
