"""Test Answer class for Sudoku board functionality."""
import unittest

from src.board.board import Board
from src.solvers.answer import Answer
from src.utils.sudoku_exception import SudokuException


class TestAnswer(unittest.TestCase):
    """Test the Answer class and its methods."""

    def setUp(self) -> None:
        """Set up the test environment."""
        # Initialize a Board object and Answer object
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        data = [
            "123456789",
            "123456789",
            "123456789",
            "123456789",
            "123456789",
            "123456789",
            "123456789",
            "123456789",
            "123456789"
        ]
        self.item = Answer(self.board, data)
        data = [
            "123456789",
            "123456789",
            "123456789",
            "123456789",
            "123456789",
            "123456789",
            "123456789",
            "123456789",
            "123456781"
        ]
        self.other = Answer(self.board, data)

    @property
    def representation(self) -> str:
        """Return the string representation of the Answer object."""
        return (
            "Answer("
            "Board(9, 9, 3, 3, None, None, None, None),"
            "["
            "'123456789', "
            "'123456789', "
            "'123456789', "
            "'123456789', "
            "'123456789', "
            "'123456789', "
            "'123456789', "
            "'123456789', "
            "'123456789'"
            "]"
            ")"
        )

    def test_repr(self):
        """Test the __repr__ method of the Answer class."""
        unittest.TestCase.maxDiff = None
        self.assertEqual(self.representation, repr(self.item))

    def test_set_get(self):
        """Test the get_value and set_value methods of the Answer class."""
        self.assertEqual(1, self.item.get_value(1, 1))
        self.assertEqual(9, self.item.get_value(9, 9))
        self.item.set_value(1, 1, 8)
        self.item.set_value(9, 9, 8)
        self.assertEqual(8, self.item.get_value(1, 1))
        self.assertEqual(8, self.item.get_value(9, 9))

    def test_equality(self):
        """Test equality and inequality comparisons for Answer objects."""
        self.assertEqual(self.item, self.item)
        self.assertNotEqual(self.item, self.other)
        with self.assertRaises(SudokuException):
            _ = self.item == '123'

    def test_string(self):
        """Test the string representation of the Answer object."""
        text = ("Answer:\n"
                "  - 123456789\n"
                "  - 123456789\n"
                "  - 123456789\n"
                "  - 123456789\n"
                "  - 123456789\n"
                "  - 123456789\n"
                "  - 123456789\n"
                "  - 123456789\n"
                "  - 123456789\n"
                )
        self.assertEqual(text, str(self.item))

    def test_standard_output(self):
        """Test the standard_string method of the Answer object."""
        expected = (
            "+-------+-------+-------+\n"
            "| 1 2 3 | 4 5 6 | 7 8 9 |\n"
            "| 1 2 3 | 4 5 6 | 7 8 9 |\n"
            "| 1 2 3 | 4 5 6 | 7 8 9 |\n"
            "+-------+-------+-------+\n"
            "| 1 2 3 | 4 5 6 | 7 8 9 |\n"
            "| 1 2 3 | 4 5 6 | 7 8 9 |\n"
            "| 1 2 3 | 4 5 6 | 7 8 9 |\n"
            "+-------+-------+-------+\n"
            "| 1 2 3 | 4 5 6 | 7 8 9 |\n"
            "| 1 2 3 | 4 5 6 | 7 8 9 |\n"
            "| 1 2 3 | 4 5 6 | 7 8 9 |\n"
            "+-------+-------+-------+\n"
        )
        self.assertEqual(expected, self.item.standard_string())


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
