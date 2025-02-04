"""CellPairsParser."""

import re

from src.parsers.parser import Parser
from src.tokens.cell_token import CellToken
from src.tokens.symbols import DashToken
from src.tokens.token import Token
from src.utils.sudoku_exception import SudokuError


class CellPairsParser(Parser):
    """Parser for handling cell pair references in the format '12-34'."""

    token: Token = CellToken() + DashToken() + CellToken()

    def parse(self, text: str) -> dict:
        """Parse the input text to extract cell references.

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
        # Check if the input text matches the defined regular expression pattern.
        cell1_text: str
        cell2_text: str

        cell1_text, cell2_text = text.split('-')
        return {
            'CellPair': {
                'Cell1': CellToken().parse(cell1_text),
                'Cell2': CellToken().parse(cell2_text),
            },
        }
