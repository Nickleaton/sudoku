"""TestQuadrupleToken."""
import unittest

from src.tokens.quadruple_token import QuadrupleToken
from tests.tokens.test_simple_token import TestSimpleToken


class TestQuadToken(TestSimpleToken):
    """Test cases for the SideToken class."""

    def setUp(self):
        """Set up example tokens specific for testing QuadrupleToken."""
        self.token = QuadrupleToken()
        self.representation = "QuadrupleToken()"
        self.pattern = r"([\d?]+)"
        self.name = 'Quad'
        self.good = ['1234', '12', '1122', '?', '12?', '????']
        self.bad = ['12345', 'X' ]
        self.group_count = 1


if __name__ == "__main__":
    unittest.main()

