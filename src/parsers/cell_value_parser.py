"""CellValueParser."""

import re

from src.parsers.parser import Parser
from src.tokens.cell_token import CellToken
from src.tokens.symbols import EqualsToken
from src.tokens.token import Token
from src.tokens.value_token import ValueToken
from src.utils.sudoku_exception import SudokuError


class CellValueParser(Parser):
    """Parser for Cell Value format: 'dd=d+' where dd are two digits and d+ is one or more digits."""

    token: Token = CellToken() + EqualsToken() + ValueToken()

    def parse(self, text: str) -> dict:
        """Parse the input text to extract cell number components.

        Args:
            text (str): The input text to be parsed

        Returns:
            dict: A dictionary containing the parsed data.
        """
        match = re.fullmatch(self.token.pattern, text)
        if match is None:
            raise SudokuError(f'Could not parse {text!r}')
        cell_text: str
        value_text: str
        cell_text, value_text = text.split('=')
        config: dict = {
            'CellValue':
                {
                    'Cell': CellToken().parse(cell_text),
                }
        }
        config['CellValue']['value'] = ValueToken().parse(value_text)['value']
        return config
