"""CellPairEqualValueParser."""
import re

from src.parsers.parser import Parser
from src.tokens.cell_token import CellToken
from src.tokens.symbols import DashToken, EqualsToken
from src.tokens.token import Token
from src.tokens.value_token import ValueToken
from src.utils.sudoku_exception import SudokuError


class CellPairEqualValueParser(Parser):
    """Parser for cell pair equal number format, such as 'r1c1-r2c2=dd'."""

    token: Token = CellToken() + DashToken() + CellToken() + EqualsToken() + ValueToken()

    def parse(self, text: str) -> dict:
        """Parse the input text for the cell pair equal number format.

        Args:
            text (str): The input text to be parsed

        Returns:
            dict: A dictionary containing the parsed data.
        """
        match = re.fullmatch(self.token.pattern, text)
        if match is None:
            raise SudokuError(f'Could not parse {text!r}')
        lhs_text: str
        rhs_text: str
        cell1_text: str
        cell2_text: str

        if CellPairEqualValueParser.token.parse(text) is None:
            raise SudokuError(f'Could not parse {text!r}')

        lhs_text, rhs_text = text.split('=')
        cell1_text, cell2_text = lhs_text.split('-')
        return {
            'CellPairValue':
                {
                    'Cell1': CellToken().parse(cell1_text),
                    'Cell2': CellToken().parse(cell2_text),
                    'Value': ValueToken().parse(rhs_text)['value'],
                }
        }
