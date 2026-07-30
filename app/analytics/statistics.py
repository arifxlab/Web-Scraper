from collections import Counter
from pathlib import Path

from app.models.product import Product


class StatisticsService:
    def __init__(self, products: list[Product]):
        self.products = products

    @classmethod
    def from_json(cls, file_path: str | Path):
        import json

        path = Path(file_path)

        with path.open(
            "r",
            encoding="utf-8",
        ) as file:
            data = json.load(file)

        products = [Product.model_validate(item) for item in data]

        return cls(products)

    def summary(self) -> dict:
        prices = [product.price for product in self.products]
        ratings = [product.rating for product in self.products]
        availability = [product.availability for product in self.products]

        return {
            "total_products": len(self.products),
            "average_price": round(sum(prices) / len(prices), 2),
            "highest_price": max(prices),
            "lowest_price": min(prices),
            "average_rating": round(sum(ratings) / len(ratings), 2),
            "rating_distribution": dict(sorted(Counter(ratings).items())),
            "availability_distribution": dict(Counter(availability)),
        }
