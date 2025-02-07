"""TestBoard6x6."""
import unittest

from src.board.board import Board
from src.board.digits import Digits
from src.utils.coord import Coord
from src.utils.tags import Tags


class TestBoard6x6(unittest.TestCase):
    """Test suite for the 6x6 Board class."""

    def setUp(self):
        """Set up the 6x6 board and coordinate configurations for testing."""
        tags: Tags = Tags({'Title': 'c', 'Reference': 'start', 'Video': 'finish', 'Author': 'd'})
        self.board = Board(Coord(6, 6), Digits(1, 6), tags)
        self.rows = [1, 2, 3, 4, 5, 6]
        self.columns = [1, 2, 3, 4, 5, 6]
        self.bad_rows = [0, 7]
        self.bad_columns = [0, 7]

    def test_construction(self):
        """Test the construction of the 6x6 board."""
        self.assertEqual(6, self.board.size.row)
        self.assertEqual(6, self.board.size.column)
        self.assertEqual('start', self.board.tags.Reference)
        self.assertEqual('finish', self.board.tags.Video)
        self.assertEqual('c', self.board.tags.Title)
        self.assertEqual('d', self.board.tags.Author)

    def test_yaml(self):
        """Test the YAML representation of the 6x6 board."""
        yaml_string = (
            "Board:\n"
            "  Size: 6x6\n"
            "  Digits: 1..6\n"
            "  Tags:\n"
            "    Title: c\n"
            "    Reference: start\n"
            "    Video: finish\n"
            "    Author: d\n"
        )
        self.assertEqual(yaml_string, self.board.to_yaml())

    def test_repr(self):
        """Test the string representation of the 6x6 board."""
        target = (
            "Board("
            "Coord(6, 6), "
            "Digits(1, 6), "
            "Tags({'Title': 'c', 'Reference': 'start', 'Video': 'finish', 'Author': 'd'})"
            ")"
        )
        self.assertEqual(target, repr(self.board))

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


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
