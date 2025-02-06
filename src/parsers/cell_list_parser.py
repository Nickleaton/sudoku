"""CellListParser."""

import re

from src.parsers.parser import Parser
from src.tokens.cell_token import CellToken
from src.tokens.symbols import CommaToken
from src.tokens.token import Token, ZeroOrMoreToken
from src.utils.sudoku_exception import SudokuError


class CellListParser(Parser):
    """Parser for a comma-separated list of cell coordinates."""

    token: Token = CellToken() + ZeroOrMoreToken(CommaToken() + CellToken())

    def parse(self, text: str) -> dict[str, list]:
        """Parse a comma-separated list of cell coordinates.

        Args:
            text (str): The input text to be parsed

        Returns:
            dict: A dictionary containing the parsed data.

        Raises:
            SudokuError: If the input text cannot be parsed
        """
        match = re.fullmatch(self.token.pattern, text)
        if match is None:
            raise SudokuError(f'Could not parse {text!r}')
        cells: dict[str, list] = {'CellList': []}
        for part in text.split(','):
            try:
                cells['CellList'].append({'Cell': CellToken().parse(part)})
            except SudokuError as exp:
                raise SudokuError(f'Could not parse {part!r}') from exp
        return cells
