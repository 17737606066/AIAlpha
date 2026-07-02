from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AI Alpha Ultimate"
    app_env: str = "development"
    database_url: str = "postgresql+psycopg://aialpha:aialpha@localhost:5432/aialpha"
    redis_url: str = "redis://localhost:6379/0"
    allowed_origins: str = "http://localhost:5173"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
