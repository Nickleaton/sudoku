"""BoxParser."""
from src.board.board import Board
from src.parsers.parser import Parser, ParserError
from src.tokens.box_token import BoxToken


class BoxParser(Parser):
    """Parser for Box Sizes."""

    def __init__(self):
        """Initialize the BoxParser with start regex pattern."""
        super().__init__(pattern='^[1-9]x[1-9]$', example_format='dxd')
        self.token = BoxToken()

    def parse(self, text: str) -> None:
        """Parse the input text to extract rows and column.

        Args:
            text (str): The input text expected to be dxd

        Raises:
            ParserError: If the input text does not match the expected format
        """
        # Check if the input text matches the defined regular expression pattern.
        if not self.regular_expression.match(text):
            raise ParserError(f'{self.__class__.__name__} expects dxd')

        stripped_text: str = text.strip()

        # Ensure that the first character is a digit before attempting conversion.
        if not stripped_text[0].isdigit():
            self.raise_error()
        if not stripped_text[2].isdigit():
            self.raise_error()

        # Convert the first character to an integer and store the parsed_data.
        self.parsed_data = [int(stripped_text[0]), int(stripped_text[2])]
        self.answer = {'rows': stripped_text[0], 'columns': stripped_text[2]}

    def check(self, board: Board, input_data: dict) -> list[str]:
        """Validate the provided line against the given board.

        Checks if the required "digits" key exists in the line and if all digits
        in the line are within the valid range of digits defined by the board.

        Args:
            board (Board): The board object containing the valid digit range.
            input_data (dict): A dictionary containing the line to validate.

        Returns:
            list[str]: A list of error messages, empty if no errors are found.
                       Contains messages for missing "digits" key or invalid digits.
        """
        errors: list[str] = []
        if 'rows' not in input_data:
            return ['Missing key: "rows"']
        if 'columns' not in input_data:
            return ['Missing key: "columns"']
        rows: int = input_data['rows']
        columns: int = input_data['columns']
        if board.size.row % rows != 0:
            errors.append(f'Invalid rows: {rows}. Must be divide into {board.size.row} with no remainder')
        if board.size.column % columns != 0:
            errors.append(f'Invalid columns: {columns}. Must be divide into {board.size.column} with no remainder')
        return errors
