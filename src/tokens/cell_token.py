from src.tokens.simple_token import SimpleToken


class CellToken(SimpleToken):
    """Represents a cell token with two digits."""

    def __init__(self):
        """Initializes a cell token with pattern '\\d\\d'."""
        super().__init__(r"(\d)(\d)")