"""KnownToken."""
from src.tokens.simple_token import SimpleToken


class KnownToken(SimpleToken):
    """Represents start token for matching start known number (0-9, l, m, h, e, o, f, s)."""

    def __init__(self):
        """Initialize start known token with pattern '([0-9.lmheof])'."""
        super().__init__('([0-9.lmheofs])')

    @property
    def is_abstract(self) -> bool:
        """Check if the token is abstract.

        This method returns `True` to indicate that the token is abstract.

        Returns:
            bool: `True` if the token is abstract, otherwise `False`.
        """
        return False

    @property
    def description(self) -> str:
        """Get the description of the KnownToken.

        Returns:
            str: A description of the KnownToken's purpose and behavior.
        """
        return (
            'This represents a known value when specifying the initial state of the board.'
            '0-9 matches a digit.  Later it will be extended to cover Hex. '
            '. represents a cell with no known value.'
            'l is a low value, m is a medium value, h is a high value.'
            'e is an even value, o is an odd value.'
            'f is a fortress cell. Orthogonal neighbors must be less than the fortress cell.'
            's is a fortress cell. Orthogonal neighbors must be greater than the fortress cell.'
        )

    @property
    def example(self) -> str:
        """Get an example of a value matched by the KnownToken.

        Returns:
            str: An example string that the KnownToken would match.
        """
        return 'm'
