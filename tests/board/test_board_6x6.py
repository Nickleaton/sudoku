"""TestBoard6x6."""
import unittest

from src.board.board import Board
from src.utils.coord import Coord
from src.utils.tags import Tags


class TestBoard6x6(unittest.TestCase):
    """Test suite for the 6x6 Board class."""

    def setUp(self):
        """Set up the 6x6 board and coordinate configurations for testing."""
        tags: Tags = Tags({'Title': 'c', 'Reference': 'start', 'Video': 'finish', 'Author': 'd'})
        self.board = Board(6, 6, 2, 3, tags)
        self.rows = [1, 2, 3, 4, 5, 6]
        self.columns = [1, 2, 3, 4, 5, 6]
        self.bad_rows = [0, 7]
        self.bad_columns = [0, 7]

    @staticmethod
    def get_box_number(row: int, col: int) -> int:
        """Calculate the box number based on the row and column indices."""
        box_row = (row - 1) // 2  # Divide by 2 for rows
        box_col = (col - 1) // 3  # Divide by 3 for columns
        return box_row * 2 + box_col + 1

    def test_construction(self):
        """Test the construction of the 6x6 board."""
        self.assertEqual(6, self.board.board_columns)
        self.assertEqual(6, self.board.board_rows)
        self.assertEqual(3, self.board.box_columns)
        self.assertEqual(2, self.board.box_rows)
        self.assertEqual('start', self.board.tags.Reference)
        self.assertEqual('finish', self.board.tags.Video)
        self.assertEqual('c', self.board.tags.Title)
        self.assertEqual('d', self.board.tags.Author)

    def test_yaml(self):
        """Test the YAML representation of the 6x6 board."""
        yaml_string = (
            "Board:\n"
            "  Board: 6x6\n"
            "  Box: 2x3\n"
            "  Tags:\n"
            "    Title: c\n"
            "    Reference: start\n"
            "    Video: finish\n"
            "    Author: d\n"
        )
        self.assertEqual(yaml_string, self.board.to_yaml())

    def test_high_mid_low(self):
        """Test the high, mid, and low rows of the board."""
        self.assertListEqual(self.board.low, [1, 2])
        self.assertListEqual(self.board.mid, [3, 4])
        self.assertListEqual(self.board.high, [5, 6])

    def test_repr(self):
        """Test the string representation of the 6x6 board."""
        self.assertEqual(
            "Board(6, 6, 2, 3, {'Title': 'c', 'Reference': 'start', 'Video': 'finish', 'Author': 'd'})",
            repr(self.board),
        )

    def test_is_valid(self):
        """Test the validity of coordinates on the 6x6 board."""
        for row in self.rows:
            for column in self.columns:
                self.assertTrue(self.board.is_valid(row, column))
        for row in self.bad_rows:
            for column in self.bad_columns:
                self.assertFalse(self.board.is_valid(row, column))

    def test_is_valid_coord(self):
        """Test the validity of coordinate objects on the 6x6 board."""
        for row in self.rows:
            for column in self.columns:
                self.assertTrue(self.board.is_valid_coordinate(Coord(row, column)))
        for row in self.bad_rows:
            for column in self.bad_columns:
                self.assertFalse(self.board.is_valid_coordinate(Coord(row, column)))

    def test_box_index(self):
        """Test the box index calculation for given coordinates on the 6x6 board."""
        for row in self.rows:
            for column in self.columns:
                self.assertEqual(TestBoard6x6.get_box_number(row, column), self.board.box_index(row, column))

    def test_prime(self):
        """Test the prime number list generated by the 6x6 board."""
        self.assertEqual([2, 3, 5], self.board.primes)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
