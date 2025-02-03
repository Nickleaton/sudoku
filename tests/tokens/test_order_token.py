"""TestDirectionToken."""
import unittest

from src.tokens.order_token import OrderToken
from tests.tokens.test_simple_token import TestSimpleToken


class TestOrderToken(TestSimpleToken):
    """Test cases for the OrderToken class."""

    def setUp(self):
        """Set up example tokens specific for testing OrderToken."""
        super().setUp()
        self.token = OrderToken()
        self.representation = "OrderToken()"
        self.pattern = r'(?P<order>[IDU])'
        self.name = 'Order'
        self.good = ['I', 'D', 'U']
        self.bad = ['X', '0', '1']
        self.backus_naur = '<Order>'
        self.result = {'order': 'I'}


if __name__ == "__main__":
    unittest.main()
