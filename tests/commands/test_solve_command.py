import unittest

from src.commands.create_board_command import CreateBoardCommand
from src.commands.create_constraints_command import CreateConstraintsCommand
from src.commands.create_lp_command import CreateLPCommand
from src.commands.load_config_command import LoadConfigCommand
from src.commands.solve_command import SolveCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestSolveCommand(TestSimpleCommand):

    def setUp(self) -> None:
        super().setUp()
        requirements =  LoadConfigCommand(self.path) \
            | CreateBoardCommand() \
            | CreateConstraintsCommand() \
            | CreateLPCommand()
        requirements.execute(self.problem)
        self.command = SolveCommand()

    @property
    def representation(self) -> str:
        return "SolveCommand('solver', 'solution', 'log')"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
