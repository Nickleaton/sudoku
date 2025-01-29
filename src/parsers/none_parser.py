"""NoneParser."""
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
