"""TestSymbols."""
import unittest

from src.tokens.symbols import CommaToken, DashToken, EqualsToken, SymbolToken, QuestionMarkToken, XToken, DotDotToken
from tests.tokens.test_simple_token import TestSimpleToken


class TestSymbolToken(TestSimpleToken):
    """Test Symbol Token."""

    def setUp(self):
        """Set up example tokens specific for testing DashToken."""
        super().setUp()
        self.token = SymbolToken('row')
        self.representation = "SymbolToken('row', 'row')"
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


class TestXToken(TestSymbolToken):
    """Test cases for the XToken class."""

    def setUp(self):
        """Set up example tokens specific for testing XToken."""
        super().setUp()
        self.token = XToken()
        self.representation = "XToken()"
        self.pattern = r"x"
        self.name = 'X'
        self.good = ['x']
        self.bad = ['X', 'xx']
        self.backus_naur = '"x"'


class TestDotDotToken(TestSymbolToken):
    """Test cases for the DotDotToken class."""

    def setUp(self):
        """Set up example tokens specific for testing DotDotToken."""
        super().setUp()
        self.token = DotDotToken()
        self.representation = "DotDotToken()"
        self.pattern = r"\.\."
        self.name = 'DotDot'
        self.good = ['..']
        self.bad = ['.', '...']
        self.backus_naur = '".."'


if __name__ == "__main__":
    unittest.main()
