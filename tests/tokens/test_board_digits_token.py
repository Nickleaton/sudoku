"""TestDigitsToken."""
import unittest

from src.tokens.board_digits_token import BoardDigitsToken
from tests.tokens.test_simple_token import TestSimpleToken


class TestBoardDigitsToken(TestSimpleToken):
    """Test cases for the BoardDigitsToken class."""

    def setUp(self):
        """Set up example tokens specific for testing BoardDigitsToken."""
        super().setUp()
        self.token = BoardDigitsToken()
        self.representation = 'BoardDigitsToken()'
        self.pattern = r'(?P<minimum>\d)\.\.(?P<maximum>\d\d{0,1})'
        self.name = 'BoardDigits'
        self.good = ['1..9', '0..8', '1..8', '1..15', '1..4', '1..6']
        self.bad = ['12', '9.1', '..9', 'a..b']
        self.group_count = 2
        self.backus_naur = '<BoardDigits>'
        self.result = {'minimum': 1, 'maximum': 9}


if __name__ == "__main__":
    unittest.main()
