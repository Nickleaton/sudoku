"""CycleToken."""
from src.tokens.simple_token import SimpleToken


class CycleToken(SimpleToken):
    """Represents a token for matching a orientation indicator (C, A)."""

    def __init__(self):
        """Initialize token with pattern '([CA])' for clockwise and anticlockwise."""
        super().__init__('([CA])')

    @property
    def description(self) -> str:
        """Get the description of the CycleToken.

        Returns:
            str: A description of the CycleToken's purpose and behavior.
        """
        return 'A direction indicator. C for clockwise, A for anticlockwise.'

    @property
    def example(self) -> str:
        return 'A'

    @property
    def is_abstract(self) -> bool:
        """Check if the token is abstract.

        This method returns `True` to indicate that the token is abstract.

        Returns:
            bool: `True` if the token is abstract, otherwise `False`.
        """
        return False
