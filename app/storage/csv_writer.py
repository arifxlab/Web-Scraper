import csv
from pathlib import Path

from app.models.product import Product


class CSVWriter:
    def __init__(self, output_dir: str = "data"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def write(
        self,
        filename: str,
        products: list[Product],
    ) -> Path:
        output_file = self.output_dir / filename

        with output_file.open(
            "w",
            newline="",
            encoding="utf-8",
        ) as csv_file:

            fieldnames = [
                "title",
                "price",
                "availability",
                "rating",
                "product_url",
                "image_url",
            ]

            writer = csv.DictWriter(
                csv_file,
                fieldnames=fieldnames,
            )

            writer.writeheader()

            for product in products:
                writer.writerow(
                    product.model_dump(mode="json")
                )

        return output_file