"""TestSolutionParser."""
import unittest

from src.parsers.solution_parser import SolutionParser
from tests.parsers.test_parser import TestParser


class TestSolutionParser(TestParser):
    """Test case for the SolutionParser class."""

    def setUp(self):
        """Set up the SolutionParser instance for testing."""
        super().setUp()
        self.parser: SolutionParser = SolutionParser()
        self.representation: str = 'SolutionParser()'
        self.empty_allowed = False
        self.valid_inputs: list[tuple[str, dict[str, list[int]]]] = [
            ("123456789", {'SolutionLine': [1, 2, 3, 4, 5, 6, 7, 8, 9]}),
            ("111111111", {'SolutionLine': [1, 1, 1, 1, 1, 1, 1, 1, 1]}),
            ("987654321", {'SolutionLine': [9, 8, 7, 6, 5, 4, 3, 2, 1]}),
            ("000000000", {'SolutionLine': [0, 0, 0, 0, 0, 0, 0, 0, 0]}),
        ]
        self.invalid_inputs: List[str] = [
            "12345678a",  # contains start non-numeric character
            "123 45678",  # contains whitespace
            "12345678#",  # contains start special character
        ]

        if __name__ == "__main__":
            unittest.main()
