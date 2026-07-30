import csv
from pathlib import Path

from app.models.product import Product
from app.storage.base_writer import BaseWriter


class CSVWriter(BaseWriter):
    def write(
        self,
        filename: str,
        products: list[Product],
    ) -> Path:

        output_file = self.get_output_file(filename)

        fieldnames = [
            "title",
            "price",
            "availability",
            "rating",
            "product_url",
            "image_url",
        ]

        with output_file.open(
            "w",
            newline="",
            encoding="utf-8",
        ) as csv_file:

            writer = csv.DictWriter(
                csv_file,
                fieldnames=fieldnames,
            )

            writer.writeheader()

            for product in products:
                writer.writerow(product.model_dump(mode="json"))

        return output_file
