from src.parsers.parser import ParserError, Parser


class SolutionParser(Parser):
    """Parses a solution string containing cell velues

    Attributes:
        result (list[str]): A list of  one character values
    """

    def __init__(self):
        """Initializes the KnownParser with a regular expression for validating input strings.
        """
        super().__init__(r"^\d+$")

    def parse(self, text: str) -> None:
        """Parses the input string and stores the result in the 'result' attribute.

        Args:
            text (str): The input string to be parsed.

        Raises:
            ParserError: If the input string does not match the expected format or cannot be converted.
        """
        # Validate the input format using the regular expression
        if not self.regular_expression.match(text):
            raise ParserError(
                f"{self.__class__.__name__} expects a list of solution values for one row")

        try:
            # Split the input text by commas and convert each value as needed
            self.result = list(text.replace(" ",""))
        except ValueError as e:
            # Raise an error if any of the values cannot be converted to an integer
            self.result = None
            raise ParserError(
                f"{self.__class__.__name__} expects a string of solution values for one row: {e}")
