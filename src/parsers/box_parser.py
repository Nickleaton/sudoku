"""BoxParser."""
import re

from src.parsers.parser import Parser
from src.tokens.box_token import BoxToken
from src.tokens.token import Token
from src.utils.sudoku_exception import SudokuError


class BoxParser(Parser):
    """Parser for Box Sizes."""

    token: Token = BoxToken()

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
        return {'Box': BoxParser.token.parse(text)}
