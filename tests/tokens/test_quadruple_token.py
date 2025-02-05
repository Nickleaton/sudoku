"""TestQuadrupleToken."""
import unittest

from src.tokens.quadruple_token import QuadrupleToken
from tests.tokens.test_simple_token import TestSimpleToken


class TestQuadToken(TestSimpleToken):
    """Test cases for the SideToken class."""

    def setUp(self):
        """Set up example tokens specific for testing QuadrupleToken."""
        super().setUp()
        self.token = QuadrupleToken()
        self.representation = 'QuadrupleToken()'
        self.pattern = r'(?P<quads>[\d]{0,4})'
        self.name = 'Quadruple'
        self.good = [
            ('123', {'quads': ['1', '2', '3']}),
            ('12', {'quads': ['1', '2']}),
            ('1122', {'quads': ['1', '1', '2', '2']}),
            ('12', {'quads': ['1', '2']})
        ]
        self.bad = ['12345', 'X']
        self.backus_naur = '<Quadruple>'
        self.result = {'quads': ['1', '2', '3']}


if __name__ == "__main__":
    unittest.main()
