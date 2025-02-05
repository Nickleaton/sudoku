"""TestDirectionToken."""
import unittest

from src.tokens.direction_token import DirectionToken
from tests.tokens.test_simple_token import TestSimpleToken


class TestDirectionToken(TestSimpleToken):
    """Test cases for the DirectionToken class."""

    def setUp(self):
        """Set up example tokens specific for testing DirectionToken."""
        super().setUp()
        self.token = DirectionToken()
        self.representation = "DirectionToken()"
        self.pattern = r"(?P<direction>(?!UD|DU|LR|RL)(UR|UL|DL|DR|U|D|L|R))"  # Regex for direction values
        self.name = 'Direction'
        self.good = [
            ('UL', {'direction': 'UL'}),
            ('U', {'direction': 'U'}),
            ('UR', {'direction': 'UR'}),
            ('L', {'direction': 'L'}),
            ('R', {'direction': 'R'}),
            ('DL', {'direction': 'DL'}),
            ('D', {'direction': 'D'}),
            ('DR', {'direction': 'DR'})
        ]
        self.bad = ['X', '0', '1', 'LR', 'UD', 'DU', 'RL']
        self.backus_naur = '<Direction>'
        self.result = {'direction': 'UL'}  # Example of matching direction


if __name__ == "__main__":
    unittest.main()
