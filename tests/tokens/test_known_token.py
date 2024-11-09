import unittest

from src.tokens.known_token import KnownToken
from tests.tokens.test_simple_token import TestSimpleToken


class TestKnownToken(TestSimpleToken):
    """Test cases for the KnownToken class."""

    def setUp(self):
        """Set up example tokens specific for testing KnownToken."""
        self.token = KnownToken()
        self.representation = "KnownToken()"
        self.pattern = r"([0-9.lmheof])"
        self.name = 'Known'
        self.good = ['0', '9', 'l', 'm', 'h', 'e', 'o', 'f', '.']
        self.bad = ['x', 'X', '?']
        self.group_count = 1


if __name__ == "__main__":
    unittest.main()
