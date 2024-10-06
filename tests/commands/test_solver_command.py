import unittest

from src.commands.create_board_command import CreateBoardCommand
from src.commands.create_constraints_command import CreateConstraintsCommand
from src.commands.create_lp_command import CreateLPCommand
from src.commands.load_config_command import LoadConfigCommand
from src.commands.solver_command import SolverCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestSolverCommand(TestSimpleCommand):

    def setUp(self) -> None:
        super().setUp()
        load_config = LoadConfigCommand(self.path)
        create_board = CreateBoardCommand()
        create_constraints = CreateConstraintsCommand()
        create_lp = CreateLPCommand()
        load_config.execute(self.problem)
        create_board.execute(self.problem)
        create_constraints.execute(self.problem)
        create_lp.execute(self.problem)
        self.command = SolverCommand()

    @property
    def representation(self) -> str:
        return r"SolverCommand()"

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
