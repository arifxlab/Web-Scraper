from urllib.parse import urljoin

from app.core.config import settings
from app.extractor.product_extractor import ProductExtractor
from app.parser.html_parser import HTMLParser
from app.scraper.client import ScraperClient
from app.utils.cleaner import DataCleaner


class WebCrawler:
    def __init__(self, client: ScraperClient):
        self.client = client
        self.extractor = ProductExtractor(settings.BASE_URL)

    def crawl(self):
        products = []
        visited = set()

        next_url = settings.BASE_URL
        page = 1

        while next_url:
            print(f"\nCrawling page {page}")

            response = self.client.get(next_url)

            parser = HTMLParser(response.text)

            books = parser.find_all("article.product_pod")

            for book in books:
                product = DataCleaner.clean(
                    self.extractor.extract(book)
                )

                if str(product.product_url) not in visited:
                    visited.add(str(product.product_url))
                    products.append(product)

            next_button = parser.find("li.next a")

            if next_button:
                href = next_button["href"]
                next_url = urljoin(next_url, href)
                page += 1
            else:
                next_url = None

        return products