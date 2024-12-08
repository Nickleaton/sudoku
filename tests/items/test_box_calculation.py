"""TestBoxCalculation."""
import unittest
from typing import List

from src.board.board import Board
from src.items.box import Box


class TestBoxCalculation(unittest.TestCase):
    """Test suite for box calculations in a Board."""

    def check(self, n: int, width: int, height: int, expected: List) -> None:
        """Check the start row and column of each box."""
        problem = Board(n, n, width, height)
        for i, row, column in expected:
            box = Box(problem, i)
            row_start = box.start().row
            column_start = box.start().column
            self.assertEqual(row, row_start)
            self.assertEqual(column, column_start)

    def test_9_9_3_3(self):
        """Test box calculations for a 9x9 grid with 3x3 sub-grids."""
        expected = [
            [1, 1, 1],
            [2, 4, 1],
            [3, 7, 1],
            [4, 1, 4],
            [5, 4, 4],
            [6, 7, 4],
            [7, 1, 7],
            [8, 4, 7],
            [9, 7, 7]
        ]
        self.check(9, 3, 3, expected)

    def test_8_8_2_4(self):
        """Test box calculations for an 8x8 grid with 2x4 sub-grids."""
        expected = [
            [1, 1, 1],
            [2, 3, 1],
            [3, 5, 1],
            [4, 7, 1],
            [5, 1, 5],
            [6, 3, 5],
            [7, 5, 5],
            [8, 7, 5]
        ]
        self.check(8, 2, 4, expected)

    def test_8_8_4_2(self):
        """Test box calculations for an 8x8 grid with 4x2 sub-grids."""
        expected = [
            [1, 1, 1],
            [2, 5, 1],
            [3, 1, 3],
            [4, 5, 3],
            [5, 1, 5],
            [6, 5, 5],
            [7, 1, 7],
            [8, 5, 7]
        ]
        self.check(8, 4, 2, expected)

    def test_6_6_2_3(self):
        """Test box calculations for a 6x6 grid with 2x3 sub-grids."""
        expected = [
            [1, 1, 1],
            [2, 3, 1],
            [3, 5, 1],
            [4, 1, 4],
            [5, 3, 4],
            [6, 5, 4]
        ]
        self.check(6, 2, 3, expected)

    def test_6_6_3_2(self):
        """Test box calculations for a 6x6 grid with 3x2 sub-grids."""
        expected = [
            [1, 1, 1],
            [2, 4, 1],
            [3, 1, 3],
            [4, 4, 3],
            [5, 1, 5],
            [6, 4, 5]
        ]
        self.check(6, 3, 2, expected)

    def test_4_4_2_2(self):
        """Test box calculations for a 4x4 grid with 2x2 sub-grids."""
        expected = [
            [1, 1, 1],
            [2, 3, 1],
            [3, 1, 3],
            [4, 3, 3]
        ]
        self.check(4, 2, 2, expected)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
