import unittest

from src.tokens.direction_token import DirectionToken
from tests.tokens.test_simple_token import TestSimpleToken


class TestDirectionToken(TestSimpleToken):
    """Test cases for the DirectionToken class."""

    def setUp(self):
        """Set up example tokens specific for testing DirectionToken."""
        self.token = DirectionToken()
        self.representation = "DirectionToken()"
        self.pattern = r"([CA])"
        self.name = 'Direction'
        self.good = ['C', 'A']
        self.bad = ['X', '0', '1']
        self.group_count = 1


if __name__ == "__main__":
    unittest.main()
