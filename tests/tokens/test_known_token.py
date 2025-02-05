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
        self.pattern = r"(?P<cell>[0-9.])"
        self.name = 'Known'
        self.good = [
            ('.', {'cell': '.'}),
            ('2', {'cell': '2'}),
        ]
        self.bad = ['row', 'X', '?']
        self.backus_naur = '<Known>'
        self.result = {'cell': 'l'}


if __name__ == "__main__":
    unittest.main()
