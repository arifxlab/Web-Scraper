from pathlib import Path

from app.core.config import settings


class BaseWriter:
    def __init__(self):
        self.output_dir = Path(settings.OUTPUT_DIRECTORY)

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def get_output_file(
        self,
        filename: str,
    ) -> Path:
        return self.output_dir / filename
