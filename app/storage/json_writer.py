import json
from pathlib import Path

from app.models.product import Product
from app.storage.base_writer import BaseWriter


class JSONWriter(BaseWriter):
    def write(
        self,
        filename: str,
        products: list[Product],
    ) -> Path:

        output_file = self.get_output_file(filename)

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
