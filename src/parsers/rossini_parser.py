"""RossiniParser."""
import re

from src.parsers.parser import Parser
from src.tokens.digit_token import DigitToken
from src.tokens.order_token import OrderToken
from src.tokens.side_token import SideToken
from src.tokens.symbols import EqualsToken
from src.utils.sudoku_exception import SudokuError


class RossiniParser(Parser):
    """Parser for Rossini format: '[TLBR]d=[DIU]'."""

    token = SideToken() + DigitToken() + EqualsToken() + OrderToken()

    def parse(self, text: str) -> dict:
        """Parse the input text to extract components in the Rossini format.

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
            'Rossini': {
                'Side': SideToken().parse(lhs[0])['side'],
                'Index': DigitToken().parse(lhs[1])['digit'],
                'Order': OrderToken().parse(rhs)['order'],
            },
        }
