"""TestCreateLinearProgramWithBookkeepingCommand."""
import unittest

from src.commands.create_linear_program_with_bookkeeping_command import CreateLinearProgramWithBookkeepingCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestCreateLinearProgramWithBookkeepingCommand(TestSimpleCommand):
    """Test suite for the CreateLinearProgramWithBookkeepingCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.command = CreateLinearProgramWithBookkeepingCommand()
        self.representation = 'CreateLinearProgramWithBookkeepingCommand()'


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
