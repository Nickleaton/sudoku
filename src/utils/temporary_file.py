from pathlib import Path
from uuid import uuid4

from src.utils.config import Config

config = Config()


class TemporaryFile:

    def __init__(self):
        directory = Path(config.temporary_directory)
        directory.mkdir(exist_ok=True)
        u = str(uuid4())
        print(u)
        file_name = Path(u)
        self._name = directory / file_name

    @property
    def name(self) -> Path:
        return self._name

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._name.unlink(missing_ok=True)
