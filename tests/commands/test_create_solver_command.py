import unittest

from src.commands.create_board_command import CreateBoardCommand
from src.commands.create_constraints_command import CreateConstraintsCommand
from src.commands.create_solver_command import CreateSolverCommand
from src.commands.load_config_command import LoadConfigCommand
from tests.commands.test_command import TestCommand


class TestCreateSolverCommand(TestCommand):

    def setUp(self) -> None:
        super().setUp()
        requirements = LoadConfigCommand(self.path) \
                       | CreateBoardCommand() \
                       | CreateConstraintsCommand()
        requirements.execute(self.problem)
        self.command = CreateSolverCommand()

    def test_command(self):
        self.command.execute(self.problem)
        self.assertIsNotNone(self.problem.solver)

    @property
    def representation(self) -> str:
        return "CreateSolverCommand('config', 'board', 'solver')"

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
