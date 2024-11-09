from src.parsers.parser import ParserError, Parser


class KnownParser(Parser):
    """Parses a known string containing know values or restricted conditions

    Attributes:
        result (list[str]): A list of  one character values
    """

    def __init__(self):
        """Initializes the KnownParser with a regular expression for validating input strings.

        .     no restriction
        0-9   a given value
        l     low
        m     medium
        h     high
        e     even
        o     odd
        f     fortress cell [Must be greater than its orthogonal neighbours]

        """
        super().__init__(pattern=f"^{Parser.KNOWN}+$", example_format="123456789")

    @classmethod
    def help(cls) -> str:
        return (
            "a string containing the known values or restricted conditions\n\n"
            ".     no restriction"
            "0-9   a given value"
            "l     low"
            "m     medium"
            "h     high"
            "e     even"
            "o     odd"
            "f     fortress cell [Must be greater than its orthogonal neighbours]"
        )

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
                f"{self.__class__.__name__} expects a list of known or restricted cell values for one row")

        try:
            self.result = list(text)
            self.answer = list(text)
        except ValueError:
            self.raise_error()
