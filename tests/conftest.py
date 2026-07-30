import pytest

from app.models.product import Product


@pytest.fixture
def sample_product() -> Product:
    return Product(
        title="Sample Book",
        price=19.99,
        availability="In stock",
        rating=4,
        product_url="https://books.toscrape.com/catalogue/sample/index.html",
        image_url="https://books.toscrape.com/media/cache/sample.jpg",
    )


@pytest.fixture
def sample_products() -> list[Product]:
    return [
        Product(
            title="Book One",
            price=10.00,
            availability="In stock",
            rating=1,
            product_url="https://books.toscrape.com/catalogue/book1/index.html",
            image_url="https://books.toscrape.com/media/cache/book1.jpg",
        ),
        Product(
            title="Book Two",
            price=20.00,
            availability="In stock",
            rating=3,
            product_url="https://books.toscrape.com/catalogue/book2/index.html",
            image_url="https://books.toscrape.com/media/cache/book2.jpg",
        ),
        Product(
            title="Book Three",
            price=30.00,
            availability="Out of stock",
            rating=5,
            product_url="https://books.toscrape.com/catalogue/book3/index.html",
            image_url="https://books.toscrape.com/media/cache/book3.jpg",
        ),
    ]
