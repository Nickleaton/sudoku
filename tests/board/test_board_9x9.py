"""TestBoard9x9."""
import unittest

from src.board.board import Board
from src.board.digits import Digits
from src.utils.coord import Coord
from src.utils.tags import Tags


class TestBoard9x9(unittest.TestCase):
    """Test suite for the 9x9 Board class."""

    def setUp(self):
        """Set up the 9x9 board and coordinate configurations for testing."""
        tags: Tags = Tags({'Title': 'c', 'Reference': 'start', 'Video': 'finish', 'Author': 'd'})
        self.board = Board(Coord(9, 9), Digits(1, 9), tags=tags)
        self.rows = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.columns = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.bad_rows = [0, 10]
        self.bad_columns = [0, 10]

    def test_construction(self):
        """Test the construction of the 9x9 board."""
        self.assertEqual(9, self.board.size.row)
        self.assertEqual(9, self.board.size.column)
        self.assertEqual('start', self.board.tags.Reference)
        self.assertEqual('finish', self.board.tags.Video)
        self.assertEqual('c', self.board.tags.Title)
        self.assertEqual('d', self.board.tags.Author)

    def test_yaml(self):
        """Test the YAML representation of the 9x9 board."""
        yaml_string = (
            "Board:\n"
            "  Size: 9x9\n"
            "  Digits: 1..9\n"
            "  Tags:\n"
            "    Title: c\n"
            "    Reference: start\n"
            "    Video: finish\n"
            "    Author: d\n"
        )
        self.assertEqual(yaml_string, self.board.to_yaml())

    def test_repr(self):
        """Test the string representation of the 9x9 board."""
        target = (
            "Board("
            "Coord(9, 9), "
            "Digits(1, 9), "
            "Tags({'Title': 'c', 'Reference': 'start', 'Video': 'finish', 'Author': 'd'})"
            ")"
        )
        self.assertEqual(target, repr(self.board))

    def test_is_valid(self):
        """Test the validity of coordinates on the 9x9 board."""
        for row in self.rows:
            for column in self.columns:
                self.assertTrue(self.board.is_valid(row, column))
        for row in self.bad_rows:
            for column in self.bad_columns:
                self.assertFalse(self.board.is_valid(row, column))

    def test_is_valid_coord(self):
        """Test the validity of coordinate objects on the 9x9 board."""
        for row in self.rows:
            for column in self.columns:
                self.assertTrue(self.board.is_valid_coordinate(Coord(row, column)))
        for row in self.bad_rows:
            for column in self.bad_columns:
                self.assertFalse(self.board.is_valid_coordinate(Coord(row, column)))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
