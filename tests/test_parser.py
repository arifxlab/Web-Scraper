from app.parser.html_parser import HTMLParser

HTML = """
<html>
    <head>
        <title>Books to Scrape</title>
    </head>

    <body>

        <div class="book">
            Book One
        </div>

        <div class="book">
            Book Two
        </div>

        <p id="price">
            £19.99
        </p>

    </body>
</html>
"""


def test_find_returns_element():
    parser = HTMLParser(HTML)

    element = parser.find("#price")

    assert element is not None
    assert element.get_text(strip=True) == "£19.99"


def test_find_returns_none_for_missing_selector():
    parser = HTMLParser(HTML)

    element = parser.find(".missing")

    assert element is None


def test_find_all_returns_all_matches():
    parser = HTMLParser(HTML)

    books = parser.find_all(".book")

    assert len(books) == 2

    assert books[0].get_text(strip=True) == "Book One"
    assert books[1].get_text(strip=True) == "Book Two"


def test_title():
    parser = HTMLParser(HTML)

    assert parser.title() == "Books to Scrape"


def test_prettify_returns_string():
    parser = HTMLParser(HTML)

    pretty = parser.prettify()

    assert isinstance(pretty, str)
    assert "<html>" in pretty
    assert "</html>" in pretty
