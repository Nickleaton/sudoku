"""TestValidateConfigCommand."""
import unittest

from src.commands.problem import Problem
from src.commands.validate_config_command import ValidateConfigCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestValidateConfigCommand(TestSimpleCommand):
    """Test suite for ValidateConfigCommand class."""

    def setUp(self) -> None:
        """Set up the test environment for ValidateConfigCommand.

        This method sets up the problem and prepares the command to be tested.
        """
        super().setUp()
        self.command = ValidateConfigCommand(self.path)
        self.problem = Problem()

    @property
    def representation(self) -> str:
        """Return the string representation of ValidateConfigCommand.

        Returns:
            str: The representation of the ValidateConfigCommand instance.
        """
        return r"ValidateConfigCommand('problems\\easy\\problem001.yaml', 'config_validation')"

    def test_repr(self):
        """Test the __repr__ method of ValidateConfigCommand.

        This method checks if the string representation matches the expected value.
        """
        self.assertEqual(self.representation, repr(self.command))

    def test_execute(self):
        """Test the execute method of ValidateConfigCommand.

        This method executes the command and prints the result of the config validation.
        """
        self.command.execute(self.problem)
        print(self.problem.config_validation)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
