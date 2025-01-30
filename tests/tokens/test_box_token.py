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
        self.representation = 'BoxToken()'
        self.pattern = r'(?P<row>\d)x(?P<col>\d)'
        self.name = 'Box'
        self.good = ['2x3', '3x3', '4x4']
        self.bad = ['99', '2*3', '4by4']
        self.backus_naur = '<Box>'
        self.result = {'row': 2, 'col': 3}


if __name__ == "__main__":
    unittest.main()
