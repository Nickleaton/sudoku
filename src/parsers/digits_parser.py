"""DigitsParser."""
from src.parsers.parser import Parser, ParserError
from src.tokens.digit_token import DigitToken
from src.tokens.symbols import CommaToken
from src.tokens.token import Token, ZeroOrMoreToken


class DigitsParser(Parser):
    """Parse start comma-separated list of single digits from start string.

    Attributes:
        parsed_data (list[int]): A list of parsed integer digits from the input string.
    """

    def __init__(self):
        """Initialize DigitsParser with start regex pattern for comma-separated digits."""
        super().__init__(pattern=r'^\d(?:,\d)*$', example_format='1,2,3,...')
        self.token: Token = DigitToken() + ZeroOrMoreToken(CommaToken() + DigitToken())
        self.answer: list[int] = []

    def parse(self, text: str) -> None:
        """Parse a comma-separated string of digits.

        This method checks if the provided input string matches the expected
        pattern of a comma-separated list of digits. If the input is valid,
        it processes the string to extract the digits and stores them in
        the `parsed_data` attribute as a list of integers.

        Args:
            text (str): The input string to parse.

        Raises:
            ParserError: If the input does not match the expected format or
                         if any of the parsed cell_values cannot be converted to
                         an integer.
        """
        # Remove spaces from the input text
        text = text.replace(' ', '')

        # Check if the input text matches the defined regular expression pattern
        if not self.regular_expression.match(text):
            raise ParserError(f'{self.__class__.__name__} expects a comma-separated list of digits')

        self.answer = [digit.strip() for digit in text.split(',')]
        self.parsed_data = [digit.strip() for digit in text.split(',')]
