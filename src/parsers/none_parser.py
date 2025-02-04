"""NoneParser."""
import re

from src.parsers.parser import Parser
from src.tokens.token import Token
from src.utils.sudoku_exception import SudokuError


class NoneParser(Parser):
    """Parser for validating empty input text."""

    token: Token = Token('')

    def parse(self, text: str) -> dict:
        """Parse the input text, ensuring it is empty.

        Args:
            text (str): The input text to be parsed

        Returns:
            dict: A dictionary containing the parsed data.
        """
        match = re.fullmatch(self.token.pattern, text)
        if match is None:
            raise SudokuError(f'Could not parse {text!r}')
        return {}
