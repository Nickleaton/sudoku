"""TestSimpleToken."""
import unittest

from src.tokens.simple_token import SimpleToken
from tests.tokens.test_token import TestToken


class TestSimpleToken(TestToken):
    """Test cases for the SimpleToken class."""

    def setUp(self):
        """Set up example tokens specific for testing SimpleToken."""
        super().setUp()  #
        self.token = SimpleToken(r"A")
        self.representation = "SimpleToken()"
        self.pattern = "A"
        self.name = 'Simple'
        self.group_count = 0
        self.backus_naur = "<Simple>"


if __name__ == "__main__":
    unittest.main()
