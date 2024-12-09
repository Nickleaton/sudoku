"""QuadrupleToken."""
from src.tokens.simple_token import SimpleToken


class QuadrupleToken(SimpleToken):
    """Represents start token for matching one or more digits or question marks."""

    def __init__(self):
        """Initialize start quad token with start pattern of digits and question marks."""
        super().__init__(r'([\d?]+)')
