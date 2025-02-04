"""OutsideArrowValueParser."""
import re

from src.parsers.parser import Parser
from src.tokens.digit_token import DigitToken
from src.tokens.direction_token import DirectionToken
from src.tokens.side_token import SideToken
from src.tokens.symbols import EqualsToken
from src.tokens.token import Token
from src.tokens.value_token import ValueToken
from src.utils.sudoku_exception import SudokuError


class OutsideArrowValueParser(Parser):
    """Parser for Outside Arrow Value format: '[TLBR]d=d+'."""

    token: Token = SideToken() + DigitToken() + DirectionToken() + EqualsToken() + ValueToken()

    def parse(self, text: str) -> dict:
        """Parse the input text to extract components in the Outside Arrow Value format.

        Args:
            text (str): The input text to be parsed

        Returns:
            dict: A dictionary containing the parsed data.
        """
        match = re.fullmatch(self.token.pattern, text)
        if match is None:
            raise SudokuError(f'Could not parse {text!r}')
        lhs: str
        rhs: str
        lhs, rhs = text.split('=')

        return {
            'Arrow': {
                'Side': SideToken().parse(lhs[0])['side'],
                'Index': DigitToken().parse(lhs[1])['digit'],
                'Direction': DirectionToken().parse(lhs[2:])['direction'],
                'Value': ValueToken().parse(rhs)['value'],
            }
        }
