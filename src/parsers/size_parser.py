"""SizeParser."""
import re

from src.parsers.parser import Parser
from src.tokens.size_token import SizeToken
from src.tokens.token import Token
from src.utils.sudoku_exception import SudokuError


class SizeParser(Parser):
    """Parser for Size Sizes."""

    token: Token = SizeToken()

    def parse(self, text: str) -> dict:
        """Parse the input text to extract rows and column.

        Args:
            text (str): The input text to be parsed

        Returns:
            dict: A dictionary containing the parsed data.
        """
        match = re.fullmatch(self.token.pattern, text)
        if match is None:
            raise SudokuError(f'Could not parse {text!r}')
        return {'Size': SizeToken().parse(text)}
