from src.parsers.parser import Parser, ParserError
from src.tokens.token import Token


class UnknownParser(Parser):
    """Parser for unknown input. Always fail so we catch missing design issues """

    def __init__(self):
        """Initializes DigitsParser with a regex pattern for comma-separated digits."""
        super().__init__(pattern=r"^This should never ever match$", example_format="")
        self.token = Token("This should never match")

    def parse(self, text: str) -> None:
        """Parses the given text according to the implemented pattern.

        Args:
            text (str): The input string to parse.

        Raises:
            NotImplementedError: This method should be implemented in subclasses.
        """
        raise ParserError(f"{self.__class__.__name__} never matches")
