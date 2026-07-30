from app.models.product import Product
from app.validator.validator import DatasetValidator


def make_product(
    title="Book",
    price=19.99,
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


def test_valid_dataset_passes():
    products = [
        make_product(),
        make_product(
            title="Book Two",
            product_url="https://books.toscrape.com/catalogue/book2/index.html",
        ),
    ]

    report = DatasetValidator(products).validate()

    assert report["passed"] is True
    assert report["records"] == 2
    assert report["duplicate_urls"] == 0
    assert report["missing_titles"] == 0
    assert report["invalid_prices"] == 0
    assert report["invalid_ratings"] == 0
    assert report["missing_availability"] == 0


def test_duplicate_urls_detected():
    products = [
        make_product(),
        make_product(),
    ]

    report = DatasetValidator(products).validate()

    assert report["duplicate_urls"] == 1
    assert report["passed"] is False


def test_invalid_price_detected():
    products = [
        make_product(price=0),
    ]

    report = DatasetValidator(products).validate()

    assert report["invalid_prices"] == 1
    assert report["passed"] is False


def test_invalid_rating_detected():
    products = [
        make_product(rating=0),
    ]

    report = DatasetValidator(products).validate()

    assert report["invalid_ratings"] == 1
    assert report["passed"] is False


def test_missing_availability_detected():
    products = [
        make_product(availability=""),
    ]

    report = DatasetValidator(products).validate()

    assert report["missing_availability"] == 1
    assert report["passed"] is False


def test_missing_title_detected():
    products = [
        make_product(title=""),
    ]

    report = DatasetValidator(products).validate()

    assert report["missing_titles"] == 1
    assert report["passed"] is False
