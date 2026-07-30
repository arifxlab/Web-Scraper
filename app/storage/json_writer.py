import json
from pathlib import Path

from app.models.product import Product


class JSONWriter:
    def __init__(self, output_dir: str = "data"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def write(self, filename: str, products: list[Product]) -> Path:
        output_file = self.output_dir / filename

        with output_file.open(
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                [product.model_dump(mode="json") for product in products],
                file,
                indent=4,
                ensure_ascii=False,
            )

        return output_file