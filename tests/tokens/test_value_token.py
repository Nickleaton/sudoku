"""TestValueToken."""
import unittest

from src.tokens.value_token import ValueToken
from tests.tokens.test_simple_token import TestSimpleToken


class TestValueToken(TestSimpleToken):
    """Test cases for the SideToken class."""

    def setUp(self):
        """Set up example tokens specific for testing QuadrupleToken."""
        super().setUp()
        self.token = ValueToken()
        self.representation = 'ValueToken()'
        self.pattern = r'(\d+)'
        self.good = ['1', '99']
        self.bad = ['X']
        self.name = 'Value'
        self.group_count = 1
        self.backus_naur = '<Value>'


if __name__ == '__main__':
    unittest.main()
