"""VertexValueParser."""

import re

from src.parsers.parser import Parser
from src.tokens.cell_token import CellToken
from src.tokens.symbols import EqualsToken
from src.tokens.token import Token
from src.tokens.value_token import ValueToken
from src.utils.sudoku_exception import SudokuError


class VertexValueParser(Parser):
    """Parser for Vertex Value format: 'dd=d' where dd are two digits and d is one or more digits."""

    token: Token = CellToken() + EqualsToken() + ValueToken()

    def parse(self, text: str) -> dict:
        """Parse the input text to extract vertex number components.

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
            'Vertex':
                {
                    'Cell': CellToken().parse(lhs),
                    'Value': ValueToken().parse(rhs)['value'],
                }
        }
