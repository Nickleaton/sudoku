"""TestImageCommand."""
import unittest

from src.commands.create_board_command import CreateBoardCommand
from src.commands.create_constraints_command import CreateConstraintsCommand
from src.commands.image_command import ImageCommand
from src.commands.load_config_command import LoadConfigCommand
from src.commands.problem import Problem
from src.commands.svg_command import SVGCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestImageCommand(TestSimpleCommand):
    """Test suite for the ImageCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.problem = Problem()
        requirements = LoadConfigCommand(self.path) \
                       | CreateBoardCommand() \
                       | CreateConstraintsCommand() \
                       | SVGCommand('svg')
        requirements.execute(self.problem)
        self.command = ImageCommand("svg", 'test.svg')
        self.representation = "ImageCommand('svg', 'test.svg')"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
