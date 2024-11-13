import unittest

from src.tokens.symbols import CommaToken, DashToken, EqualsToken, SymbolToken, QuestionMarkToken
from tests.tokens.test_simple_token import TestSimpleToken


class TestSymbolToken(TestSimpleToken):
    def setUp(self):
        """Set up example tokens specific for testing DashToken."""
        self.token = SymbolToken('x')
        self.representation = "SymbolToken('x')"
        self.pattern = "x"
        self.name = 'Symbol'
        self.good = ['x']
        self.bad = ['X', '--']
        self.group_count = 1
        self.bnf = '"x"'

    def test_backus_naur_form(self):
        self.assertEqual(self.bnf, self.token.backus_naur_form())


class TestCommaToken(TestSymbolToken):
    """Test cases for the CommaToken class."""

    def setUp(self):
        """Set up example tokens specific for testing CommaToken."""
        self.token = CommaToken()
        self.representation = "CommaToken()"
        self.pattern = r","
        self.name = 'Comma'
        self.good = [',']
        self.bad = ['X', ',,']
        self.group_count = 1
        self.bnf = '","'


class TestDashToken(TestSymbolToken):
    """Test cases for the DashToken class."""

    def setUp(self):
        """Set up example tokens specific for testing DashToken."""
        self.token = DashToken()
        self.representation = "DashToken()"
        self.pattern = r"-"
        self.name = 'Dash'
        self.good = ['-']
        self.bad = ['X', '--']
        self.group_count = 1
        self.bnf = '"-"'


class TestEqualsToken(TestSymbolToken):
    """Test cases for the EqualsToken class."""

    def setUp(self):
        """Set up example tokens specific for testing EqualsToken."""
        self.token = EqualsToken()
        self.representation = "EqualsToken()"
        self.pattern = r"="
        self.name = 'Equals'
        self.good = ['=']
        self.bad = ['X', '==']
        self.group_count = 1
        self.bnf = '"="'


class TestQuestionMarkToken(TestSymbolToken):
    """Test cases for the EqualsToken class."""

    def setUp(self):
        """Set up example tokens specific for testing EqualsToken."""
        self.token = QuestionMarkToken()
        self.representation = "QuestionMarkToken()"
        self.pattern = r"\?"
        self.name = 'QuestionMark'
        self.good = ['?']
        self.bad = ['X', '==']
        self.group_count = 1
        self.bnf = r'"?"'


if __name__ == "__main__":
    unittest.main()
