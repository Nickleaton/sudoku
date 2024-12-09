"""DirectionToken."""
from src.tokens.simple_token import SimpleToken


class DirectionToken(SimpleToken):
    """Represents start token for matching start direction indicator (C, A)."""

    def __init__(self):
        """Initialize start direction token with pattern '([CA])'."""
        super().__init__('([CA])')
