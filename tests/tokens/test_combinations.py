"""TestCombinations."""
import unittest

from src.tokens.cell_token import CellToken
from src.tokens.symbols import CommaToken
from src.tokens.token import Token


class TestCombinations(unittest.TestCase):
    """Test Combinations of Tokens."""

    def test_cell(self):
        """Test matching a single cell token."""
        token: Token = CellToken()
        self.assertTrue(token.match("11"))

    def test_cell_list(self):
        """Test matching a list of cell tokens separated by commas."""
        token: Token = CellToken() + CommaToken() + CellToken()
        self.assertTrue(token.match("11,22"))

    def test_long_cell_list(self):
        """Test matching a long list of cell tokens separated by commas."""
        token: Token = CellToken() + (CommaToken() + CellToken()) * (0, 999)
        self.assertTrue(token.match("11,22,33"))
        self.assertTrue(token.match("11,22,33,44"))

    def test_empty_input(self):
        """Test if empty input returns False for cell matching."""
        token: Token = CellToken() + CommaToken() + CellToken()
        self.assertFalse(token.match(""))

    def test_invalid_format(self):
        """Test if an incorrectly formatted cell list returns False."""
        token: Token = CellToken() + CommaToken() + CellToken()
        self.assertFalse(token.match("11,,22"))


if __name__ == '__main__':
    unittest.main()
