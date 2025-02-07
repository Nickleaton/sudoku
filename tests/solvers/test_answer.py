"""Test Answer class for Sudoku board functionality."""
import unittest

from src.board.board import Board
from src.board.digits import Digits
from src.solvers.answer import Answer
from src.utils.coord import Coord
from src.utils.tags import Tags


class TestAnswer(unittest.TestCase):
    """Test the Answer class and its methods."""

    def setUp(self) -> None:
        """Set up the test environment."""
        # Initialize start Board object and Answer object
        self.board: Board = Board(Coord(9, 9), Digits(1, 9), Tags())
        data = (
            "123456789",
            "123456789",
            "123456789",
            "123456789",
            "123456789",
            "123456789",
            "123456789",
            "123456789",
            "123456789"
        )
        self.item = Answer(self.board, data)
        data = (
            "123456789",
            "123456789",
            "123456789",
            "123456789",
            "123456789",
            "123456789",
            "123456789",
            "123456789",
            "123456781"
        )
        self.other = Answer(self.board, data)

    @property
    def representation(self) -> str:
        """Return the string representation of the Answer object."""
        return (
            "Answer(\n"
            "    Board(Coord(9, 9), Digits(1, 9), Tags({})),\n"
            "    [\n"
            "    '123456789',\n"
            "    '123456789',\n"
            "    '123456789',\n"
            "    '123456789',\n"
            "    '123456789',\n"
            "    '123456789',\n"
            "    '123456789',\n"
            "    '123456789',\n"
            "    '123456789'\n"
            "    ]\n"
            ")"
        )

    def test_repr(self):
        """Test the __repr__ method of the Answer class."""
        unittest.TestCase.maxDiff = None
        self.assertEqual(self.representation, repr(self.item))

    def test_set_get(self):
        """Test the get_value and set_value methods of the Answer class."""
        self.assertEqual(1, self.item[1, 1])
        self.assertEqual(9, self.item[9, 9])
        self.item[1, 1] = 8
        self.item[9, 9] = 8
        self.assertEqual(8, self.item[1, 1])
        self.assertEqual(8, self.item[9, 9])

    def test_equality(self):
        """Test equality and inequality comparisons for Answer objects."""
        self.assertEqual(self.item, self.item)
        self.assertNotEqual(self.item, self.other)
        self.assertNotEqual(self.item, '123')

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
                "  - 123456789"
                )
        self.assertEqual(text, str(self.item))

    # def test_standard_output(self):
    #     """Test the standard_string method of the Answer object."""
    #     expected = (
    #         "+-------+-------+-------+\n"
    #         "| 1 2 3 | 4 5 6 | 7 8 9 |\n"
    #         "| 1 2 3 | 4 5 6 | 7 8 9 |\n"
    #         "| 1 2 3 | 4 5 6 | 7 8 9 |\n"
    #         "+-------+-------+-------+\n"
    #         "| 1 2 3 | 4 5 6 | 7 8 9 |\n"
    #         "| 1 2 3 | 4 5 6 | 7 8 9 |\n"
    #         "| 1 2 3 | 4 5 6 | 7 8 9 |\n"
    #         "+-------+-------+-------+\n"
    #         "| 1 2 3 | 4 5 6 | 7 8 9 |\n"
    #         "| 1 2 3 | 4 5 6 | 7 8 9 |\n"
    #         "| 1 2 3 | 4 5 6 | 7 8 9 |\n"
    #         "+-------+-------+-------+\n"
    #     )
    #     self.assertEqual(expected, self.item.standard_string())


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
