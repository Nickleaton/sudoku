import unittest

from src.tokens.digit_token import DigitToken
from tests.tokens.test_simple_token import TestSimpleToken


class TestDigitToken(TestSimpleToken):
    """Test cases for the DigitToken class."""

    def setUp(self):
        """Set up example tokens specific for testing DigitToken."""
        self.token = DigitToken()
        self.representation = "DigitToken()"
        self.pattern = r"\d"
        self.name = 'Digit'
        self.good = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.bad = ['A', 'B', 'C', 'D']
        self.group_count = 1

if __name__ == "__main__":
    unittest.main()
