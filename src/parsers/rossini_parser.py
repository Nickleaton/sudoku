from typing import Optional, Dict

from src.parsers.parser import Parser, ParserError


class RossiniParser(Parser):
    """Parser for Rossini format: '[TLBR]d=[DIU]'."""

    def __init__(self):
        """Initializes the RossiniParser with a regex pattern for the Rossini format."""
        super().__init__(r'^[TLBR]\d=[DIU]$')
        self.answer: Optional[Dict[str, Any]] = None

    def parse(self, text: str) -> None:
        """Parses the input text to extract components in the Rossini format.

        Args:
            text (str): The input text expected to be in the format '[TLBR]d=[DIU]'.

        Raises:
            ParserError: If the input text does not match the expected format.
        """
        # Check if the input text matches the defined regular expression pattern.
        if not self.regular_expression.match(text):
            raise ParserError(f"{self.__class__.__name__} expects format like '[TLBR]d=[DIU]'")

        # Extract the components: side, index, and direction.
        side = text[0]  # 'T', 'L', 'B', or 'R'
        index = int(text[1])  # digit following the side
        direction = text[3]  # 'D', 'I', or 'U'

        # Store results in the result attribute.
        self.result = [side, index, direction]
        self.answer = {
            'side': side,
            'index': str(index),
            'direction': direction
        }
