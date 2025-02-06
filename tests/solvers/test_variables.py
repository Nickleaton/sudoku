import unittest

from src.board.board import Board
from src.board.cell_types import EntropicType, ModuloType, ParityType, PrimeType
from src.board.digits import Digits
from src.solvers.variables import Variables, VariableSet
from src.utils.coord import Coord
from src.utils.tags import Tags


class TestVariables(unittest.TestCase):
    """Unit tests for the Variables class."""

    def setUp(self):
        """Sets up a mock board for testing."""
        self.board: Board = Board(Coord(9, 9), Digits(1, 9), Tags())

    @staticmethod
    def counter(variables: dict) -> int:
        if not isinstance(variables, dict):
            return 1
        return sum(TestVariables.counter(value) for value in variables.values())

    def test_add_choices(self):
        """Tests that choice variables are added correctly."""
        variables = Variables(self.board, [VariableSet.choice])
        count: int = self.board.digits.maximum * self.board.size.column * self.board.size.row
        self.assertEqual(count, TestVariables.counter(variables.choices))

    def test_add_value(self):
        """Tests that number variables are added correctly."""
        variables = Variables(self.board, [VariableSet.number])
        count: int = self.board.size.column * self.board.size.row
        self.assertEqual(count, TestVariables.counter(variables.numbers))

    def test_add_parity(self):
        """Tests that parity variables are added correctly."""
        variables = Variables(self.board, [VariableSet.parity])
        count: int = self.board.size.column * self.board.size.row * len(ParityType)
        self.assertEqual(count, TestVariables.counter(variables.parity))

    def test_add_entropic(self):
        """Tests that entropy variables are added correctly."""
        variables = Variables(self.board, [VariableSet.entropic])
        count: int = self.board.size.column * self.board.size.row * len(EntropicType)
        self.assertEqual(count, TestVariables.counter(variables.entropic))

    def test_add_modulo(self):
        """Tests that modulo variables are added correctly."""
        variables = Variables(self.board, [VariableSet.modulo])
        count: int = self.board.size.column * self.board.size.row * len(ModuloType)
        self.assertEqual(count, TestVariables.counter(variables.modulo))

    def test_add_prime(self):
        """Tests that prime variables are added correctly."""
        variables = Variables(self.board, [VariableSet.prime])
        count: int = self.board.size.column * self.board.size.row * len(PrimeType)
        self.assertEqual(count, TestVariables.counter(variables.prime))


if __name__ == '__main__':
    unittest.main()
