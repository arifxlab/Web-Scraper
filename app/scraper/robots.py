import logging
from urllib.parse import urljoin
from urllib.robotparser import RobotFileParser


logger = logging.getLogger(__name__)


class RobotsChecker:
    def __init__(self, base_url: str, user_agent: str):
        self.base_url = base_url
        self.user_agent = user_agent

        self.robots_url = urljoin(self.base_url, "robots.txt")

        self.parser = RobotFileParser()
        self.parser.set_url(self.robots_url)

    def load(self) -> None:
        logger.info("Loading robots.txt from %s", self.robots_url)

        try:
            self.parser.read()
            logger.info("Successfully loaded robots.txt")
        except Exception as exc:
            logger.exception("Failed to load robots.txt")
            raise exc

    def can_fetch(self, url: str) -> bool:
        logger.info("Checking robots permission for %s", url)

        allowed = self.parser.can_fetch(self.user_agent, url)

        logger.info("Allowed: %s", allowed)

        return allowed