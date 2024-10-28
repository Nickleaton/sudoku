import unittest

import pytest

from src.commands.create_board_command import CreateBoardCommand
from src.commands.create_constraints_command import CreateConstraintsCommand
from src.commands.create_linear_program_with_bookkeeping_command import CreateLinearProgramWithBookkeepingCommand
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
        self.command = CreateLinearProgramWithBookkeepingCommand()

    @pytest.mark.skip(reason="Ignore until bookkeeping is implemented properly")
    def test_command(self):
        self.command.execute(self.problem)
        self.assertIsNotNone(self.problem.linear_program)
        print(self.problem.contraints)
        print(type(self.problem.contraints))
        print(self.problem.contraints.bookkeeping_unique())

    @property
    def representation(self) -> str:
        return r"CreateLinearProgramWithBookkeepingCommand('board', 'config', 'constraints', 'solver', 'linear_program')"

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
