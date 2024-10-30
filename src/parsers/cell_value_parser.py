from typing import Dict, Optional

from src.parsers.parser import Parser, ParserError


class CellValueParser(Parser):
    """Parser for Cell Value format: 'dd=d+' where dd are two digits and d+ is one or more digits."""

    def __init__(self):
        """Initializes the CellValueParser with a regex pattern for the Cell Value format."""
        super().__init__(r'^\d{2}=\d+$')
        self.answer: Optional[Dict[str, int]] = None

    def parse(self, text: str) -> None:
        """Parses the input text to extract cell value components.

        Args:
            text (str): The input text expected to be in the format 'dd=d+'.

        Raises:
            ParserError: If the input text does not match the expected format.
        """
        # Check if the input text matches the defined regular expression pattern.
        if not self.regular_expression.match(text):
            raise ParserError(f"{self.__class__.__name__} expects format like 'dd=d+'")

        # Split the text at the equals sign to extract components.
        index, value = text.split('=')
        index = [int(index[0]), int(index[1])]  # Convert the two digits to integers
        value = int(value)  # Convert the right side of the equals sign to an integer

        # Store results in the result attribute.
        self.result = [index, value]
        self.answer = {
            'cell': {
                'row': str(index[0]),
                'column': str(index[1])
            },
            'value': str(value)
        }
