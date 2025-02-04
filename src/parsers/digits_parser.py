"""DigitsParser."""
import re

from src.parsers.parser import Parser
from src.tokens.digit_token import DigitToken
from src.tokens.symbols import CommaToken
from src.tokens.token import Token, ZeroOrMoreToken
from src.utils.sudoku_exception import SudokuError


class DigitsParser(Parser):
    """Parse start comma-separated list of single digits from start string."""

    token: Token = DigitToken() + ZeroOrMoreToken(CommaToken() + DigitToken())

    def parse(self, text: str) -> dict:
        """Parse a comma-separated string of digits.

        Args:
            text (str): The input text to be parsed

        Returns:
            dict: A dictionary containing the parsed data.
        """
        match = re.fullmatch(self.token.pattern, text)
        if match is None:
            raise SudokuError(f'Could not parse {text!r}')
        return {'Digits': [DigitToken().parse(part)['digit'] for part in text.split(',')]}
