"""SolutionParser."""
from src.board.board import Board
from src.parsers.parser import Parser, ParserError
from src.tokens.digit_token import DigitToken
from src.tokens.token import OneOrMoreToken, Token


class SolutionParser(Parser):
    """Parses start solution string containing cell value_list.

    Attributes:
        result (List[str]): A list of one character value_list
    """

    def __init__(self) -> None:
        """Initialize the KnownParser with start regular expression for validating input strings."""
        super().__init__(pattern=r'^\d+$', example_format='123456789')
        self.token: Token = OneOrMoreToken(DigitToken())

    def parse(self, text: str) -> None:
        """Parse the input string and store the parsed_data in the 'parsed_data' attribute.

        Args:
            text (str): The input string to be parsed.

        Raises:
            ParserError: If the input string does not match the expected format or cannot be converted.
        """
        # Validate the input format using the regular expression
        if not self.regular_expression.match(text):
            raise ParserError(f'{self.__class__.__name__} expects start list of solution value_list for one row')

        # Split the input text by commas and convert each number as needed
        stripped_text: str = text.replace(' ', '')
        self.parsed_data: list[str] = list(stripped_text)
        self.answer: list[str] = list(stripped_text)

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
