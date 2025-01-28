"""TestBookkeepingCommand."""
import unittest

from postponed.src.commands.bookkeeping_command import BookkeepingCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestBookkeepingCommand(TestSimpleCommand):
    """Test suite for the BookkeepingCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.command = BookkeepingCommand()
        self.representation = r"BookkeepingCommand()"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
