import logging
import os

from reportlab.graphics import renderPM
from svglib.svglib import svg2rlg

from src.commands.simple_command import SimpleCommand
from src.commands.svg_command import SVGCommand


class ProblemPNGCommand(SimpleCommand):

    def __init__(self, config_filename: str, output_filename: str):
        super().__init__(config_filename, output_filename)
        self.tempfilename = "temp.svg"
        if os.path.exists(self.tempfilename):
            os.unlink(self.tempfilename)
        self.svg = SVGCommand(config_filename, self.tempfilename)

    def process(self) -> None:
        super().process()
        self.svg.process()
        self.svg.write()
        assert self.problem is not None

    def write(self) -> None:
        if self.output_filename is None:
            return
        assert self.output_filename is not None
        assert self.output is not None
        self.check_directory()
        logging.info("Producing png file")
        drawing = svg2rlg(self.tempfilename)
        renderPM.drawToFile(drawing, self.output_filename, fmt="PNG")
        logging.info(f"Writing output to {self.output_filename}")
        os.unlink(self.tempfilename)
