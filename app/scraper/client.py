import time

import requests

from app.core.config import settings
from app.core.logger import get_logger
from app.scraper.robots import RobotsChecker

logger = get_logger(__name__)


class ScraperClient:
    def __init__(self, robots: RobotsChecker):
        self.robots = robots

        self.session = requests.Session()

        self.session.headers.update(
            {
                "User-Agent": settings.USER_AGENT,
                "Accept": (
                    "text/html,"
                    "application/xhtml+xml,"
                    "application/xml;q=0.9,"
                    "*/*;q=0.8"
                ),
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
            }
        )

    def get(self, url: str) -> requests.Response:
        if not self.robots.can_fetch(url):
            raise PermissionError(f"robots.txt disallows crawling: {url}")

        for attempt in range(
            1,
            settings.MAX_RETRIES + 1,
        ):
            try:
                logger.info(
                    "Request %d/%d -> %s",
                    attempt,
                    settings.MAX_RETRIES,
                    url,
                )

                time.sleep(settings.REQUEST_DELAY)

                response = self.session.get(
                    url,
                    timeout=settings.TIMEOUT,
                )

                response.raise_for_status()

                return response

            except (
                requests.ConnectionError,
                requests.Timeout,
                requests.HTTPError,
            ) as exc:

                if (
                    isinstance(exc, requests.HTTPError)
                    and exc.response is not None
                    and exc.response.status_code < 500
                ):
                    raise

                if attempt == settings.MAX_RETRIES:
                    logger.exception("Maximum retries reached.")
                    raise

                backoff = 2 ** (attempt - 1)

                logger.warning(
                    "Retrying in %d second(s)...",
                    backoff,
                )

                time.sleep(backoff)

        raise RuntimeError("Unexpected request failure.")

    def close(self):
        self.session.close()

    def __enter__(self):
        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback,
    ):
        self.close()
