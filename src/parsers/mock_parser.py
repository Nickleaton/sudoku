from src.parsers.parser import Parser, ParserError


class MockParser(Parser):
    """A mock parser for testing purposes.

    This parser provides a basic implementation of the Parser class
    for testing purposes, focusing on simple comma-separated text input.

    Attributes:
        result (list[str]): The result of the parsing operation.
    """

    def __init__(self):
        """Initializes the MockParser with a dummy regex pattern.

        This pattern is not used in the tests as this mock parser focuses
        on basic string manipulation rather than regex matching.
        """
        super().__init__(pattern=r"", example_format="")  # Dummy pattern, not used in tests

    def parse(self, text: str):
        """Parses the input text into a list of strings.

        Splits the input text by commas and raises a ParserError if the
        input is empty.

        Args:
            text (str): The input string to parse.

        Returns:
            list[str]: A list of strings obtained by splitting the input
            text by commas.

        Raises:
            ParserError: If the input string is empty.
        """
        if not text:
            raise ParserError("Input cannot be empty.")
        self.result = text.split(',')
        self.answer = text.split(',')
