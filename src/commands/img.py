import logging
import os
from tempfile import NamedTemporaryFile

from reportlab.graphics import renderPM
from svglib.svglib import svg2rlg

from src.commands.command import Command
from src.commands.svg import SVG


class IMG(Command):

    def __init__(self, config_filename: str, output_filename: str, file_format: str = "jpg"):
        super().__init__(config_filename, output_filename)
        self.file_format = file_format
        self.drawing = None

    def process(self) -> None:
        logging.info(f"Producing image file of type {self.file_format}")
        super().process()
        svg_command = SVG(self.config_filename, "")
        svg_command.process()

        ntf = NamedTemporaryFile()
        fname = ntf.name
        ntf.close()
        logging.debug(f"Writing to temp file name {fname}")
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(svg_command.output)
        self.drawing = svg2rlg(fname)
        logging.debug(f"Removing temp file name  {fname}")
        os.unlink(fname)

    def write(self) -> None:
        self.check_directory()
        logging.info(f"Writing output to {self.output_filename}")
        renderPM.drawToFile(self.drawing, self.output_filename, fmt=self.file_format)
