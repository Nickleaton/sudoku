""" Base class for all image producing classes"""

import logging
import os
from pathlib import Path
from tempfile import NamedTemporaryFile

from reportlab.graphics import renderPM
from svglib.svglib import svg2rlg

from src.commands.command import Command
from src.commands.svg_command import SVGCommand


class IMGCommand(Command):

    def __init__(self, svg: SVGCommand, output_filename: Path):
        super().__init__()
        self.output_filename = output_filename
        self.svg = svg
        self.drawing = None

    def process(self) -> None:
        super().process()
        logging.info(f"Producing image file of type {self.output_filename.suffix[1:]}")
        self.svg.process()
        with NamedTemporaryFile() as ntf:
            temp_file_name = Path(ntf.name)
            ntf.close()

        logging.debug(f"Writing to temp file name {temp_file_name}")
        if self.svg.output is not None:
            with open(temp_file_name, 'w', encoding='utf-8') as file:
                file.write(self.svg.output)
        else:
            logging.error("Expecting output but it is empty")  # pragma: no cover
        self.drawing = svg2rlg(temp_file_name)
        logging.debug(f"Removing temp file name  {temp_file_name}")
        temp_file_name.unlink()

    def write(self) -> None:
        super().write()
        self.check_directory()
        renderPM.drawToFile(self.drawing, self.output_filename, fmt=self.output_filename.suffix)

    def __repr__(self):
        return f"{self.__class__.__name__}({repr(self.svg)}, {self.output_filename})"
