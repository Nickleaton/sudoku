import unittest

from src.tokens.cell_token import CellToken
from src.tokens.symbols import CommaToken
from src.tokens.token import Token


class TestCombinations(unittest.TestCase):

    def test_cell(self):
        token: Token = CellToken()
        self.assertTrue(token.match("11"))

    def test_cell_list(self):
        token: Token = CellToken() + CommaToken() + CellToken()
        self.assertTrue(token.match("11,22"))


    def test_long_cell_list(self):
        token: Token = CellToken() + (CommaToken() + CellToken()) * (0, 999)
        self.assertTrue(token.match("11,22,33"))
        self.assertTrue(token.match("11,22,33,44"))


if __name__ == '__main__':
    unittest.main()
