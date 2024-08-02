from pydantic import BaseSettings

class Settings(BaseSettings):
    astro_api_access_key: str
    astro_api_secret_key: str

    class Config:
        env_file = ".env"

settings = Settings()