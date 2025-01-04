import unittest

from src.board.board import Board
from src.utils.coord import Coord
from src.utils.cyclic import Cyclic  # Import the Cyclic class
from src.utils.side import Side  # Import the Side class


class TestBoard(unittest.TestCase):
    """Test suite for the Board class."""

    def setUp(self):
        """Set up the different board configurations for testing."""
        tags: dict[str, str] = {'Reference': 'start', 'Video': 'finish', 'Title': 'c', 'Author': 'd'}
        self.board9x9_no_boxes: Board = Board(9, 9, 0, 0, tags=tags)
        self.board9x9: Board = Board(9, 9, 3, 3, tags=tags)
        self.board4x4: Board = Board(4, 4, tags=tags)
        self.board8x8: Board = Board(8, 8, 2, 4, tags=tags)
        self.board6x6: Board = Board(6, 6, 2, 3, tags=tags)
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
        self.assertEqual(8, self.board8x8.board_columns)
        self.assertEqual(8, self.board8x8.board_rows)
        self.assertEqual(4, self.board8x8.box_columns)
        self.assertEqual(2, self.board8x8.box_rows)

    def test_yaml(self):
        """Test the YAML representation of the board."""
        yaml_string = (
            "Board:\n"
            "  Board: 8x8\n"
            "  Box: 2x4\n"
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
        self.assertEqual(f'Board(8, 8, 2, 4, {tag_str})', repr(self.board8x8))

    def test_no_boxes(self):
        """Test the board with no boxes configuration (9x9)."""
        self.assertEqual(9, self.board9x9_no_boxes.board_columns)
        self.assertEqual(9, self.board9x9_no_boxes.board_rows)
        self.assertEqual(0, self.board9x9_no_boxes.box_columns)
        self.assertEqual(0, self.board9x9_no_boxes.box_rows)

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
        self.assertTrue(self.board9x9_no_boxes.is_valid_side_index(Coord(0, 5)))
        self.assertTrue(self.board9x9_no_boxes.is_valid_side_index(Coord(10, 5)))
        self.assertTrue(self.board9x9_no_boxes.is_valid_side_index(Coord(5, 0)))
        self.assertTrue(self.board9x9_no_boxes.is_valid_side_index(Coord(5, 10)))
        self.assertTrue(self.board9x9_no_boxes.is_valid_side_index(Coord(0, 0)))
        self.assertTrue(self.board9x9_no_boxes.is_valid_side_index(Coord(10, 10)))

        # Invalid cases
        self.assertFalse(self.board9x9_no_boxes.is_valid_side_index(Coord(5, 5)))
        self.assertFalse(self.board9x9_no_boxes.is_valid_side_index(Coord(-1, 5)))
        self.assertFalse(self.board9x9_no_boxes.is_valid_side_index(Coord(11, 5)))
        self.assertFalse(self.board9x9_no_boxes.is_valid_side_index(Coord(5, -1)))
        self.assertFalse(self.board9x9_no_boxes.is_valid_side_index(Coord(5, 11)))

    def test_get_side_coordinate(self):
        """Test the get_side_coordinate method with valid and invalid inputs."""
        # Valid cases
        self.assertEqual(self.board9x9_no_boxes.get_side_coordinate(Side.top, 5), Coord(0, 5))
        self.assertEqual(self.board9x9_no_boxes.get_side_coordinate(Side.bottom, 5), Coord(10, 5))
        self.assertEqual(self.board9x9_no_boxes.get_side_coordinate(Side.left, 5), Coord(5, 0))
        self.assertEqual(self.board9x9_no_boxes.get_side_coordinate(Side.right, 5), Coord(5, 10))

        # Invalid index cases
        with self.assertRaises(ValueError):
            self.board9x9_no_boxes.get_side_coordinate(Side.top, 0)
        with self.assertRaises(ValueError):
            self.board9x9_no_boxes.get_side_coordinate(Side.bottom, 10)
        with self.assertRaises(ValueError):
            self.board9x9_no_boxes.get_side_coordinate(Side.left, 0)
        with self.assertRaises(ValueError):
            self.board9x9_no_boxes.get_side_coordinate(Side.right, 10)

    def test_marker_edge_cases(self):
        """Test marker method with edge cases on the board."""
        board = Board(9, 9)
        self.assertEqual(Coord(0, 0), board.marker(Side.top, 0))
        self.assertEqual(Coord(10, 9), board.marker(Side.bottom, 9))

    def test_start_cell_edge_cases(self):
        """Test start_cell method with edge cases on the board."""
        board = Board(9, 9)
        self.assertEqual(Coord(1, 9), board.start_cell(Side.top, 9))
        self.assertEqual(Coord(9, 1), board.start_cell(Side.bottom, 1))

    # def test_start_cell_with_cyclic(self):
    #     board = Board(9, 9)
    #     test_cases: list[tuple[Side, Cyclic, int, Coord]] = [
    #         (Side.top, Cyclic.clockwise, 5, Coord(1, 6)),
    #         (Side.top, Cyclic.anticlockwise, 5, Coord(1, 4)),
    #         (Side.right, Cyclic.clockwise, 5, Coord(6, 9)),
    #         (Side.right, Cyclic.anticlockwise, 5, Coord(4, 9)),
    #         (Side.bottom, Cyclic.clockwise, 5, Coord(9, 4)),
    #         (Side.bottom, Cyclic.anticlockwise, 5, Coord(9, 6)),
    #         (Side.left, Cyclic.anticlockwise, 5, Coord(6, 1)),
    #         (Side.left, Cyclic.clockwise, 5, Coord(4, 1)),
    #     ]
    #     # Iterate through test cases
    #     for side, cyclic, index, expected in test_cases:
    #         with self.subTest(side=side, cyclic=cyclic, index=index):
    #             self.assertEqual(expected, board.start_cell_with_cyclic(side, cyclic, index))
