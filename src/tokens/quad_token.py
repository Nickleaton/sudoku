from src.tokens.simple_token import SimpleToken


class QuadToken(SimpleToken):
    """Represents a token for matching one or more digits or question marks."""

    def __init__(self):
        """Initializes a quad token with a pattern of digits and question marks."""
        super().__init__(r"([\d?]+)")
