from bs4 import BeautifulSoup, Tag


class HTMLParser:
    def __init__(self, html: str):
        self.soup = BeautifulSoup(html, "lxml")

    def find(self, selector: str) -> Tag | None:
        return self.soup.select_one(selector)

    def find_all(self, selector: str) -> list[Tag]:
        return self.soup.select(selector)

    def title(self) -> str:
        title = self.soup.title
        return title.get_text(strip=True) if title else ""

    def prettify(self) -> str:
        return self.soup.prettify()
