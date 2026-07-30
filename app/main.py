import logging

from app.core.config import settings
from app.crawler.crawler import WebCrawler
from app.scraper.client import ScraperClient
from app.scraper.robots import RobotsChecker
from app.storage.json_writer import JSONWriter


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(message)s",
)


def main():
    robots = RobotsChecker(
        settings.BASE_URL,
        settings.USER_AGENT,
    )

    robots.load()

    with ScraperClient(robots) as client:
        crawler = WebCrawler(client)

        products = crawler.crawl()

    output = JSONWriter().write(
        "products.json",
        products,
    )

    print("\n" + "=" * 60)
    print("FLYRANK WEB SCRAPER COMPLETE")
    print("=" * 60)
    print(f"Products : {len(products)}")
    print(f"Output   : {output}")
    print("=" * 60)


if __name__ == "__main__":
    main()