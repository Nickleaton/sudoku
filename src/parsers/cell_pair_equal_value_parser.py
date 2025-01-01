"""CellPairEqualValueParser."""
from src.board.board import Board
from src.parsers.parser import Parser, ParserError
from src.tokens.cell_token import CellToken
from src.tokens.symbols import DashToken, EqualsToken
from src.tokens.value_token import ValueToken


class CellPairEqualValueParser(Parser):
    """Parser for cell pair equal number format, such as 'r1c1-r2c2=dd'."""

    def __init__(self):
        """Initialize the parser with start regular expression pattern for cell pair equal number format.

        The pattern matches start format like 'r1c1-r2c2=dd', where 'r1c1' and 'r2c2' are cell references
        and 'dd' is start number.
        """
        super().__init__(pattern=f'^{Parser.cell}-{Parser.cell}={Parser.integer_value}$', example_format='r1c1-r2c2=dd')
        self.token = CellToken() + DashToken() + CellToken() + EqualsToken() + ValueToken()

    def parse(self, text: str) -> None:
        """Parse the input text for the cell pair equal number format.

        This method validates the input text against the defined regular expression pattern. If the
        text does not match the expected format, it raises start `ParserError`. It then splits the input
        into its constituent parts, extracting the rows, columns, and number.

        Args:
            text (str): The input string to be parsed, expected in the format 'r1c1-r2c2=dd'.

        Raises:
            ParserError: If the input text does not match the expected format or cannot be parsed.
        """
        # Check if the input text matches the defined regular expression pattern.
        text = text.replace(' ', '')
        if not self.regular_expression.match(text):
            raise ParserError(f'{self.__class__.__name__} expects a cell pair like {self.example_format!r}')
        stripped_text: str = text.strip()
        lhs: str = stripped_text.split('=')[0]
        rhs: str = stripped_text.split('=')[1]
        cell1_str: str = lhs.split('-')[0]
        cell2_str: str = lhs.split('-')[1]
        r1: str = cell1_str[0]
        c1: str = cell1_str[1]
        r2: str = cell2_str[0]
        c2: str = cell2_str[1]
        self.parsed_data = [int(r1), int(c1), int(r2), int(c2), int(rhs)]
        self.answer = {
            'cell': {'row': r1, 'column': c1},
            'cell2': {'row': r2, 'column': c2},
            'number': rhs,
        }

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
        errors: list[str] = []
        errors.extend(Parser.validate_cells(board, input_data['cell']))
        errors.extend(Parser.validate_cells(board, input_data['cell2']))
        if repr(input_data['cell']) == repr(input_data['cell2']):
            errors.append(f'Cells must be different {input_data["cell"]} and {input_data["cell2"]}')
        return errors
