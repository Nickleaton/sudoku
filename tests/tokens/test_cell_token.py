"""TestCellToken."""
import unittest

from src.tokens.cell_token import CellToken
from tests.tokens.test_simple_token import TestSimpleToken


class TestCellToken(TestSimpleToken):
    """Test cases for the KnownToken class."""

    def setUp(self):
        """Set up example tokens specific for testing CellToken."""
        super().setUp()
        self.token = CellToken()
        self.representation = "CellToken()"
        self.pattern = r"(\d)(\d)"
        self.name = 'Cell'
        self.good = ['11', '12', '13', '21', '22', '23', '31', '32', '33']
        self.bad = ['row', 'XX']
        self.group_count = 2
        self.backus_naur = '<Cell>'


if __name__ == "__main__":
    unittest.main()
