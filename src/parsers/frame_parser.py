"""FrameParser."""

import re

from src.parsers.parser import Parser
from src.tokens.digit_token import DigitToken
from src.tokens.side_token import SideToken
from src.tokens.symbols import EqualsToken
from src.tokens.token import Token
from src.tokens.value_token import ValueToken
from src.utils.sudoku_exception import SudokuError


class FrameParser(Parser):
    """Parser for extracting side, index, and number from start string format like 'T1=2'."""

    token: Token = SideToken() + DigitToken() + EqualsToken() + ValueToken()

    def parse(self, text: str) -> dict:
        """Parse the input string to extract side, index, and integer number.

        Args:
            text (str): The input text to be parsed

        Returns:
            dict: A dictionary containing the parsed data.

        Raises:
            SudokuError: If the input text cannot be parsed.
        """
        match = re.fullmatch(self.token.pattern, text)
        if match is None:
            raise SudokuError(f'Could not parse {text!r}')
        lhs: str
        rhs: str
        lhs, rhs = text.split('=')
        return {
            'Frame': {
                'Index': DigitToken().parse(lhs[1])['digit'],
                'Side': SideToken().parse(lhs[0])['side'],
                'Value': ValueToken().parse(rhs)['value'],
            },
        }
