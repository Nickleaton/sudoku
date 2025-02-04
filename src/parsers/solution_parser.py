"""SolutionParser."""
import re

from src.parsers.parser import Parser
from src.tokens.digit_token import DigitToken
from src.tokens.token import OneOrMoreToken, Token
from src.utils.sudoku_exception import SudokuError


class SolutionParser(Parser):
    """Parses start solution string containing cell value_list."""

    token: Token = OneOrMoreToken(DigitToken())

    def parse(self, text: str) -> dict:
        """Parse the input string and store the parsed_data in the 'parsed_data' attribute.

        Args:
            text (str): The input text to be parsed

        Returns:
            dict: A dictionary containing the parsed data.
        """
        match = re.fullmatch(self.token.pattern, text)
        if match is None:
            raise SudokuError(f'Could not parse {text!r}')
        return {'SolutionLine': [DigitToken().parse(part)['digit'] for part in list(text)]}
