"""TestValidateConfigCommand."""
import unittest

from src.commands.validate_config_command import ValidateConfigCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestValidateConfigCommand(TestSimpleCommand):
    """Test suite for ValidateConfigCommand class."""

    def setUp(self) -> None:
        """Set up the test environment for ValidateConfigCommand.

        This method sets up the problem and prepares the command to be tested.
        """
        super().setUp()
        self.command = ValidateConfigCommand()
        self.representation = 'ValidateConfigCommand()'


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
