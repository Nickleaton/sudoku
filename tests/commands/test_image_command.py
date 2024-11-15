"""TestImageCommand."""
import unittest
from pathlib import Path

from src.commands.create_board_command import CreateBoardCommand
from src.commands.create_constraints_command import CreateConstraintsCommand
from src.commands.image_command import ImageCommand, ImageFormat
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
        self.command = ImageCommand("svg", Path('test.svg'))

    @property
    def representation(self) -> str:
        """Return the string representation of the ImageCommand."""
        return "ImageCommand('svg', WindowsPath('test.svg'))"

    def test_execute(self):
        """Test the execute method of ImageCommand."""
        self.assertIsNotNone(self.problem.svg)
        if self.command.target.exists():
            self.command.target.unlink(missing_ok=True)
        self.command.execute(self.problem)
        self.assertTrue(self.command.target.exists())

    def xtest_formats(self):
        """Test different image formats."""
        for fmt in ImageFormat:
            self.command.image_format = fmt
            self.command.target = Path(f"test.{fmt.name.lower()}")
            print(self.command.target)
            if self.command.target.exists():
                self.command.target.unlink(missing_ok=True)
            self.command.execute(self.problem)
            self.assertTrue(self.command.target.exists())
            if self.command.target.exists():
                self.command.target.unlink(missing_ok=True)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
