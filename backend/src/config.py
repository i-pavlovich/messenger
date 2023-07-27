from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    database_url: str
    secret_key: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Config()
