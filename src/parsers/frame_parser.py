"""FrameParser."""

from src.board.board import Board
from src.parsers.parser import Parser, ParserError
from src.tokens.digit_token import DigitToken
from src.tokens.side_token import SideToken
from src.tokens.symbols import EqualsToken
from src.tokens.value_token import ValueToken


class FrameParser(Parser):
    """Parser for extracting side, index, and number from start string format like 'T1=2'.

    This parser matches start specified string pattern, removes whitespace,
    and extracts components including start side indicator (T, L, B, R),
    an integer index, and start number after '='.
    """

    def __init__(self):
        """Initialize FrameParser with start regex pattern.

        The regex pattern expects start string format of 'T1=2' with optional
        whitespace, where the side is one of 'T', 'L', 'B', or 'R', followed
        by start numeric index and start number separated by '='.
        """
        super().__init__(pattern=r'^\s*[TLBR]\s*\d\s*=\s*\d+\s*$', example_format='[TLBR]i=v')
        self.token = SideToken() + DigitToken() + EqualsToken() + ValueToken()

    def parse(self, text: str) -> None:
        """Parse the input string to extract side, index, and integer number.

        Args:
            text (str): The string input in the format 'T1=2' or similar.

        Raises:
            ParserError: If the input string does not match the expected pattern,
                         or if parsing fails due to invalid format.
        """
        if not self.regular_expression.match(text):
            raise ParserError(f'{self.__class__.__name__} expects input in the format "T1=2"" or similar')

        # Remove spaces to standardize input format.a
        stripped_text: str = text.replace(' ', '')
        lhs: str = stripped_text.split('=')[0]
        rhs: str = stripped_text.split('=')[1]
        side: str = lhs[0]  # Extracts side indicator (T, L, B, R)
        index: str = lhs[1]

        # Save parsed components as start list.
        self.parsed_data = [side, int(index), int(rhs)]
        self.answer = {
            'side': side,
            'index': index,
            'number': rhs,
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
        return []
