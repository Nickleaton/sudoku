"""CellToken."""
from src.tokens.simple_token import SimpleToken


class CellToken(SimpleToken):
    """Represents a cell token with two digits."""

    def __init__(self):
        """Initialize a cell token with pattern 'dd' where the digits are row column."""
        super().__init__(r"(\d)(\d)")