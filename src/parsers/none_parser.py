"""NoneParser."""
from src.board.board import Board
from src.parsers.parser import Parser, ParserError
from src.tokens.token import Token


class NoneParser(Parser):
    """Parser for validating empty input text."""

    def __init__(self):
        """Initialize the NoneParser with an empty pattern to match."""
        super().__init__(pattern='^$', example_format='')
        self.token = Token('')

    def parse(self, text: str) -> None:
        """Parse the input text, ensuring it is empty.

        Args:
            text (str): The input text, expected to be empty.

        Raises:
            ParserError: If the input text is not empty.
        """
        # Check if text is empty; raise ParserError if not
        if text != '':
            raise ParserError(f'{self.__class__.__name__} expects nothing')
        raise ParserError(f'{self.__class__.__name__} expects nothing')

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
        if input_data:
            return [f'Expecting None, got {input_data!r}']
        return []
