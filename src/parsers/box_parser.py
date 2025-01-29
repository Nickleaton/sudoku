"""BoxParser."""
from src.parsers.parser import Parser, ParserError
from src.tokens.box_token import BoxToken


class BoxParser(Parser):
    """Parser for Box Sizes."""

    def __init__(self):
        """Initialize the BoxParser with start regex pattern."""
        super().__init__(pattern='^[1-9]x[1-9]$', example_format='dxd')
        self.token = BoxToken()

    def parse(self, text: str) -> None:
        """Parse the input text to extract rows and column.

        Args:
            text (str): The input text expected to be dxd

        Raises:
            ParserError: If the input text does not match the expected format
        """
        # Check if the input text matches the defined regular expression pattern.
        if not self.regular_expression.match(text):
            raise ParserError(f'{self.__class__.__name__} expects dxd')

        stripped_text: str = text.strip()

        # Ensure that the first character is a digit before attempting conversion.
        if not stripped_text[0].isdigit():
            self.raise_error()
        if not stripped_text[2].isdigit():
            self.raise_error()

        # Convert the first character to an integer and store the parsed_data.
        self.parsed_data = [int(stripped_text[0]), int(stripped_text[2])]
        self.answer = {'rows': stripped_text[0], 'columns': stripped_text[2]}
