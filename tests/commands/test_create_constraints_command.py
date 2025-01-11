"""TestCreateConstraintsCommand."""
import unittest

from src.commands.create_constraints_command import CreateConstraintsCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestCreateConstraintsCommand(TestSimpleCommand):
    """Test suite for the CreateConstraintsCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.command = CreateConstraintsCommand()
        self.representation = "CreateConstraintsCommand()"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
