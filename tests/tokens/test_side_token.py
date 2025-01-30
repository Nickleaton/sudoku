"""TestSideToken."""
import unittest

from src.tokens.side_token import SideToken
from tests.tokens.test_simple_token import TestSimpleToken


class TestSideToken(TestSimpleToken):
    """Test cases for the SideToken class."""

    def setUp(self):
        """Set up example tokens specific for testing SideToken."""
        super().setUp()
        self.token = SideToken()  # Example SideToken
        self.representation = 'SideToken()'
        self.pattern = r'(?P<side>[TLBR])'
        self.name = 'Side'
        self.good = ['T', 'L', 'B', 'R']
        self.bad = ['X']
        self.backus_naur = '<Side>'
        self.result = {'side': 'T'}


if __name__ == "__main__":
    unittest.main()
