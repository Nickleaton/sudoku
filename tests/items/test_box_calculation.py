import itertools
import unittest

from src.board.board import Board
from src.board.digits import Digits
from src.items.boxes import Boxes
from src.utils.coord import Coord
from src.utils.tags import Tags


class TestBoardCalculations(unittest.TestCase):
    """Base class for board-related calculations."""

    def setUp(self):
        """Set up the board and boxes."""
        self.board_size = Coord(4, 4)  # Default to 4x4 board
        self.digits = Digits(1, 4)
        self.box_size = Coord(2, 2)
        self.expected_box_indices = None
        self.expected_top_lefts = None
        self.bad_indices = None
        self.bad_row_columns = None

    def test_expected_box_indices(self):
        """Test that all cells are covered, and box indices are correctly calculated."""
        if self.expected_box_indices is None:
            return

        board = Board(self.board_size, self.digits, Tags())
        boxes = Boxes(board, self.box_size)

        # Generate all combinations of (row, col) using itertools.product
        for row, col in itertools.product(board.row_range, board.column_range):
            expected_index = int(self.expected_box_indices[row - 1][col - 1])
            self.assertEqual(
                boxes.box_index(row, col),
                expected_index,
                f"Cell ({row}, {col}) returned incorrect box index",
            )

    def test_boxes_first(self):
        """Test the `first` method to ensure top-left coordinates are correct."""
        if self.expected_top_lefts is None:
            return
        board = Board(self.board_size, self.digits, Tags())
        boxes = Boxes(board, self.box_size)
        for box_index, expected_coord_str in enumerate(self.expected_top_lefts, start=1):
            row, col = map(int, expected_coord_str)
            expected_coord = Coord(row, col)
            actual_coord = boxes.first(box_index)
            self.assertEqual(
                actual_coord,
                expected_coord,
                f"Box {box_index} returned incorrect top-left coordinate: expected {expected_coord}, got {boxes.first(box_index)}",
            )

    def test_bad_indices(self):
        """Test that `first` raises an IndexError for out-of-bounds box indices."""
        if self.bad_indices is None:
            return
        board = Board(self.board_size, self.digits, Tags())
        boxes = Boxes(board, self.box_size)

        for bad_index in self.bad_indices:
            with self.assertRaises(IndexError):
                boxes.first(bad_index)

    def test_bad_row_columns(self):
        """Test that `box_index` raises an IndexError for out-of-bounds row/column pairs."""
        if self.bad_row_columns is None:
            return
        board = Board(self.board_size, self.digits, Tags())
        boxes = Boxes(board, self.box_size)

        for bad_rc in self.bad_row_columns:
            row, col = map(int, list(bad_rc))  # Convert the string 'xy' to row=x, col=y
            with self.assertRaises(IndexError):
                boxes.box_index(row, col)


class Test4x4BoardCalculations(TestBoardCalculations):
    """Tests specific to the 4x4 board with 2x2 boxes."""

    def setUp(self):
        """Set up the 4x4 board with 2x2 boxes and expected values."""
        super().setUp()
        self.board_size = Coord(4, 4)
        self.box_size = Coord(2, 2)

        self.expected_box_indices = [
            '1122',  # Row 1
            '1122',  # Row 2
            '3344',  # Row 3
            '3344',  # Row 4
        ]
        self.expected_top_lefts = [
            '11',  # Box 1 -> (1, 1)
            '13',  # Box 2 -> (1, 3)
            '31',  # Box 3 -> (3, 1)
            '33',  # Box 4 -> (3, 3)
        ]
        self.bad_indices = [0, 5, -1]
        self.bad_row_columns = [
            '51',
            '03',
            '30',
            '55'
        ]


class Test6x6BoardCalculations(TestBoardCalculations):
    """Tests specific to the 6x6 board with 2x3 boxes."""

    def setUp(self):
        """Set up the 6x6 board with 2x3 boxes and expected values."""
        super().setUp()
        self.board_size = Coord(6, 6)
        self.box_size = Coord(2, 3)

        self.expected_box_indices = [
            '111222',  # Row 1
            '111222',  # Row 2
            '333444',  # Row 3
            '333444',  # Row 4
            '555666',  # Row 5
            '555666',  # Row 6
        ]
        self.expected_top_lefts = [
            '11',  # Box 1 -> (1, 1)
            '14',  # Box 2 -> (1, 3)
            '31',  # Box 3 -> (3, 1)
            '34',  # Box 4 -> (3, 3)
            '51',  # Box 4 -> (3, 3)
            '54',  # Box 4 -> (3, 3)
        ]
        self.bad_indices = [0, 7, -1]
        self.bad_row_columns = [
            '91',
            '03',
            '30',
            '99'
        ]


class Test9x9BoardCalculations(TestBoardCalculations):
    """Tests specific to the 9x9 board with 3x3 boxes."""

    def setUp(self):
        """Set up the 9x9 board with 3x3 boxes and expected values."""
        super().setUp()
        self.board_size = Coord(9, 9)
        self.box_size = Coord(3, 3)

        self.expected_box_indices = [
            '111222333',  # Row 1
            '111222333',  # Row 1
            '111222333',  # Row 1
            '444555666',  # Row 1
            '444555666',  # Row 1
            '444555666',  # Row 1
            '777888999',  # Row 1
            '777888999',  # Row 1
            '777888999',  # Row 1
        ]
        self.expected_top_lefts = [
            '11',  # Box 1 -> (1, 1)
            '14',  # Box 2 -> (1, 3)
            '17',  # Box 2 -> (1, 3)
            '41',  # Box 1 -> (1, 1)
            '44',  # Box 2 -> (1, 3)
            '47',  # Box 2 -> (1, 3)
            '71',  # Box 1 -> (1, 1)
            '74',  # Box 2 -> (1, 3)
            '77',  # Box 2 -> (1, 3)
        ]
        self.bad_indices = [0, 10, -1]
        self.bad_row_columns = [
            '03',
            '30',
        ]
