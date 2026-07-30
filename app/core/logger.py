import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from app.core.config import settings


def configure_logging() -> None:
    log_directory = Path(settings.LOG_DIRECTORY)
    log_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    log_file = log_directory / settings.LOG_FILE

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        "%Y-%m-%d %H:%M:%S",
    )

    root_logger = logging.getLogger()

    if root_logger.handlers:
        return

    root_logger.setLevel(
        getattr(
            logging,
            settings.LOG_LEVEL.upper(),
            logging.INFO,
        )
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = RotatingFileHandler(
        filename=log_file,
        maxBytes=1_048_576,
        backupCount=5,
        encoding="utf-8",
    )

    file_handler.setFormatter(formatter)

    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)


def get_logger(name: str) -> logging.Logger:
    configure_logging()
    return logging.getLogger(name)
