from typing import List

from src.parsers.parser import Parser, ParserError


class CellListParser(Parser):
    """Parser for a comma-separated list of cell coordinates."""

    def __init__(self):
        """Initialize the CellListParser with a specific regex pattern."""
        super().__init__(pattern=r"^\s*\d\d\s*(?:,\s*\d\d\s*)*$", example_format="rc,rc,...")

    def parse(self, text: str) -> None:
        """Parse the input text into a list of cell coordinates.

        Args:
            text (str): The input string containing comma-separated cell coordinates.

        Raises:
            ParserError: If the input does not match the expected format or if
                         any coordinates cannot be converted to integers.
        """
        # Check if the input text matches the defined regular expression pattern
        if not self.regular_expression.match(text):
            raise ParserError(f"{self.__class__.__name__} expects a comma-separated list of cell coordinates")

        try:
            # Split the input text by commas, strip whitespace, and convert each
            # coordinate into a list of integers. The result is stored in the result attribute.
            cells: List[List[str]] = [[d.strip()[0], d.strip()[1]] for d in text.split(',')]
            self.result = [[int(cell[0]), int(cell[1])] for cell in cells]
            self.answer = [
                {'row': cell[0], 'column': cell[1]} for cell in cells
            ]
        except ValueError:
            self.raise_error()
