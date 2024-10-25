from src.parsers.parser import Parser, ParserError


class UnknownParser(Parser):
    """Parser for unknown input. Always fail so we catch missing design issues """

    def __init__(self):
        """Initializes DigitsParser with a regex pattern for comma-separated digits."""
        super().__init__(r"^This should never ever match$")

    def parse(self, text: str) -> None:
        """Parses the given text according to the implemented pattern.

        Args:
            text (str): The input string to parse.

        Raises:
            NotImplementedError: This method should be implemented in subclasses.
        """
        raise ParserError(f"{self.__class__.__name__} never matches")
