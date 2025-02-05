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
        self.good = [
            ('12', {'row': 1, 'col': 2}),
            ('11', {'row': 1, 'col': 1}),
            ('13', {'row': 1, 'col': 3}),
            ('21', {'row': 2, 'col': 1}),
            ('22', {'row': 2, 'col': 2}),
            ('23', {'row': 2, 'col': 3}),
            ('31', {'row': 3, 'col': 1}),
            ('32', {'row': 3, 'col': 2}),
            ('33', {'row': 3, 'col': 3}),
        ]
        self.bad = ['row', 'XX']
        self.backus_naur = '<Cell>'
        self.result = {'row': 1, 'col': 2}


if __name__ == "__main__":
    unittest.main()
