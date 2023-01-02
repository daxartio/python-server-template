from pydantic import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_prefix = 'APP_'
