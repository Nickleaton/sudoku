"""Test ConstraintUtilities class for logical operations."""
import unittest

from src.board.board import Board
from src.items.cell import Cell
from src.solvers.constraint_utilities import ConstraintUtilities
from src.solvers.solver import Solver
from src.utils.tags import Tags


class TestConstraintUtilities(unittest.TestCase):
    """Test the ConstraintUtilities class and its methods."""

    def setUp(self) -> None:
        """Set up the test environment."""
        # Initialize the board and solver for tests
        tags: Tags = Tags({'Reference': 'start', 'Video': 'finish', 'Title': 'c', 'Author': 'd'})
        self.board: Board = Board(9, 9, tags=tags)
        self.solver = Solver(self.board, "TestConstraintUtilities")

    def test_logical_log10_cell(self) -> None:
        """Test the log10_cell method of the ConstraintUtilities class."""
        # Create start cell and apply the log10_cell method
        c1 = Cell.make(self.board, 1, 1)
        rule = ConstraintUtilities.log10_cell(self.solver, c1)
        self.assertEqual('log10_1_1', str(rule))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
