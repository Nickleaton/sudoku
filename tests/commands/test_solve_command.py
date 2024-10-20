import unittest

from src.commands.create_linear_program_command import CreateLinearProgramCommand

from src.commands.create_board_command import CreateBoardCommand
from src.commands.create_constraints_command import CreateConstraintsCommand
from src.commands.create_solver_command import CreateSolverCommand
from src.commands.load_config_command import LoadConfigCommand
from src.commands.solve_command import SolveCommand
from src.solvers.pulp_solver import Status
from tests.commands.test_simple_command import TestSimpleCommand


class TestSolveCommand(TestSimpleCommand):

    def setUp(self) -> None:
        super().setUp()
        requirements = LoadConfigCommand(self.path) \
                       | CreateBoardCommand() \
                       | CreateSolverCommand() \
                       | CreateConstraintsCommand() \
                       | CreateLinearProgramCommand()
        requirements.execute(self.problem)
        self.command = SolveCommand()

    def test_command(self):
        self.assertEqual(self.problem.solver.status, Status.NOT_SOLVED)
        self.command.execute(self.problem)
        self.assertEqual(self.problem.solver.status, Status.OPTIMAL)

    @property
    def representation(self) -> str:
        return "SolveCommand('solver', 'solution', 'log')"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
