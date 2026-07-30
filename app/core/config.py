from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BASE_URL: str = Field(..., description="Base URL of the target website")
    USER_AGENT: str = Field(..., description="User-Agent used for HTTP requests")
    REQUEST_DELAY: float = Field(
        default=1.5,
        description="Delay between requests in seconds",
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()