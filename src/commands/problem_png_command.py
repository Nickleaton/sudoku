import logging
import os
from pathlib import Path

from reportlab.graphics import renderPM
from svglib.svglib import svg2rlg

from src.commands.simple_command import SimpleCommand
from src.commands.svg_command import SVGCommand


class ProblemPNGCommand(SimpleCommand):

    def __init__(self, config_filename: Path, output_filename: Path):
        super().__init__(config_filename, output_filename)
        self.temp_filename = Path("temp.svg")
        if self.temp_filename.exists():
            self.temp_filename.unlink()
        if not self.temp_filename.parent.exists():
            self.temp_filename.parent.mkdir()
        self.svg = SVGCommand(config_filename, self.temp_filename)

    def execute(self) -> None:
        super().execute()
        self.svg.execute()
        self.svg.write()
        assert self.problem is not None

    def write(self) -> None:
        if self.output_filename is None:
            return
        assert self.output_filename is not None
        assert self.output is not None
        self.check_directory()
        logging.info("Producing png file")
        drawing = svg2rlg(self.temp_filename)
        renderPM.drawToFile(drawing, self.output_filename, fmt="PNG")
        logging.info(f"Writing output to {self.output_filename}")
        os.unlink(self.temp_filename)
