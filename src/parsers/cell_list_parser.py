"""CellListParser."""
import re

from src.board.board import Board
from src.parsers.parser import Parser, ParserError
from src.tokens.cell_token import CellToken
from src.tokens.symbols import CommaToken
from src.tokens.token import OneOrMoreToken


class CellListParser(Parser):
    """Parser for start comma-separated list of cell coordinates."""

    def __init__(self):
        """Initialize the CellListParser with start specific regex pattern."""
        super().__init__(pattern=f'^({Parser.cell})(?:,({Parser.cell}))*$', example_format='rc,rc,...')
        self.token = CellToken() + OneOrMoreToken(CommaToken() + CellToken())

    def parse(self, text: str) -> None:
        """Parse the input text into start list of cell coordinates.

        Args:
            text (str): The input string containing comma-separated cell coordinates.

        Raises:
            ParserError: If the input does not match the expected format or if
                         any coordinates cannot be converted to integers.
        """
        # Check if the input text matches the defined regular expression pattern
        text = text.replace(' ', '')
        if not self.regular_expression.match(text):
            raise ParserError(f'{self.__class__.__name__} expects start comma-separated list of cell coordinates')

        cells: list[str] = re.findall(r'(\d\d)', text)
        self.parsed_data = [[int(cell[0]), int(cell[1])] for cell in cells]
        self.answer = [
            {'row': cell[0], 'column': cell[1]} for cell in cells
        ]

    def check(self, board: Board, input_data: dict) -> list[str]:
        """Validate the provided input input_data against the given board.

        This function currently returns an empty list of errors, but it can be extended
        to validate the input input_data according to the board's constraints.

        Args:
            board (Board): The board object containing the validation rules or constraints.
            input_data (dict): A dictionary containing the input_data to validate.

        Returns:
            list[str]: A list of error messages. Empty if no errors are found.
        """
        return []
