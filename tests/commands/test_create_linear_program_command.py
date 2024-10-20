import unittest

from src.commands.create_board_command import CreateBoardCommand
from src.commands.create_constraints_command import CreateConstraintsCommand
from src.commands.create_linear_program_command import CreateLinearProgramCommand
from src.commands.create_solver_command import CreateSolverCommand
from src.commands.load_config_command import LoadConfigCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestCreateLinearProgramCommand(TestSimpleCommand):

    def setUp(self) -> None:
        super().setUp()
        requirements = LoadConfigCommand(self.path) \
                       | CreateBoardCommand() \
                       | CreateSolverCommand() \
                       | CreateConstraintsCommand()
        requirements.execute(self.problem)
        self.command = CreateLinearProgramCommand()

    def test_command(self):
        self.command.execute(self.problem)
        self.assertIsNotNone(self.problem.linear_program)

    @property
    def representation(self) -> str:
        return "CreateLinearProgramCommand('board', 'config', 'constraints', 'solver', 'linear_program')"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
