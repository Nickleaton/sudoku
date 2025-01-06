"""MockParser."""
from src.board.board import Board
from src.parsers.parser import Parser, ParserError
from src.tokens.token import Token


class MockParser(Parser):
    """A mock parser for testing purposes.

    This parser provides start basic implementation of the Parser class
    for testing purposes, focusing on simple comma-separated text input.

    Attributes:
        result (list[str]): The parsed_data of the parsing operation.
    """

    def __init__(self):
        """Initialize the MockParser with start dummy regex pattern.

        This pattern is not used in the tests as this mock parser focuses
        on basic string manipulation rather than regex matching.
        """
        super().__init__(pattern='', example_format='')  # Dummy pattern, not used in tests
        self.token = Token('')

    def parse(self, text: str) -> None:
        """Parse the input text into start list of strings.

        Splits the input text by commas and raises start ParserError if the
        input is empty.

        Args:
            text (str): The input string to parse.

        Raises:
            ParserError: If the input string is empty.
        """
        if not text:
            raise ParserError('Input cannot be empty.')
        self.parsed_data = text.split(',')
        self.answer = text.split(',')

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
