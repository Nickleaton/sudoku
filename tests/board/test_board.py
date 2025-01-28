import unittest

from src.board.board import Board
from src.board.digits import Digits
from src.utils.coord import Coord
from src.utils.cyclic import Cyclic  # Import the Cyclic class
from src.utils.side import Side  # Import the Side class
from src.utils.tags import Tags


class TestBoard(unittest.TestCase):
    """Test suite for the Board class."""

    def setUp(self):
        """Set up the different board configurations for testing."""
        tags: Tags = Tags({'Reference': 'start', 'Video': 'finish', 'Title': 'c', 'Author': 'd'})
        self.board9x9: Board = Board(9, 9, Digits(1, 9), tags=tags)
        self.board4x4: Board = Board(4, 4, Digits(1, 4), tags=tags)
        self.board8x8: Board = Board(8, 8, Digits(1, 8), tags=tags)
        self.board6x6: Board = Board(6, 6, Digits(1, 6), tags=tags)
        # Define the expected map for a 4x4 board
        self.expected_map = {
            # Top row
            (Side.top, Cyclic.clockwise, 0): Coord(1, 1),
            (Side.top, Cyclic.clockwise, 1): Coord(1, 2),
            (Side.top, Cyclic.clockwise, 2): Coord(1, 3),
            (Side.top, Cyclic.clockwise, 3): Coord(1, 4),
            (Side.top, Cyclic.anticlockwise, 0): Coord(1, -1),
            (Side.top, Cyclic.anticlockwise, 1): Coord(1, 0),
            (Side.top, Cyclic.anticlockwise, 2): Coord(1, 1),
            (Side.top, Cyclic.anticlockwise, 3): Coord(1, 2),

            # Bottom row
            (Side.bottom, Cyclic.clockwise, 0): Coord(4, -1),
            (Side.bottom, Cyclic.clockwise, 1): Coord(4, 0),
            (Side.bottom, Cyclic.clockwise, 2): Coord(4, 1),
            (Side.bottom, Cyclic.clockwise, 3): Coord(4, 2),
            (Side.bottom, Cyclic.anticlockwise, 0): Coord(4, 1),
            (Side.bottom, Cyclic.anticlockwise, 1): Coord(4, 2),
            (Side.bottom, Cyclic.anticlockwise, 2): Coord(4, 3),
            (Side.bottom, Cyclic.anticlockwise, 3): Coord(4, 4),

            # Left column
            (Side.left, Cyclic.clockwise, 0): Coord(-1, 1),
            (Side.left, Cyclic.clockwise, 1): Coord(0, 1),
            (Side.left, Cyclic.clockwise, 2): Coord(1, 1),
            (Side.left, Cyclic.clockwise, 3): Coord(2, 1),
            (Side.left, Cyclic.anticlockwise, 0): Coord(1, 1),
            (Side.left, Cyclic.anticlockwise, 1): Coord(2, 1),
            (Side.left, Cyclic.anticlockwise, 2): Coord(3, 1),
            (Side.left, Cyclic.anticlockwise, 3): Coord(4, 1),

            # Right column
            (Side.right, Cyclic.clockwise, 0): Coord(1, 4),
            (Side.right, Cyclic.clockwise, 1): Coord(2, 4),
            (Side.right, Cyclic.clockwise, 2): Coord(3, 4),
            (Side.right, Cyclic.clockwise, 3): Coord(4, 4),
            (Side.right, Cyclic.anticlockwise, 0): Coord(-1, 4),
            (Side.right, Cyclic.anticlockwise, 1): Coord(0, 4),
            (Side.right, Cyclic.anticlockwise, 2): Coord(1, 4),
            (Side.right, Cyclic.anticlockwise, 3): Coord(2, 4),
        }

    def test_side_direction(self):
        for key, expected_coord in self.expected_map.items():
            print(key, expected_coord)
            self.assertEqual(
                self.board4x4.side_cyclic_map[key],
                expected_coord,
                f"Mismatch for {key}: {self.board4x4.side_cyclic_map[key]} != {expected_coord}",
            )
        self.assertNotIn(self.board4x4.side_cyclic_map, (Side.right, Cyclic.clockwise, 8))

    def test_construction_8x8(self):
        """Test the construction of a 8x8 board."""
        self.assertEqual(8, self.board8x8.size.row)
        self.assertEqual(8, self.board8x8.size.column)

    def test_yaml(self):
        """Test the YAML representation of the board."""
        yaml_string = (
            "Board:\n"
            "  Size: 8x8\n"
            "  Digits: 1..8\n"
            "  Tags:\n"
            "    Reference: start\n"
            "    Video: finish\n"
            "    Title: c\n"
            "    Author: d\n"
        )
        self.assertEqual(yaml_string, self.board8x8.to_yaml())

    def test_repr(self):
        """Test the string representation of the board."""
        tag_str: str = "{'Reference': 'start', 'Video': 'finish', 'Title': 'c', 'Author': 'd'}"
        self.assertEqual(f'Board(8, 8, {self.board8x8.digits!r}, {tag_str})', repr(self.board8x8))

    def test_is_valid(self):
        """Test the validity of coordinates on the board."""
        self.assertTrue(self.board4x4.is_valid(1, 1))
        self.assertTrue(self.board4x4.is_valid(1, 4))
        self.assertTrue(self.board4x4.is_valid(4, 1))
        self.assertTrue(self.board4x4.is_valid(4, 4))
        self.assertFalse(self.board4x4.is_valid(0, 1))
        self.assertFalse(self.board4x4.is_valid(1, 0))
        self.assertFalse(self.board4x4.is_valid(9, 1))
        self.assertFalse(self.board4x4.is_valid(1, 9))

    def test_is_valid_coord(self):
        """Test the validity of coordinate objects on the board."""
        self.assertTrue(self.board4x4.is_valid_coordinate(Coord(1, 1)))
        self.assertTrue(self.board4x4.is_valid_coordinate(Coord(1, 4)))
        self.assertTrue(self.board4x4.is_valid_coordinate(Coord(4, 1)))
        self.assertTrue(self.board4x4.is_valid_coordinate(Coord(4, 4)))
        self.assertFalse(self.board4x4.is_valid_coordinate(Coord(0, 1)))
        self.assertFalse(self.board4x4.is_valid_coordinate(Coord(1, 0)))
        self.assertFalse(self.board4x4.is_valid_coordinate(Coord(9, 1)))
        self.assertFalse(self.board4x4.is_valid_coordinate(Coord(1, 9)))

    def test_is_valid_side_index(self):
        """Test the is_valid_side_index method with various coordinates."""
        # Valid cases
        self.assertTrue(self.board9x9.is_valid_side_index(Coord(0, 5)))
        self.assertTrue(self.board9x9.is_valid_side_index(Coord(10, 5)))
        self.assertTrue(self.board9x9.is_valid_side_index(Coord(5, 0)))
        self.assertTrue(self.board9x9.is_valid_side_index(Coord(5, 10)))
        self.assertTrue(self.board9x9.is_valid_side_index(Coord(0, 0)))
        self.assertTrue(self.board9x9.is_valid_side_index(Coord(10, 10)))

        # Invalid cases
        self.assertFalse(self.board9x9.is_valid_side_index(Coord(5, 5)))
        self.assertFalse(self.board9x9.is_valid_side_index(Coord(-1, 5)))
        self.assertFalse(self.board9x9.is_valid_side_index(Coord(11, 5)))
        self.assertFalse(self.board9x9.is_valid_side_index(Coord(5, -1)))
        self.assertFalse(self.board9x9.is_valid_side_index(Coord(5, 11)))

    def test_get_side_coordinate(self):
        """Test the get_side_coordinate method with valid and invalid inputs."""
        # Valid cases
        self.assertEqual(self.board9x9.get_side_coordinate(Side.top, 5), Coord(0, 5))
        self.assertEqual(self.board9x9.get_side_coordinate(Side.bottom, 5), Coord(10, 5))
        self.assertEqual(self.board9x9.get_side_coordinate(Side.left, 5), Coord(5, 0))
        self.assertEqual(self.board9x9.get_side_coordinate(Side.right, 5), Coord(5, 10))

        # Invalid index cases
        with self.assertRaises(ValueError):
            self.board9x9.get_side_coordinate(Side.top, 0)
        with self.assertRaises(ValueError):
            self.board9x9.get_side_coordinate(Side.bottom, 10)
        with self.assertRaises(ValueError):
            self.board9x9.get_side_coordinate(Side.left, 0)
        with self.assertRaises(ValueError):
            self.board9x9.get_side_coordinate(Side.right, 10)

    def test_marker_edge_cases(self):
        """Test marker method with edge cases on the board."""
        board = Board(9, 9, Digits(1, 9))
        self.assertEqual(Coord(0, 0), board.marker(Side.top, 0))
        self.assertEqual(Coord(10, 9), board.marker(Side.bottom, 9))

    def test_start_cell_edge_cases(self):
        """Test start_cell method with edge cases on the board."""
        board = Board(9, 9, Digits(1, 9))
        self.assertEqual(Coord(1, 9), board.start_cell(Side.top, 9))
        self.assertEqual(Coord(9, 1), board.start_cell(Side.bottom, 1))
