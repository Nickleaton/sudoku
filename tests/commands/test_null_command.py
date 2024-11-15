"""TestNullCommand."""
import unittest

from src.commands.null_command import NullCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestNullCommand(TestSimpleCommand):
    """Test suite for the NullCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.command = NullCommand()


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
