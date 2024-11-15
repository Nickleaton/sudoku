"""TestBookkeepingCommand."""
import unittest

from src.commands.bookkeeping_command import BookkeepingCommand
from src.commands.create_board_command import CreateBoardCommand
from src.commands.create_constraints_command import CreateConstraintsCommand
from src.commands.create_solver_command import CreateSolverCommand
from src.commands.load_config_command import LoadConfigCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestLinearProgramWithBookkeepingCommand(TestSimpleCommand):
    """Test suite for the BookkeepingCommand."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        requirements = LoadConfigCommand(self.path) \
                       | CreateBoardCommand() \
                       | CreateSolverCommand() \
                       | CreateConstraintsCommand()
        requirements.execute(self.problem)
        self.command = BookkeepingCommand()

    def test_command(self):
        """Test the execution of the BookkeepingCommand."""
        self.command.execute(self.problem)
        self.assertIn("bookkeeping_unique", self.problem)
        self.assertIsNotNone(self.problem["bookkeeping_unique"])
        # TODO: Check that the bookkeeping is unique

    @property
    def representation(self) -> str:
        """Return the string representation of the command."""
        return r"BookkeepingCommand('constraints', 'bookkeeping_unique')"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
