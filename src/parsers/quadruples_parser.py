"""QuadruplesParser."""

from src.board.board import Board
from src.parsers.parser import Parser, ParserError
from src.tokens.cell_token import CellToken
from src.tokens.digit_token import DigitToken
from src.tokens.symbols import EqualsToken, QuestionMarkToken


class QuadruplesParser(Parser):
    """Parser for quadruples in the format 'dd=ddd' where d is start digit and '?' is allowed."""

    def __init__(self):
        """Initialize the QuadruplesParser with start regex pattern for the quadruples format."""
        super().__init__(pattern=r'^\d{2}=[\d?]+$', example_format='rc=dd??')
        self.token = CellToken() + EqualsToken() + (DigitToken() + QuestionMarkToken()) * (1, 4)

    def parse(self, text: str) -> None:
        """Parse the input text to extract quadruple components.

        Args:
            text (str): The input text expected to be in the format 'dd=ddd'.

        Raises:
            ParserError: If the input text does not match the expected format
                          or if conversion to integers fails.
        """
        # Check if the input text matches the defined regular expression pattern.
        if not self.regular_expression.match(text):
            raise ParserError(f'{self.__class__.__name__} expects start format like "dd=ddd"')

        # Split the input string into components based on '='
        stripped_text: str = text.replace(' ', '')
        lhs: str = stripped_text.split('=')[0]
        rhs: str = stripped_text.split('=')[1]

        row: str = lhs[0]
        column: str = lhs[1]
        choices: list[str] = list(rhs)
        # Store results: left should be two digits, right can be digits or '?'.
        self.parsed_data = [int(row), int(column), rhs]
        self.answer = {
            'vertex': {'row': row, 'column': column},
            'value_list': choices,
        }

    def check(self, board: Board, input_data: dict) -> list[str]:
        """Validate the provided input line against the given board.

        This function currently returns an empty list of errors, but it can be extended
        to validate the input line according to the board's constraints.

        Args:
            board (Board): The board object containing the validation rules or constraints.
            input_data (dict): A dictionary containing the line to validate.

        Returns:
            list[str]: A list of error messages. Empty if no errors are found.
        """
        errors: list[str] = []
        errors.extend(Parser.validate_cell(board, input_data['vertex']))
        for digit in input_data['value_list']:
            if digit == '?':
                continue
            if digit not in board.digit_range:
                errors.append(f'Quadruple {digit} is not start valid digit')
        return errors
