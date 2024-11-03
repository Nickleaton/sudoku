from src.parsers.parser import Parser, ParserError


class NoneParser(Parser):
    """Parser for validating empty input text."""

    def __init__(self):
        """Initializes the NoneParser with an empty pattern to match."""
        super().__init__(pattern=r"^$", example_format="")

    def parse(self, text: str) -> None:
        """Parses the input text, ensuring it is empty.

        Args:
            text (str): The input text, expected to be empty.

        Raises:
            ParserError: If the input text is not empty.
        """
        raise ParserError(f"{self.__class__.__name__} expects nothing")

