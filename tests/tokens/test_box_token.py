"""TestBoxToken."""
import unittest

from src.tokens.box_token import BoxToken
from tests.tokens.test_simple_token import TestSimpleToken


class TestBoxToken(TestSimpleToken):
    """Test cases for the BoxToken class."""

    def setUp(self):
        """Set up example tokens specific for testing BoxToken."""
        super().setUp()
        self.token = BoxToken()
        self.representation = "BoxToken()"
        self.pattern = r"(\d)x(\d)"
        self.name = 'Box'
        self.good = ['9x9', '2x3', '4x4']
        self.bad = ['99', '2*3', '4by4']
        self.group_count = 2
        self.backus_naur = '<Box>'


if __name__ == "__main__":
    unittest.main()
