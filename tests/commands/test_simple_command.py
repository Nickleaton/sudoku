"""TestSimpleCommand."""
import unittest
from pathlib import Path

from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from tests.commands.test_command import TestCommand


class TestSimpleCommand(TestCommand):
    """Test suite for SimpleCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.command = SimpleCommand()
        self.problem = Problem()
        self.empty_problem = Problem()
        self.path = Path('problems\\easy\\problem001.yaml')

    def test_command(self):
        """Test the execution of the SimpleCommand."""
        if self.command is None:
            return
        self.command.execute(self.problem)
        name = self.__class__.__name__.replace("Test", "").replace("Command", "")
        self.assertEqual(self.command.name, name)

    @property
    def representation(self) -> str:
        """Return a string representation of the SimpleCommand."""
        return f"{self.command.__class__.__name__}()"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
