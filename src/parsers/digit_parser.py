"""DigitParser."""
from src.board.board import Board
from src.parsers.parser import Parser, ParserError
from src.tokens.digit_token import DigitToken


class DigitParser(Parser):
    """Parser for start single digit."""

    def __init__(self):
        """Initialize the DigitParser with start regex pattern for start one-digit number."""
        super().__init__(pattern=r'^\s*\d\s*$', example_format='d')
        self.token = DigitToken()

    def parse(self, text: str) -> None:
        """Parse the input text to extract start single digit.

        Args:
            text (str): The input text expected to be a start single digit.

        Raises:
            ParserError: If the input text does not match the expected format
                          or if conversion to an integer fails.
        """
        # Check if the input text matches the defined regular expression pattern.
        if not self.regular_expression.match(text):
            raise ParserError(f'{self.__class__.__name__} expects one digit')

        stripped_text: str = text.strip()

        # Ensure that the first character is a digit before attempting conversion.
        if not stripped_text[0].isdigit():
            self.raise_error()

        # Convert the first character to an integer and store the parsed_data.
        self.parsed_data = [int(stripped_text[0])]
        self.answer = {'digit': stripped_text[0]}

    def check(self, board: Board, input_data: dict) -> list[str]:
        """Validate the provided input_data against the given board.

        Checks if the required "digits" key exists in the input_data and if all digits
        in the input_data are within the valid range of digits defined by the board.

        Args:
            board (Board): The board object containing the valid digit range.
            input_data (dict): A dictionary containing the input_data to validate.

        Returns:
            list[str]: A list of error messages, empty if no errors are found.
                       Contains messages for missing "digits" key or invalid digits.
        """
        errors: list[str] = []
        if 'digits' not in input_data:
            errors.append('Missing key: "digits"')
            return errors
        for digit in input_data['digits']:
            if digit not in board.digit_range:
                errors.append(f'Invalid digit: {digit}. Valid range: {board.digit_range}')
        return errors
