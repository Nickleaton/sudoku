"""TestSizeToken."""
import unittest

from src.tokens.size_token import SizeToken
from tests.tokens.test_simple_token import TestSimpleToken


class TestSizeToken(TestSimpleToken):
    """Test cases for the SizeToken class."""

    def setUp(self):
        """Set up example tokens specific for testing SizeToken."""
        super().setUp()
        self.token = SizeToken()
        self.representation = 'SizeToken()'
        self.pattern = r'(?P<rows>\d\d{0,1})x(?P<cols>\d\d{0,1})'
        self.name = 'Size'
        self.good = \
            [
                ('9x9', {'cols': 9, 'rows': 9}),
                ('2x3', {'cols': 3, 'rows': 2}),
                ('4x4', {'cols': 4, 'rows': 4}),
                ('16x16', {'cols': 16, 'rows': 16}),
            ]
        self.bad = ['99', '2*3', '4by4']
        self.group_count = 2
        self.backus_naur = '<Size>'
        self.result = {'rows': 9, 'cols': 9}


if __name__ == "__main__":
    unittest.main()
