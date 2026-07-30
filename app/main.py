from app.cli import app
from app.core.logger import configure_logging

configure_logging()


if __name__ == "__main__":
    app()
