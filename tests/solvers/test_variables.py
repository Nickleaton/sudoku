import unittest

from src.board.board import Board
from src.board.cell_types import ParityType, ModuloType, PrimeType, EntropicType
from src.solvers.variables import Variables, Variable


class TestVariables(unittest.TestCase):
    """Unit tests for the Variables class."""

    def setUp(self):
        """Sets up a mock board for testing."""
        tags: dict[str, str] = {'Reference': 'start', 'Video': 'finish', 'Title': 'c', 'Author': 'd'}
        self.board: Board = Board(9, 9, 3, 3, tags=tags)

    @staticmethod
    def counter(variables: dict) -> int:
        if not isinstance(variables, dict):
            return 1
        return sum(TestVariables.counter(value) for value in variables.values())

    def test_add_choices(self):
        """Tests that choice variables are added correctly."""
        variables = Variables(self.board, [Variable.choice])
        self.assertIn('choices', variables)
        count: int = self.board.maximum_digit * self.board.board_columns * self.board.board_rows
        self.assertEqual(count, TestVariables.counter(variables.choices))

    def test_add_value(self):
        """Tests that value variables are added correctly."""
        variables = Variables(self.board, [Variable.value])
        self.assertIn('values_', variables)
        count: int = self.board.board_columns * self.board.board_rows
        self.assertEqual(count, TestVariables.counter(variables.values_))

    def test_add_parity(self):
        """Tests that parity variables are added correctly."""
        variables = Variables(self.board, [Variable.parity])
        self.assertIn('parity', variables)
        count: int = self.board.board_columns * self.board.board_rows * len(ParityType)
        self.assertEqual(count, TestVariables.counter(variables.parity))

    def test_add_entropic(self):
        """Tests that entropy variables are added correctly."""
        variables = Variables(self.board, [Variable.entropic])
        self.assertIn('entropic', variables)
        count: int = self.board.board_columns * self.board.board_rows * len(EntropicType)
        self.assertEqual(count, TestVariables.counter(variables.entropic))

    def test_add_modulo(self):
        """Tests that modulo variables are added correctly."""
        variables = Variables(self.board, [Variable.modulo])
        self.assertIn('modulo', variables)
        count: int = self.board.board_columns * self.board.board_rows * len(ModuloType)
        self.assertEqual(count, TestVariables.counter(variables.modulo))

    def test_add_prime(self):
        """Tests that prime variables are added correctly."""
        variables = Variables(self.board, [Variable.prime])
        self.assertIn('prime', variables)
        count: int = self.board.board_columns * self.board.board_rows * len(PrimeType)
        self.assertEqual(count, TestVariables.counter(variables.prime))


if __name__ == '__main__':
    unittest.main()
