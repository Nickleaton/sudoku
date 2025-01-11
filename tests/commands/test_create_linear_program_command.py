"""TestCreateLinearProgramCommand."""
import unittest

from src.commands.create_linear_program_command import CreateLinearProgramCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestCreateLinearProgramCommand(TestSimpleCommand):
    """Test suite for the CreateLinearProgramCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.command = CreateLinearProgramCommand()
        self.representation = 'CreateLinearProgramCommand()'


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
