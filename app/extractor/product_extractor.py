from urllib.parse import urljoin

from bs4 import Tag

from app.models.product import Product


class ProductExtractor:
    RATING_MAP = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5,
    }

    def __init__(self, base_url: str):
        self.base_url = base_url

    def extract(self, article: Tag) -> Product:
        title = article.select_one("h3 a")["title"].strip()

        price_text = article.select_one(".price_color").get_text(strip=True)
        price = float(price_text.replace("£", "").replace("Â", ""))

        availability = (
            article.select_one(".availability")
            .get_text(strip=True)
        )

        rating_classes = article.select_one("p.star-rating")["class"]
        rating = 0

        for cls in rating_classes:
            if cls in self.RATING_MAP:
                rating = self.RATING_MAP[cls]
                break

        product_href = article.select_one("h3 a")["href"]
        image_src = article.select_one("img")["src"]

        product_url = urljoin(
            self.base_url,
            product_href,
        )

        image_url = urljoin(
            self.base_url,
            image_src,
        )

        return Product(
            title=title,
            price=price,
            availability=availability,
            rating=rating,
            product_url=product_url,
            image_url=image_url,
        )