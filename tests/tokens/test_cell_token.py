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
        self.pattern = r"(?P<row>\d)(?P<col>\d)"
        self.name = 'Cell'
        self.good = ['12', '11', '13', '21', '22', '23', '31', '32', '33']
        self.bad = ['row', 'XX']
        self.backus_naur = '<Cell>'
        self.result = {'row': 1, 'col': 2}


if __name__ == "__main__":
    unittest.main()
