from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BASE_URL: str = Field(
        ...,
        description="Base URL of the target website",
    )

    USER_AGENT: str = Field(
        ...,
        description="User-Agent used for HTTP requests",
    )

    REQUEST_DELAY: float = Field(
        default=1.5,
        description="Delay between requests in seconds",
    )

    TIMEOUT: int = Field(
        default=30,
        description="HTTP request timeout in seconds",
    )

    MAX_RETRIES: int = Field(
        default=3,
        description="Maximum retry attempts",
    )

    OUTPUT_DIRECTORY: str = Field(
        default="data",
        description="Directory where output files are stored",
    )

    JSON_FILENAME: str = Field(
        default="products.json",
        description="JSON output filename",
    )

    CSV_FILENAME: str = Field(
        default="products.csv",
        description="CSV output filename",
    )

    LOG_LEVEL: str = Field(
        default="INFO",
        description="Application log level",
    )

    LOG_DIRECTORY: str = Field(
        default="logs",
        description="Directory where log files are stored",
    )

    LOG_FILE: str = Field(
        default="scraper.log",
        description="Log filename",
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
