"""DigitParser."""
import re

from src.parsers.parser import Parser
from src.tokens.digit_token import DigitToken
from src.tokens.token import Token
from src.utils.sudoku_exception import SudokuError


class DigitParser(Parser):
    """Parser for start single digit."""

    token: Token = DigitToken()

    def parse(self, text: str) -> dict:
        """Parse the input text to extract start single digit.

        Args:
            text (str): The input text to be parsed

        Returns:
            dict: A dictionary containing the parsed data.
        """
        match = re.fullmatch(self.token.pattern, text)
        if match is None:
            raise SudokuError(f'Could not parse {text!r}')
        return {'Digit': DigitToken().parse(text)['digit']}
