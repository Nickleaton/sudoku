"""TestDirectionToken."""
import unittest

from src.tokens.cycle_token import CycleToken
from tests.tokens.test_simple_token import TestSimpleToken


class TestCycleToken(TestSimpleToken):
    """Test cases for the CycleToken class."""

    def setUp(self):
        """Set up example tokens specific for testing CycleToken."""
        super().setUp()
        self.token = CycleToken()
        self.representation = "CycleToken()"
        self.pattern = r"(?P<cycle>[CA])"
        self.name = 'Cycle'
        self.good = ['C', 'A']
        self.bad = ['X', '0', '1']
        self.backus_naur = '<Cycle>'
        self.result = {'cycle': 'C'}


if __name__ == "__main__":
    unittest.main()
