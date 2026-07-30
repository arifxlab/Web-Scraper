from app.models.product import Product
from app.utils.cleaner import DataCleaner


def test_clean_product():
    product = Product(
        title="  The Great Book   ",
        price=19.999,
        availability="   In    stock   ",
        rating=4,
        product_url="https://books.toscrape.com/catalogue/book_1/index.html",
        image_url="https://books.toscrape.com/media/cache/book.jpg",
    )

    cleaned = DataCleaner.clean(product)

    assert cleaned.title == "The Great Book"
    assert cleaned.price == 20.00
    assert cleaned.availability == "In stock"
    assert cleaned.rating == 4
    assert str(cleaned.product_url) == (
        "https://books.toscrape.com/catalogue/book_1/index.html"
    )
    assert str(cleaned.image_url) == ("https://books.toscrape.com/media/cache/book.jpg")


def test_clean_product_keeps_valid_values():
    product = Product(
        title="Python 101",
        price=25.50,
        availability="In stock",
        rating=5,
        product_url="https://books.toscrape.com/catalogue/book_2/index.html",
        image_url="https://books.toscrape.com/media/cache/book2.jpg",
    )

    cleaned = DataCleaner.clean(product)

    assert cleaned == product


def test_price_rounding():
    product = Product(
        title="Book",
        price=10.126,
        availability="In stock",
        rating=3,
        product_url="https://books.toscrape.com/catalogue/book_3/index.html",
        image_url="https://books.toscrape.com/media/cache/book3.jpg",
    )

    cleaned = DataCleaner.clean(product)

    assert cleaned.price == 10.13


def test_availability_whitespace_cleanup():
    product = Product(
        title="Book",
        price=10,
        availability="\n   In     stock\t",
        rating=3,
        product_url="https://books.toscrape.com/catalogue/book_4/index.html",
        image_url="https://books.toscrape.com/media/cache/book4.jpg",
    )

    cleaned = DataCleaner.clean(product)

    assert cleaned.availability == "In stock"
