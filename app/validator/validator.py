import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

from app.models.product import Product


class DatasetValidator:
    def __init__(self, products: list[Product]):
        self.products = products

    @classmethod
    def from_json(cls, file_path: str | Path):
        path = Path(file_path)

        with path.open(
            "r",
            encoding="utf-8",
        ) as file:
            data = json.load(file)

        products = [Product.model_validate(item) for item in data]

        return cls(products)

    @staticmethod
    def _valid_url(url: str) -> bool:
        parsed = urlparse(url)
        return parsed.scheme in {"http", "https"} and bool(parsed.netloc)

    def validate(self) -> dict:
        duplicate_urls = 0
        missing_titles = 0
        invalid_prices = 0
        invalid_ratings = 0
        invalid_product_urls = 0
        invalid_image_urls = 0
        missing_availability = 0

        url_counter = Counter(str(product.product_url) for product in self.products)

        duplicate_urls = sum(count - 1 for count in url_counter.values() if count > 1)

        for product in self.products:

            if not product.title.strip():
                missing_titles += 1

            if product.price <= 0:
                invalid_prices += 1

            if product.rating not in {1, 2, 3, 4, 5}:
                invalid_ratings += 1

            if not product.availability.strip():
                missing_availability += 1

            if not self._valid_url(str(product.product_url)):
                invalid_product_urls += 1

            if not self._valid_url(str(product.image_url)):
                invalid_image_urls += 1

        passed = all(
            value == 0
            for value in [
                duplicate_urls,
                missing_titles,
                invalid_prices,
                invalid_ratings,
                invalid_product_urls,
                invalid_image_urls,
                missing_availability,
            ]
        )

        return {
            "records": len(self.products),
            "duplicate_urls": duplicate_urls,
            "missing_titles": missing_titles,
            "invalid_prices": invalid_prices,
            "invalid_ratings": invalid_ratings,
            "invalid_product_urls": invalid_product_urls,
            "invalid_image_urls": invalid_image_urls,
            "missing_availability": missing_availability,
            "passed": passed,
        }
