import unittest

from src.board.board import Board
from src.board.digits import Digits
from src.items.cell import Cell
from src.solvers.constraint_utilities import ConstraintUtilities
from src.solvers.solver import Solver
from src.utils.coord import Coord
from src.utils.tags import Tags


class TestConstraintUtilities(unittest.TestCase):
    """Test the ConstraintUtilities class and its methods."""

    def setUp(self) -> None:
        """Set up the test environment."""
        self.board: Board = Board(Coord(9, 9), Digits(1, 9), tags=Tags())
        self.solver = Solver(self.board, "TestConstraintUtilities")
        ConstraintUtilities.variables.clear()

    def test_logical_log10_cell(self) -> None:
        """Test the log10_cell method of the ConstraintUtilities class."""
        c1 = Cell.make(self.board, 1, 1)
        rule = ConstraintUtilities.log10_cell(self.solver, c1)

        # Check the variable name explicitly
        self.assertEqual(rule.name, 'log10_1_1')

        # Ensure constraint is added to the solver model
        self.assertIn('log10_1_1', {c.name for c in self.solver.model.constraints.values()})

        # Check that calling log10_cell again returns the same variable
        rule2 = ConstraintUtilities.log10_cell(self.solver, c1)
        self.assertIs(rule, rule2)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
