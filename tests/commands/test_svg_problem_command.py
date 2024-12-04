"""TestSvgProblemCommand."""
import unittest
from pathlib import Path

from src.commands.create_board_command import CreateBoardCommand
from src.commands.create_constraints_command import CreateConstraintsCommand
from src.commands.file_reader_command import FileReaderCommand
from src.commands.load_config_command import LoadConfigCommand
from src.commands.svg_problem_command import SVGProblemCommand
from tests.commands.test_svg_command import TestSVGCommand


class TestSVGProblemCommand(TestSVGCommand):
    """Test suite for SVGProblemCommand class."""

    def setUp(self) -> None:
        """Set up the test environment for SVGProblemCommand."""
        super().setUp()
        self.command = SVGProblemCommand()
        self.representation = r"SVGProblemCommand('board', 'constraints', 'svg')"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
