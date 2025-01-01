"""LittleKillerParser."""
from src.board.board import Board
from src.parsers.parser import Parser, ParserError
from src.tokens.cycle_token import CycleToken
from src.tokens.digit_token import DigitToken
from src.tokens.side_token import SideToken
from src.tokens.symbols import EqualsToken
from src.tokens.value_token import ValueToken


class LittleKillerParser(Parser):
    """Parser for the Little Killers format."""

    def __init__(self):
        """Initialize the LittleKillerParser with start regex pattern for valid input formats."""
        super().__init__(pattern=r'^\s*[TLBR]\s*\d\s*[C|A]\s*=\s*\d+\s*$', example_format='[TLBR]i=dd')
        self.token = SideToken() + DigitToken() + CycleToken() + EqualsToken() + ValueToken()

    def parse(self, text: str) -> None:
        """Parse the input text to extract components of the Little Killers format.

        Args:
            text (str): The input text expected to be in the format 'T1C=2' or similar.

            First letter is T, L, B, or R corresponding to the side of the board, Top, Left, Right or Bottom.
            Second number is the index of the cell. Column or row index
            Third letter is C or A corresponding to the direction of the cell, Clockwise or Anticlockwise.
            Last number is the number depending on the constraint

        Raises:
            ParserError: If the input text does not match the expected format
                          or if conversion to integers fails.
        """
        # Check if the input text matches the defined regular expression pattern.
        if not self.regular_expression.match(text):
            raise ParserError(f'{self.__class__.__name__} expects input in the format "T1C=2" or similar')

        # Remove whitespace from the input text.
        stripped_text: str = text.replace(' ', '')

        # Extract the components based on the specified format.
        side: str = stripped_text[0]  # The first character (T, L, B, R)
        index: str = stripped_text[1]  # The second character as an integer index
        cycle: str = stripped_text[2]  # The third character (C or A)
        target: str = stripped_text.split('=')[1]  # The number after '='

        # Store the extracted components in the parsed_data attribute.
        self.parsed_data = [side, int(index), cycle, int(target)]
        self.answer = {
            'side': side,
            'index': index,
            'cycle': cycle,
            'number': target,
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
