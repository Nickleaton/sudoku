"""RossiniParser."""
from src.board.board import Board
from src.parsers.parser import Parser, ParserError
from src.tokens.cycle_token import CycleToken
from src.tokens.digit_token import DigitToken
from src.tokens.side_token import SideToken
from src.tokens.symbols import EqualsToken


class RossiniParser(Parser):
    """Parser for Rossini format: '[TLBR]d=[DIU]'."""

    def __init__(self):
        """Initialize the RossiniParser with start regex pattern for the Rossini format."""
        super().__init__(pattern=r'^[TLBR]\d=[DIU]$', example_format='[TLBR]d=[DIU]')
        self.token = SideToken() + DigitToken() + EqualsToken() + CycleToken()

    def parse(self, text: str) -> None:
        """Parse the input text to extract components in the Rossini format.

        Args:
            text (str): The input text expected to be in the format '[TLBR]d=[DIU]'.

        Raises:
            ParserError: If the input text does not match the expected format.
        """
        # Check if the input text matches the defined regular expression pattern.
        if not self.regular_expression.match(text):
            raise ParserError(f'{self.__class__.__name__} expects format like "[TLBR]d=[DIU]"')

        # Extract the components: side, index, and direction.
        side = text[0]  # 'T', 'L', 'B', or 'R'
        index = int(text[1])  # digit following the side
        direction = text[3]  # 'D', 'I', or 'U'

        # Store results in the parsed_data attribute.
        self.parsed_data = [side, index, direction]
        self.answer = {
            'side': side,
            'index': str(index),
            'direction': direction,
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
        return Parser.validate_side_index(board, input_data)
