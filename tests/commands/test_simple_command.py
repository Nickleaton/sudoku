"""TestSimpleCommand."""
import unittest

from src.commands.simple_command import SimpleCommand
from tests.commands.test_command import TestCommand


class TestSimpleCommand(TestCommand):
    """Test suite for SimpleCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.command = SimpleCommand()
        self.representation = "SimpleCommand()"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
