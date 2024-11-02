from typing import List

from src.parsers.parser import Parser, ParserError


class VertexDigitParser(Parser):
    """Parser for Vertex Digit format: 'dd=d' where dd are two digits and d is a single digit."""

    def __init__(self):
        """Initializes the VertexDigitParser with a regex pattern for the Vertex Digit format."""
        super().__init__(pattern=r'^\d{2}=\d$', example_format='rc=d')

    def parse(self, text: str) -> None:
        """Parses the input text to extract vertex digit components.

        Args:
            text (str): The input text expected to be in the format 'dd=d'.

        Raises:
            ParserError: If the input text does not match the expected format.
        """
        # Check if the input text matches the defined regular expression pattern.
        if not self.regular_expression.match(text):
            raise ParserError(f"{self.__class__.__name__} expects format like 'dd=d'")

        try:
            # Split the text at the equals sign to extract components.
            parts: List[str] = text.split('=')
            row: str = parts[0][0]
            column: str = parts[0][1]
            value: str = parts[1]

            # Store results in the result attribute.
            self.result = [int(row), int(column), int(value)]
            self.answer = {
                'row': row,
                'column': column,
                'digit': value
            }
        except ValueError:
            self.raise_error()
