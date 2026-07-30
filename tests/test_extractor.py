from bs4 import BeautifulSoup

from app.extractor.product_extractor import ProductExtractor
from app.models.product import Product

HTML = """
<article class="product_pod">

    <img src="media/cache/book.jpg"/>

    <p class="star-rating Four"></p>

    <h3>
        <a href="catalogue/book_1/index.html"
           title="The Great Book">
            The Great Book
        </a>
    </h3>

    <p class="price_color">
        £19.99
    </p>

    <p class="availability">
        In stock
    </p>

</article>
"""


def test_extract_returns_product():
    soup = BeautifulSoup(HTML, "lxml")

    article = soup.select_one("article")

    extractor = ProductExtractor("https://books.toscrape.com/")

    product = extractor.extract(article)

    assert isinstance(product, Product)


def test_extract_title():
    soup = BeautifulSoup(HTML, "lxml")

    article = soup.select_one("article")

    extractor = ProductExtractor("https://books.toscrape.com/")

    product = extractor.extract(article)

    assert product.title == "The Great Book"


def test_extract_price():
    soup = BeautifulSoup(HTML, "lxml")

    article = soup.select_one("article")

    extractor = ProductExtractor("https://books.toscrape.com/")

    product = extractor.extract(article)

    assert product.price == 19.99


def test_extract_availability():
    soup = BeautifulSoup(HTML, "lxml")

    article = soup.select_one("article")

    extractor = ProductExtractor("https://books.toscrape.com/")

    product = extractor.extract(article)

    assert product.availability == "In stock"


def test_extract_rating():
    soup = BeautifulSoup(HTML, "lxml")

    article = soup.select_one("article")

    extractor = ProductExtractor("https://books.toscrape.com/")

    product = extractor.extract(article)

    assert product.rating == 4


def test_extract_product_url():
    soup = BeautifulSoup(HTML, "lxml")

    article = soup.select_one("article")

    extractor = ProductExtractor("https://books.toscrape.com/")

    product = extractor.extract(article)

    assert str(product.product_url) == (
        "https://books.toscrape.com/catalogue/book_1/index.html"
    )


def test_extract_image_url():
    soup = BeautifulSoup(HTML, "lxml")

    article = soup.select_one("article")

    extractor = ProductExtractor("https://books.toscrape.com/")

    product = extractor.extract(article)

    assert str(product.image_url) == ("https://books.toscrape.com/media/cache/book.jpg")


def test_all_rating_values():
    expected = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5,
    }

    for css_class, rating in expected.items():

        html = f"""
        <article class="product_pod">

            <img src="media/cache/book.jpg"/>

            <p class="star-rating {css_class}"></p>

            <h3>
                <a href="catalogue/book/index.html"
                   title="Book">
                    Book
                </a>
            </h3>

            <p class="price_color">£10.00</p>

            <p class="availability">
                In stock
            </p>

        </article>
        """

        soup = BeautifulSoup(
            html,
            "lxml",
        )

        article = soup.select_one("article")

        extractor = ProductExtractor("https://books.toscrape.com/")

        product = extractor.extract(article)

        assert product.rating == rating
