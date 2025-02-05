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
        self.pattern = r'(?P<rows>\d)x(?P<cols>\d)'
        self.name = 'Box'
        self.good = [
            ('2x3', {'rows': 2, 'cols': 3}),
            ('3x3', {'rows': 3, 'cols': 3}),
            ('4x4', {'rows': 4, 'cols': 4}),
        ]
        self.bad = ['99', '2*3', '4by4']
        self.backus_naur = '<Box>'
        self.result = {'rows': 2, 'cols': 3}


if __name__ == "__main__":
    unittest.main()
