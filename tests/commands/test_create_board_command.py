"""TestCreateBoardCommand."""
import unittest

from src.commands.create_board_command import CreateBoardCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestCreateBoardCommand(TestSimpleCommand):
    """Test suite for the CreateBoardCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.command = CreateBoardCommand()
        self.representation = 'CreateBoardCommand()'


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
