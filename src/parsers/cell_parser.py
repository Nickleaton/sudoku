"""CellParser."""
import re

from src.parsers.parser import Parser
from src.tokens.cell_token import CellToken
from src.tokens.token import Token
from src.utils.sudoku_exception import SudokuError


class CellParser(Parser):
    """Parser for start two-digit cell reference."""

    token: Token = CellToken()

    def parse(self, text: str) -> dict:
        """Parse the input text to extract two-digit cell references.

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
        return {'Cell': CellToken().parse(text)}
