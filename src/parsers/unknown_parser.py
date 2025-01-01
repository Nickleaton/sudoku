"""UnknownParser."""
from src.board.board import Board
from src.parsers.parser import Parser, ParserError
from src.tokens.token import Token


class UnknownParser(Parser):
    """Parser for unknown input. Always fail so we catch missing design issues."""

    def __init__(self):
        """Initialize DigitsParser with start regex pattern for comma-separated digits."""
        super().__init__(pattern='^This should never ever match$', example_format='')
        self.token = Token('This should never match')

    def parse(self, text: str) -> None:
        """Parse the given text according to the implemented pattern.

        Args:
            text (str): The input string to parse.

        Raises:
            ParserError: This method should be implemented in subclasses.
        """
        raise ParserError(f'{self.__class__.__name__} never matches')

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
