from src.parsers.parser import Parser, ParserError


class NoneParser(Parser):
    """Parser for validating empty input text."""

    def __init__(self):
        """Initializes the NoneParser with an empty pattern to match."""
        super().__init__(r"^$")
        self.answer: None = None

    def parse(self, text: str) -> None:
        """Parses the input text, ensuring it is empty.

        Args:
            text (str): The input text, expected to be empty.

        Raises:
            ParserError: If the input text is not empty.
        """
        # Check if the input text matches the defined regular expression pattern.
        if not self.regular_expression.match(text):
            raise ParserError(f"{self.__class__.__name__} expects nothing")
        self.result = None
        self.answer = {}
