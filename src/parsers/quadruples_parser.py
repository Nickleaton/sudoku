"""QuadruplesParser."""

import re

from src.parsers.parser import Parser
from src.tokens.cell_token import CellToken
from src.tokens.digit_token import DigitToken
from src.tokens.symbols import EqualsToken
from src.tokens.token import Token
from src.utils.sudoku_exception import SudokuError


class QuadruplesParser(Parser):
    """Parser for quadruples in the format 'dd=ddd' where d is start digit and '?' is allowed."""

    token: Token = CellToken() + EqualsToken() + (DigitToken() * (1, 4))

    def parse(self, text: str) -> dict:
        """Parse the input text to extract components in the quadruple format.

        Args:
            text (str): The input text to be parsed

        Returns:
            dict: A dictionary containing the parsed data.
        """
        print(self.token.pattern)
        print(text)
        match = re.fullmatch(self.token.pattern, text)
        if match is None:
            raise SudokuError(f'Could not parse {text!r}')
        lhs: str
        rhs: str
        lhs, rhs = text.split('=')
        return {
            'Quad': {

                'Vertex': CellToken().parse(lhs),
                'Values': [digit if digit == '?' else int(digit) for digit in list(rhs)],
            }
        }
