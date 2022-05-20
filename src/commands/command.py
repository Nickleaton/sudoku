import logging
import os
from typing import Optional


class Command:

    def __init__(self, output_filename: Optional[str]):
        self.output_filename: Optional[str] = output_filename
        self.parent: Optional[Command] = None

    def process(self) -> None:
        logging.info(f"{self.__class__.__name__} process")

    def write(self) -> None:
        logging.info(f"Writing output to {self.output_filename}")

    def check_directory(self) -> None:
        assert self.output_filename is not None
        directory: str = os.path.dirname(self.output_filename)
        if directory == '':
            return
        if not os.path.exists(directory):  # pragma: no cover
            logging.info(f"Creating directory {directory}")
            os.makedirs(directory)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.output_filename}')"
