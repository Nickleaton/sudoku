"""CycleToken."""
from src.tokens.simple_token import SimpleToken


class CycleToken(SimpleToken):
    """Represents a token for matching a orientation indicator (C, A)."""

    def __init__(self):
        """Initialize token with pattern '([CA])' for clockwise and anticlockwise."""
        super().__init__('([CA])')
