"""TestCreateRulesCommand."""
import unittest

from src.commands.create_rules_command import CreateRulesCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestCreateRulesCommand(TestSimpleCommand):
    """Test suite for the CreateRulesCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.command = CreateRulesCommand()
        self.representation = 'CreateRulesCommand()'


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
