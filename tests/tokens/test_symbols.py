"""TestSymbols."""
import unittest

from src.tokens.symbols import CommaToken, DashToken, DotDotToken, EndToken, EqualsToken, QuestionMarkToken, StartToken, \
    SymbolToken, XToken
from tests.tokens.test_simple_token import TestSimpleToken


class TestSymbolToken(TestSimpleToken):
    """Base test class for symbol tokens."""

    def setUp(self):
        """Set up a SymbolToken instance for testing."""
        super().setUp()
        self.token = SymbolToken('row')
        self.representation = "SymbolToken('row', 'row')"
        self.pattern = "row"
        self.name = 'Symbol'
        self.good = \
            [
                ('row', {}),
            ]
        self.bad = ['X', '--']
        self.backus_naur = '"row"'


class TestCommaToken(TestSymbolToken):
    """Tests for the CommaToken class."""

    def setUp(self):
        """Set up a CommaToken instance for testing."""
        super().setUp()
        self.token = CommaToken()
        self.representation = "CommaToken()"
        self.pattern = r","
        self.name = 'Comma'
        self.good = \
            [
                (',', {}),
            ]
        self.bad = ['X', ',,']
        self.backus_naur = '","'


class TestDashToken(TestSymbolToken):
    """Tests for the DashToken class."""

    def setUp(self):
        """Set up a DashToken instance for testing."""
        super().setUp()
        self.token = DashToken()
        self.representation = "DashToken()"
        self.pattern = r"-"
        self.name = 'Dash'
        self.good = \
            [
                ('-', {}),
            ]
        self.bad = ['X', '--']
        self.backus_naur = '"-"'


class TestEqualsToken(TestSymbolToken):
    """Tests for the EqualsToken class."""

    def setUp(self):
        """Set up an EqualsToken instance for testing."""
        super().setUp()
        self.token = EqualsToken()
        self.representation = "EqualsToken()"
        self.pattern = r"="
        self.name = 'Equals'
        self.good = \
            [
                ('=', {}),
            ]
        self.bad = ['X', '==']
        self.backus_naur = '"="'


class TestQuestionMarkToken(TestSymbolToken):
    """Tests for the QuestionMarkToken class."""

    def setUp(self):
        """Set up a QuestionMarkToken instance for testing."""
        super().setUp()
        self.token = QuestionMarkToken()
        self.representation = "QuestionMarkToken()"
        self.pattern = r"\?"
        self.name = 'QuestionMark'
        self.good = \
            [
                ('?', {}),
            ]
        self.bad = ['X', '==']
        self.backus_naur = r'"?"'


class TestXToken(TestSymbolToken):
    """Tests for the XToken class."""

    def setUp(self):
        """Set up an XToken instance for testing."""
        super().setUp()
        self.token = XToken()
        self.representation = "XToken()"
        self.pattern = r"x"
        self.name = 'X'
        self.good = \
            [
                ('x', {}),
            ]
        self.bad = ['X', 'xx']
        self.backus_naur = '"x"'


class TestDotDotToken(TestSymbolToken):
    """Tests for the DotDotToken class."""

    def setUp(self):
        """Set up a DotDotToken instance for testing."""
        super().setUp()
        self.token = DotDotToken()
        self.representation = "DotDotToken()"
        self.pattern = r"\.\."
        self.name = 'DotDot'
        self.good = \
            [
                ('..', {}),
            ]
        self.bad = ['.', '...', 'x']
        self.backus_naur = '".."'


class TestStartToken(TestSymbolToken):
    """Tests for the StartToken class."""

    def setUp(self):
        """Set up a StartToken instance for testing."""
        super().setUp()
        self.token = StartToken()
        self.representation = "StartToken()"
        self.pattern = r"^"
        self.name = 'Start'
        self.good = \
            [
                ('', {}),
            ]
        self.bad = ['X', '^^']
        self.backus_naur = '"^"'


class TestEndToken(TestSymbolToken):
    """Tests for the EndToken class."""

    def setUp(self):
        """Set up an EndToken instance for testing."""
        super().setUp()
        self.token = EndToken()
        self.representation = "EndToken()"
        self.pattern = r"$"
        self.name = 'End'
        self.good = \
            [
                ('', {}),
            ]
        self.bad = ['X', '$$']
        self.backus_naur = '"$"'


if __name__ == "__main__":
    unittest.main()
