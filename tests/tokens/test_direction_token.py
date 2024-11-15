"""TestDirectionToken."""
import unittest
from src.tokens.direction_token import DirectionToken
from src.utils.direction import Direction
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

    def test_direction(self):
        """Test the behavior of Direction.direction method."""
        # Test invalid input for direction
        with self.assertRaises(ValueError):
            _ = Direction.direction(10)

        # Test valid locations
        for location in range(1, 10):
            # Check that direction(location) does not raise errors
            result = Direction.direction(location)
            # Optional: Add checks if the result matches expected values
            self.assertIn(result, ['C', 'A'], f"Unexpected result for location {location}: {result}")

    def test_valid_tokens(self):
        """Test that valid tokens are matched."""
        for token in self.good:
            self.assertTrue(self.token.match(token), f"Token {token} should match but didn't.")

    def test_invalid_tokens(self):
        """Test that invalid tokens are rejected."""
        for token in self.bad:
            self.assertFalse(self.token.match(token), f"Token {token} should not match but did.")

if __name__ == "__main__":
    unittest.main()
