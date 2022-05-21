import logging
import os
from tempfile import NamedTemporaryFile

from reportlab.graphics import renderPM
from svglib.svglib import svg2rlg

from src.commands.command import Command
from src.commands.svg_command import SVGCommand


class IMGCommand(Command):

    def __init__(self, output_filename: str, svg: SVGCommand):
        super().__init__(output_filename)
        self.output_filename = output_filename
        self.svg = svg
        self.file_format = self.output_filename.split('.')[-1]
        self.drawing = None

    def process(self) -> None:
        super().process()
        logging.info(f"Producing image file of type {self.file_format}")
        self.svg.process()
        with NamedTemporaryFile() as ntf:
            fname = ntf.name
            ntf.close()

        logging.debug(f"Writing to temp file name {fname}")
        if self.svg.output is not None:
            with open(fname, 'w', encoding='utf-8') as file:
                file.write(self.svg.output)
        else:
            logging.error("Expecting output but it is empty")  # pragma: no cover
        self.drawing = svg2rlg(fname)
        logging.debug(f"Removing temp file name  {fname}")
        os.unlink(fname)

    def write(self) -> None:
        super().write()
        self.check_directory()
        renderPM.drawToFile(self.drawing, self.output_filename, fmt=self.file_format)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.output_filename}', {repr(self.svg)})"
