"""TestValueToken."""
import unittest

from src.tokens.value_token import ValueToken
from tests.tokens.test_simple_token import TestSimpleToken


class TestValueToken(TestSimpleToken):
    """Test cases for the SideToken class."""

    def setUp(self):
        """Set up example tokens specific for testing QuadrupleToken."""
        self.token = ValueToken()
        self.representation = "ValueToken()"
        self.pattern = r"(\d+)"
        self.name = 'Value'


if __name__ == "__main__":
    unittest.main()

