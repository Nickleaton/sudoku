"""DirectionToken."""
from src.tokens.simple_token import SimpleToken


class DirectionToken(SimpleToken):
    """Represents a token for matching a direction indicator (C, A)."""

    def __init__(self):
        """Initialize a direction token with pattern '([CA])'."""
        super().__init__(r"([CA])")
