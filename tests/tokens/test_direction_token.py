"""TestDirectionToken."""
import unittest

from src.tokens.direction_token import DirectionToken
from tests.tokens.test_simple_token import TestSimpleToken


class TestDirectionToken(TestSimpleToken):
    """Test cases for the DirectionToken class."""

    def setUp(self):
        """Set up example tokens specific for testing DirectionToken."""
        super().setUp()
        self.token = DirectionToken()
        self.representation = "DirectionToken()"
        self.pattern = r"(?P<direction>(?!UD|DU|LR|RL)(UR|UL|DL|DR|U|D|L|R))"  # Regex for direction values
        self.name = 'Direction'
        self.good = ['UL', 'U', 'UR', 'L', 'R', 'DL', 'D', 'DR']
        self.bad = ['X', '0', '1', 'LR', 'UD', 'DU', 'RL']
        self.backus_naur = '<Direction>'
        self.result = {'direction': 'UL'}  # Example of matching direction

    def test_good_values(self):
        """Test that the valid direction values are matched."""
        for value in self.good:
            with self.subTest(value=value):
                self.assertTrue(self.token.match(value), f"{value} should be a valid direction")

    def test_bad_values(self):
        """Test that the invalid direction values are not matched."""
        for value in self.bad:
            with self.subTest(value=value):
                self.assertFalse(self.token.match(value), f"{value} should not be a valid direction")


if __name__ == "__main__":
    unittest.main()
