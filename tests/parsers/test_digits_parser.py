"""TestDigitsParser."""
import unittest
from typing import List, Tuple

from src.parsers.digits_parser import DigitsParser
from tests.parsers.test_parser import TestParser


class TestDigitsParser(TestParser):
    """Test case for the DigitsParser class."""

    def setUp(self):
        """Set up the DigitsParser instance for testing."""
        self.parser: DigitsParser = DigitsParser()
        self.representation: str = 'DigitsParser()'
        self.example_format: str = '1,2,3,...'
        self.valid_input_result: List[Tuple[str, List[str]]] = \
            [
                (
                    '1, 2, 3, 4, 6',
                    ['1', '2', '3', '4', '6']
                ),
                (
                    ' 1,    2,3  , 4,   7   ',
                    ['1', '2', '3', '4', '7']
                )
            ]
        self.valid_input_answer: List[Tuple[str, List[str]]] = \
            [
                (
                    '1, 2, 3, 4, 8',
                    ['1', '2', '3', '4', '8']
                ),
                (
                    ' 1,    2,3  , 4,   9   ',
                    ['1', '2', '3', '4', '9']
                )
            ]
        self.invalid_input: List[str] = \
            [
                '1, 2, start, 4',
                '1, 2, 3,',
                ', 1, 2, 3',
                '1, 2, 3, 4, 5, row',
                '10, 20, 30, 40, 50',
                'abc, def, ghi',
                ''
            ]


if __name__ == "__main__":
    unittest.main()
