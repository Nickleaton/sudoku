"""TestKnownToken."""
import unittest

from src.tokens.known_token import KnownToken
from tests.tokens.test_simple_token import TestSimpleToken


class TestKnownToken(TestSimpleToken):
    """Test cases for the KnownToken class."""

    def setUp(self):
        """Set up example tokens specific for testing KnownToken."""
        super().setUp()
        self.token = KnownToken()
        self.representation = "KnownToken()"
        self.pattern = r"([0-9.lmheof])"
        self.name = 'Known'
        self.good = ['0', '9', 'l', 'm', 'h', 'e', 'o', 'f', '.']
        self.bad = ['row', 'X', '?']
        self.group_count = 1
        self.backus_naur = '<Known>'


if __name__ == "__main__":
    unittest.main()
