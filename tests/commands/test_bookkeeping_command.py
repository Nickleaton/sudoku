import unittest

from src.commands.bookkeeping_command import BookkeepingCommand
from src.commands.create_board_command import CreateBoardCommand
from src.commands.create_constraints_command import CreateConstraintsCommand
from src.commands.create_solver_command import CreateSolverCommand
from src.commands.load_config_command import LoadConfigCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestLinearProgramWithBookkeepingCommand(TestSimpleCommand):

    def setUp(self) -> None:
        super().setUp()
        requirements = LoadConfigCommand(self.path) \
                       | CreateBoardCommand() \
                       | CreateSolverCommand() \
                       | CreateConstraintsCommand()
        requirements.execute(self.problem)
        self.command = BookkeepingCommand()

    def test_command(self):
        self.command.execute(self.problem)
        self.assertIn("bookkeeping_unique", self.problem)
        self.assertTrue(self.problem["bookkeeping_unique"])

    @property
    def representation(self) -> str:
        return r"BookkeepingCommand('constraints', 'bookkeeping_unique')"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
