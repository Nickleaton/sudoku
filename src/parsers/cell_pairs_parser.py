"""CellPairsParser."""

from src.board.board import Board
from src.parsers.parser import Parser, ParserError
from src.tokens.cell_token import CellToken
from src.tokens.symbols import DashToken


class CellPairsParser(Parser):
    """Parser for handling cell pair references in the format '12-34'."""

    def __init__(self):
        """Initialize the CellPairsParser.

        Calls the parent class (Parser) constructor with a start regex pattern
        that matches the required format for cell pairs (e.g., '12-34').
        """
        super().__init__(pattern=r'^\s*\d\d\s*-\s*\d\d\s*$', example_format='r1c1=r2c2')
        self.token = CellToken() + DashToken() + CellToken()

    def parse(self, text: str) -> None:
        """Parse the input text to extract cell references.

        Args:
            text (str): The input text in the format 'XY-ZW' to be parsed.

        Raises:
            ParserError: If the input text does not match an integer format.
        """
        # Check if the input text matches the defined regular expression pattern.
        if not self.regular_expression.match(text):
            # Raise an error if the format is incorrect.
            raise ParserError(f'{self.__class__.__name__} expects cell reference equals cell reference, e.g., 12-34')

        # Strip spaces and extract row and column values.
        stripped_text: str = text.replace(' ', '')
        row1: str = stripped_text[0]
        col1: str = stripped_text[1]
        row2: str = stripped_text[3]
        col2: str = stripped_text[4]

        # Store the parsed data as a list of integers.
        self.parsed_data = [
            int(row1),
            int(col1),
            int(row2),
            int(col2),
        ]

        # Store the parsed cell data in a dictionary.
        self.answer = {
            'cell1': {'row': int(row1), 'column': int(col1)},
            'cell2': {'row': int(row2), 'column': int(col2)},
        }

    def check(self, board: Board, input_data: dict) -> list[str]:
        """Validate the provided line against the given board.

        Args:
            board (Board): The board object containing the validation rules or constraints.
            input_data (dict): A dictionary containing the input data to validate.

        Returns:
            list[str]: A list of error messages. Empty if no errors are found.
        """
        errors: list[str] = []

        # Validate both cells in the input data.
        errors.extend(Parser.validate_cells(board, input_data['cell']))
        errors.extend(Parser.validate_cells(board, input_data['cell2']))

        # Check if both cells are the same.
        if repr(input_data['cell']) == repr(input_data['cell2']):
            errors.append(f'Cells must be different: {input_data["cell"]} and {input_data["cell2"]}')

        return errors
