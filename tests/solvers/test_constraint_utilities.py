"""Test ConstraintUtilities class for logical operations."""
import unittest

from src.board.board import Board
from src.items.cell import Cell
from src.solvers.constraint_utilities import ConstraintUtilities
from src.solvers.pulp_solver import PulpSolver


class TestConstraintUtilities(unittest.TestCase):
    """Test the ConstraintUtilities class and its methods."""

    def setUp(self) -> None:
        """Set up the test environment."""
        # Initialize the board and solver for tests
        self.board = Board(9, 9, 3, 3)
        self.solver = PulpSolver(self.board, "TestConstraintUtilities")

    def test_logical_log10_cell(self) -> None:
        """Test the log10_cell method of the ConstraintUtilities class."""
        # Create start cell and apply the log10_cell method
        c1 = Cell.make(self.board, 1, 1)
        rule = ConstraintUtilities.log10_cell(self.solver, c1)
        self.assertEqual('log10_1_1', str(rule))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
