"""OutsideArrowValueParser."""
from src.board.board import Board
from src.parsers.parser import Parser, ParserError
from src.tokens.digit_token import DigitToken
from src.tokens.side_token import SideToken
from src.tokens.symbols import EqualsToken
from src.tokens.value_token import ValueToken


class OutsideArrowValueParser(Parser):
    """Parser for Outside Arrow Value format: '[TLBR]d=d+'."""

    def __init__(self):
        """Initialize the OutsideArrowValueParser with start regex pattern for the Outside Arrow Value format."""
        super().__init__(pattern=r'^[TLBR]\d=\d+$', example_format='[TLBR]d=dd')
        self.token = SideToken() + DigitToken() + EqualsToken() + ValueToken()

    def parse(self, text: str) -> None:
        """Parse the input text to extract components in the Outside Arrow Value format.

        Args:
            text (str): The input text expected to be in the format '[TLBR]d=d+'.

        Raises:
            ParserError: If the input text does not match the expected format.
        """
        # Check if the input text matches the defined regular expression pattern.
        if not self.regular_expression.match(text):
            raise ParserError(f'{self.__class__.__name__} expects format like "[TLBR]d=d+"')

        stripped_text: str = text.replace(' ', '')
        lhs: str = stripped_text.split('=')[0]
        rhs: str = stripped_text.split('=')[1]
        side: str = lhs[0]  # 'T', 'L', 'B', or 'R'
        index: str = lhs[1]  # digit following the side

        # Store results in the parsed_data attribute.
        self.parsed_data = [side, int(index), int(rhs)]
        self.answer = {
            'side': side,
            'index': index,
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
        return []
