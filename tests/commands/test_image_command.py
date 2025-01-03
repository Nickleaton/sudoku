"""TestImageCommand."""
import unittest
from pathlib import Path

from src.commands.create_board_command import CreateBoardCommand
from src.commands.create_constraints_command import CreateConstraintsCommand
from src.commands.file_reader_command import FileReaderCommand
from src.commands.image_command import ImageCommand, ImageFormat
from src.commands.load_config_command import LoadConfigCommand
from src.commands.svg_command import SVGCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestImageCommand(TestSimpleCommand):
    """Test suite for the ImageCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.prerequisites = FileReaderCommand(file_name='config_file_name',
                                               target='config_text',
                                               file_path=Path('problems\\easy\\problem001.yaml')) \
                             | LoadConfigCommand() \
                             | CreateBoardCommand() \
                             | CreateConstraintsCommand() \
                             | SVGCommand()
        self.prerequisites.execute(self.problem)
        self.command = ImageCommand(image_format_name="format",
                                    image_format=ImageFormat.SVG,
                                    source="svg",
                                    target="svg_text")
        self.representation = "ImageCommand('format', 'ImageFormat.SVG', 'svg', 'svg_text')"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
