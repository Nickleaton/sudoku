from src.parsers.parser import Parser, ParserError


class CellPairsParser(Parser):
    """Parser for cell pairs in the format 'XY=AB', where X, Y, A, and B are digits."""

    def __init__(self):
        """Initializes CellPairsParser with a regex pattern for comma-separated digits."""
        # Call the parent class (Parser) constructor with a regex pattern that matches the required format.
        super().__init__(pattern=r"^\s*\d\d\s*-\s*\d\d\s*$", example_format="r1c1=r2c2")

    def parse(self, text: str) -> None:
        """Parses the input text to extract cell references.

        Args:
            text (str): The input text in the format 'XY=AB' to be parsed.

        Raises:
            ParserError: If the input text does not match the expected format or if conversion to integers fails.
        """
        # Check if the input text matches the defined regular expression pattern.
        if not self.regular_expression.match(text):
            # Raise an error if the format is incorrect.
            raise ParserError(f"{self.__class__.__name__} expects a cell reference equals cell reference eg '12=23'")

        try:
            # Split the input text into individual characters, convert them to integers,
            # and store the result as a list of integers in the result attribute.
            stripped_text: str = text.replace(" ", "")
            row1: str = stripped_text[0]
            column1: str = stripped_text[1]
            row2: str = stripped_text[3]
            column2: str = stripped_text[4]
            self.result = [
                int(row1),
                int(column1),
                int(row2),
                int(column2)
            ]
            self.answer = {
                'row1': row1,
                'column1': column1,
                'row2': row2,
                'column2': column2
            }
        except ValueError:
            self.raise_error()
