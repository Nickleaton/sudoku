"""TestSymbols."""
import unittest

from src.tokens.symbols import CommaToken, DashToken, EqualsToken, SymbolToken, QuestionMarkToken
from tests.tokens.test_simple_token import TestSimpleToken


class TestSymbolToken(TestSimpleToken):
    """Test Symbol Token."""

    def setUp(self):
        """Set up example tokens specific for testing DashToken."""
        super().setUp()
        self.token = SymbolToken('row')
        self.representation = "SymbolToken('row')"
        self.pattern = "row"
        self.name = 'Symbol'
        self.good = ['row']
        self.bad = ['X', '--']
        self.backus_naur = '"row"'


class TestCommaToken(TestSymbolToken):
    """Test cases for the CommaToken class."""

    def setUp(self):
        """Set up example tokens specific for testing CommaToken."""
        super().setUp()
        self.token = CommaToken()
        self.representation = "CommaToken()"
        self.pattern = r","
        self.name = 'Comma'
        self.good = [',']
        self.bad = ['X', ',,']
        self.backus_naur = '","'


class TestDashToken(TestSymbolToken):
    """Test cases for the DashToken class."""

    def setUp(self):
        """Set up example tokens specific for testing DashToken."""
        super().setUp()
        self.token = DashToken()
        self.representation = "DashToken()"
        self.pattern = r"-"
        self.name = 'Dash'
        self.good = ['-']
        self.bad = ['X', '--']
        self.backus_naur = '"-"'


class TestEqualsToken(TestSymbolToken):
    """Test cases for the EqualsToken class."""

    def setUp(self):
        """Set up example tokens specific for testing EqualsToken."""
        super().setUp()
        self.token = EqualsToken()
        self.representation = "EqualsToken()"
        self.pattern = r"="
        self.name = 'Equals'
        self.good = ['=']
        self.bad = ['X', '==']
        self.backus_naur = '"="'


class TestQuestionMarkToken(TestSymbolToken):
    """Test cases for the EqualsToken class."""

    def setUp(self):
        """Set up example tokens specific for testing EqualsToken."""
        super().setUp()
        self.token = QuestionMarkToken()
        self.representation = "QuestionMarkToken()"
        self.pattern = r"\?"
        self.name = 'QuestionMark'
        self.good = ['?']
        self.bad = ['X', '==']
        self.backus_naur = r'"?"'


if __name__ == "__main__":
    unittest.main()
