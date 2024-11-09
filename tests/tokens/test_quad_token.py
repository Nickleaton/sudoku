import unittest

from src.tokens.quad_token import QuadToken
from tests.tokens.test_simple_token import TestSimpleToken


class TestQuadToken(TestSimpleToken):
    """Test cases for the SideToken class."""

    def setUp(self):
        """Set up example tokens specific for testing QuadToken."""
        self.token = QuadToken()
        self.representation = "QuadToken()"
        self.pattern = r"([\d?]+)"
        self.name = 'Quad'
        self.good = ['1234', '12', '1122', '?', '12?', '????']
        self.bad = ['12345', 'X' ]
        self.group_count = 1


if __name__ == "__main__":
    unittest.main()
