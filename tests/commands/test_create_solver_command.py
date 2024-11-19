"""TestCreateSolverCommand."""
import unittest

from src.commands.create_board_command import CreateBoardCommand
from src.commands.create_constraints_command import CreateConstraintsCommand
from src.commands.create_solver_command import CreateSolverCommand
from src.commands.load_config_command import LoadConfigCommand
from tests.commands.test_command import TestCommand


class TestCreateSolverCommand(TestCommand):
    """Test suite for the CreateSolverCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.prerequisites = LoadConfigCommand(self.path) \
                       | CreateBoardCommand() \
                       | CreateConstraintsCommand()
        self.prerequisites.execute(self.problem)
        self.command = CreateSolverCommand()
        self.requirements = ['config', 'board']
        self.target = "solver"

    def test_command(self):
        """Test the execute method of CreateSolverCommand."""
        self.command.execute(self.problem)
        self.assertIsNotNone(self.problem.solver)

    @property
    def representation(self) -> str:
        """Return the string representation of the CreateSolverCommand."""
        return "CreateSolverCommand('config', 'board', 'solver')"

    def test_repr(self):
        """Test the string representation of the command."""
        self.assertEqual(self.representation, repr(self.command))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
