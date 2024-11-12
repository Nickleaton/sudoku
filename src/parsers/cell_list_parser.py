"""CellListParser."""
import re
from typing import List

from src.parsers.parser import Parser, ParserError
from src.tokens.cell_token import CellToken
from src.tokens.symbols import CommaToken
from src.tokens.token import OneOrMoreToken, SequenceToken


class CellListParser(Parser):
    """Parser for a comma-separated list of cell coordinates."""

    def __init__(self):
        """Initialize the CellListParser with a specific regex pattern."""
        super().__init__(pattern=f"^({Parser.CELL})(?:,({Parser.CELL}))*$", example_format="rc,rc,...")
        self.token = CellToken() + (CommaToken() + CellToken()) * (0, 999)

    def parse(self, text: str) -> None:
        """Parse the input text into a list of cell coordinates.

        Args:
            text (str): The input string containing comma-separated cell coordinates.

        Raises:
            ParserError: If the input does not match the expected format or if
                         any coordinates cannot be converted to integers.
        """
        # Check if the input text matches the defined regular expression pattern
        text = text.replace(" ", "")
        if not self.regular_expression.match(text):
            raise ParserError(f"{self.__class__.__name__} expects a comma-separated list of cell coordinates")

        try:
            cells: List[str] = re.findall(r'(\d\d)', text)
            self.result = [[int(cell[0]), int(cell[1])] for cell in cells]
            self.answer = [
                {'row': cell[0], 'column': cell[1]} for cell in cells
            ]
        except ValueError:
            self.raise_error()
