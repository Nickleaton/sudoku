from src.parsers.parser import Parser, ParserError


class QuadruplesParser(Parser):
    """Parser for quadruples in the format 'dd=ddd' where d is a digit and '?' is allowed."""

    def __init__(self):
        """Initializes the QuadruplesParser with a regex pattern for the quadruples format."""
        super().__init__(r'^\d{2}=[\d?]+$')

    def parse(self, text: str) -> None:
        """Parses the input text to extract quadruple components.

        Args:
            text (str): The input text expected to be in the format 'dd=ddd'.

        Raises:
            ParserError: If the input text does not match the expected format
                          or if conversion to integers fails.
        """
        # Check if the input text matches the defined regular expression pattern.
        if not self.regular_expression.match(text):
            raise ParserError(f"{self.__class__.__name__} expects a format like 'dd=ddd'")

        try:
            # Split the input string into components based on '='
            left, right = text.split('=')
            # Store results: left should be two digits, right can be digits or '?'.
            self.result = [int(left.strip()), right.strip()]
        except ValueError:
            # If any of the values cannot be converted, clear the result and raise an error.
            self.result = None
            raise ParserError(f"{self.__class__.__name__} expects a format like 'dd=ddd'")
