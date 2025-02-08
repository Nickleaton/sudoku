"""TestSimpleToken."""
import unittest

from src.tokens.simple_token import SimpleToken
from tests.tokens.test_token import TestToken


class TestSimpleToken(TestToken):
    """Test cases for the SimpleToken class."""

    def setUp(self):
        """Set up example tokens specific for testing SimpleToken."""
        super().setUp()
        self.token = SimpleToken('A')
        self.representation = "SimpleToken()"
        self.good = [
            ('A', {})
        ]
        self.pattern = 'A'
        self.name = 'Simple'
        self.backus_naur = '<Simple>'


if __name__ == '__main__':
    unittest.main()
