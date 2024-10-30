from typing import Optional, Dict, Any

from src.parsers.parser import Parser, ParserError


class OutsideArrowValueParser(Parser):
    """Parser for Outside Arrow Value format: '[TLBR]d=d+'."""

    def __init__(self):
        """Initializes the OutsideArrowValueParser with a regex pattern for the Outside Arrow Value format."""
        super().__init__(r'^[TLBR]\d=\d+$')
        self.answer: Optional[Dict[str, Any]] = None

    def parse(self, text: str) -> None:
        """Parses the input text to extract components in the Outside Arrow Value format.

        Args:
            text (str): The input text expected to be in the format '[TLBR]d=d+'.

        Raises:
            ParserError: If the input text does not match the expected format.
        """
        # Check if the input text matches the defined regular expression pattern.
        if not self.regular_expression.match(text):
            raise ParserError(f"{self.__class__.__name__} expects format like '[TLBR]d=d+'")

        # Extract the components: side, index, and value.
        side = text[0]  # 'T', 'L', 'B', or 'R'
        index = int(text[1])  # digit following the side
        value = int(text.split('=')[1])  # value after the equals sign

        # Store results in the result attribute.
        self.result = [side, index, value]
        self.answer = {
            'side': side,
            'index': str(index),
            'value': str(value),
        }
