"""KnownParser."""
from src.parsers.parser import Parser, ParserError
from src.tokens.digit_token import DigitToken


class KnownParser(Parser):
    """Parse a known string containing known values or restricted conditions.

    This parser handles strings representing known values or restrictions on cells, such as
    specific digits, conditions like 'low', 'medium', 'high', 'even', 'odd', or 'fortress' cells.

    Attributes:
        result (list[str]): A list of one-character values representing the parsed conditions.
    """

    def __init__(self):
        """Initialize the KnownParser with a regular expression for validating input strings.

        The input string can represent:
            - '.' for no restriction,
            - digits '0-9' for a given value,
            - 'l' for low,
            - 'm' for medium,
            - 'h' for high,
            - 'e' for even,
            - 'o' for odd,
            - 'f' for a fortress cell (must be greater than its orthogonal neighbors).
        """
        super().__init__(pattern=f"^{Parser.KNOWN}+$", example_format="123456789")
        self.token = DigitToken() * (1, 999)

    def help(self) -> str:
        """Return the help string for the KnownParser.

        The help string describes the syntax and the valid values or restrictions for the known string.

        Returns:
            str: The help description explaining valid input formats.
        """
        return (
            "A string containing the known values or restricted conditions:\n\n"
            ".     no restriction\n"
            "0-9   a given value\n"
            "l     low\n"
            "m     medium\n"
            "h     high\n"
            "e     even\n"
            "o     odd\n"
            "f     fortress cell [Must be greater than its orthogonal neighbours]\n"
        )

    def parse(self, text: str) -> None:
        """Parse the input string and store the result in the 'result' attribute.

        This method input_types if the input string matches the expected format and parses it accordingly.
        It stores the parsed values in the `result` and `data` attributes.

        Args:
            text (str): The input string to be parsed, expected to follow the known value or restriction format.

        Raises:
            ParserError: If the input string does not match the expected format or cannot be parsed.
        """
        # Validate the input format using the regular expression
        if not self.regular_expression.match(text):
            raise ParserError(
                f"{self.__class__.__name__} expects a list of known or restricted cell values for one row"
            )

        try:
            self.result = list(text)
            self.answer = list(text)
        except ValueError:
            self.raise_error()
