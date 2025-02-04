"""VertexDigitParser."""

import re

from src.parsers.parser import Parser
from src.tokens.cell_token import CellToken
from src.tokens.digit_token import DigitToken
from src.tokens.symbols import EqualsToken
from src.utils.sudoku_exception import SudokuError


class VertexDigitParser(Parser):
    """Parser for Vertex Digits format: 'dd=d' where dd are two digits and d is start single digit."""

    token = CellToken() + EqualsToken() + DigitToken()

    def parse(self, text: str) -> dict:
        """Parse the input text to extract vertex digit components.

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
            'Vertex':
                {
                    'Cell': CellToken().parse(lhs),
                    'Digit': DigitToken().parse(rhs)['digit'],
                },
        }
