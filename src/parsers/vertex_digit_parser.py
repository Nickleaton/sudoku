from src.parsers.parser import Parser, ParserError


class VertexDigitParser(Parser):
    """Parser for Vertex Digit format: 'dd=d' where dd are two digits and d is a single digit."""

    def __init__(self):
        """Initializes the VertexDigitParser with a regex pattern for the Vertex Digit format."""
        super().__init__(r'^\d{2}=\d$')

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

        # Split the text at the equals sign to extract components.
        index, value = text.split('=')
        index = [int(index[0]), int(index[1])]  # Convert the two digits to integers
        value = int(value)  # Convert the right side of the equals sign to an integer

        # Store results in the result attribute.
        self.result = [index, value]
