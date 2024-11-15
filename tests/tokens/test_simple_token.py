"""TestSimpleToken."""
import unittest

from src.tokens.simple_token import SimpleToken


class TestSimpleToken(unittest.TestCase):
    """Test cases for the SimpleToken class."""

    def setUp(self):
        """Set up example tokens specific for testing SimpleToken."""
        super().setUp()  #
        self.token = SimpleToken(r"A")
        self.representation = "SimpleToken()"
        self.pattern = "A"
        self.name = 'Simple'
        self.group_count = 1

    def test_representation(self):
        """Test the string representation of the SimpleToken."""
        self.assertEqual(repr(self.token), self.representation)

    def test_pattern(self):
        """Test that the pattern of the SimpleToken is correct."""
        self.assertEqual(self.token.pattern, self.pattern)


if __name__ == "__main__":
    unittest.main()

