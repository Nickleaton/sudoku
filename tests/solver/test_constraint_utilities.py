import unittest

from src.items.board import Board
from src.items.cell import Cell
from src.solvers.constraint_utilities import ConstraintUtilities
from src.solvers.pulp_solver import PulpSolver


class TestConstraintUtilities(unittest.TestCase):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3)
        self.solver = PulpSolver(self.board, "TestConstraintUtilities")

    def test_logical_log10_cell(self) -> None:
        c1 = Cell.make(self.board, 1, 1)
        rule = ConstraintUtilities.log10_cell(self.solver, c1)
        self.assertEqual('Log10_1_1', str(rule))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
