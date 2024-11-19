"""TestCreateLinearProgramCommand."""
import unittest

from src.commands.create_board_command import CreateBoardCommand
from src.commands.create_constraints_command import CreateConstraintsCommand
from src.commands.create_linear_program_command import CreateLinearProgramCommand
from src.commands.create_solver_command import CreateSolverCommand
from src.commands.load_config_command import LoadConfigCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestCreateLinearProgramCommand(TestSimpleCommand):
    """Test suite for the CreateLinearProgramCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.prerequisites = LoadConfigCommand(self.path) \
                       | CreateBoardCommand() \
                       | CreateSolverCommand() \
                       | CreateConstraintsCommand()
        self.prerequisites.execute(self.problem)
        self.command = CreateLinearProgramCommand()
        self.requirements = ['board', 'config', 'constraints', 'solver']
        self.target = "linear_program"

    def test_command(self):
        """Test the execute method of the CreateLinearProgramCommand."""
        self.command.execute(self.problem)
        self.assertIsNotNone(self.problem.linear_program)

    @property
    def representation(self) -> str:
        """Return the string representation of the CreateLinearProgramCommand."""
        return "CreateLinearProgramCommand('board', 'config', 'constraints', 'solver', 'linear_program')"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
