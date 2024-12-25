"""SideToken."""
from src.tokens.simple_token import SimpleToken


class SideToken(SimpleToken):
    """Represents start token for matching start side indicator (T, L, B, R)."""

    def __init__(self):
        """Initialize start side token with pattern '([TLBR])'."""
        super().__init__('([TLBR])')

    @property
    def description(self) -> str:
        """Get the description of the SideToken.

        Returns:
            str: A description of the SideToken's purpose and behavior.
        """
        return (
            'This represents a Side of the board.'
            'T is top, L is left, B is bottom, R is right.'
        )

    @property
    def example(self) -> str:
        """Get an example of a value matched by the SideToken.

        Returns:
            str: An example string that the SideToken would match.
        """
        return 'B'

    @property
    def is_abstract(self) -> bool:
        """Check if the token is abstract.

        This method returns `True` to indicate that the token is abstract.

        Returns:
            bool: `True` if the token is abstract, otherwise `False`.
        """
        return False
