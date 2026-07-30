from app.analytics.statistics import StatisticsService
from app.models.product import Product


def make_product(
    title="Book",
    price=20.0,
    availability="In stock",
    rating=4,
    product_url="https://books.toscrape.com/catalogue/book/index.html",
    image_url="https://books.toscrape.com/media/cache/book.jpg",
):
    return Product(
        title=title,
        price=price,
        availability=availability,
        rating=rating,
        product_url=product_url,
        image_url=image_url,
    )


def test_total_products():
    products = [
        make_product(),
        make_product(title="Book Two"),
        make_product(title="Book Three"),
    ]

    stats = StatisticsService(products).summary()

    assert stats["total_products"] == 3


def test_average_price():
    products = [
        make_product(price=10),
        make_product(price=20),
        make_product(price=30),
    ]

    stats = StatisticsService(products).summary()

    assert stats["average_price"] == 20.00


def test_highest_price():
    products = [
        make_product(price=10),
        make_product(price=25),
        make_product(price=15),
    ]

    stats = StatisticsService(products).summary()

    assert stats["highest_price"] == 25


def test_lowest_price():
    products = [
        make_product(price=10),
        make_product(price=25),
        make_product(price=15),
    ]

    stats = StatisticsService(products).summary()

    assert stats["lowest_price"] == 10


def test_average_rating():
    products = [
        make_product(rating=1),
        make_product(rating=3),
        make_product(rating=5),
    ]

    stats = StatisticsService(products).summary()

    assert stats["average_rating"] == 3.00


def test_rating_distribution():
    products = [
        make_product(rating=1),
        make_product(rating=1),
        make_product(rating=3),
        make_product(rating=5),
        make_product(rating=5),
    ]

    stats = StatisticsService(products).summary()

    assert stats["rating_distribution"] == {
        1: 2,
        3: 1,
        5: 2,
    }


def test_availability_distribution():
    products = [
        make_product(availability="In stock"),
        make_product(availability="In stock"),
        make_product(availability="Out of stock"),
    ]

    stats = StatisticsService(products).summary()

    assert stats["availability_distribution"] == {
        "In stock": 2,
        "Out of stock": 1,
    }


def test_summary_contains_expected_keys():
    products = [
        make_product(),
    ]

    stats = StatisticsService(products).summary()

    expected_keys = {
        "total_products",
        "average_price",
        "highest_price",
        "lowest_price",
        "average_rating",
        "rating_distribution",
        "availability_distribution",
    }

    assert set(stats.keys()) == expected_keys
