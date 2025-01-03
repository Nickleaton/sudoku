"""KnownToken."""
from src.tokens.simple_token import SimpleToken


class KnownToken(SimpleToken):
    """Represents start token for matching start known number (0-9, l, m, h, e, o, f, s)."""

    def __init__(self) -> None:
        """Initialize start known token with pattern '([0-9.lmheof])'."""
        super().__init__(pattern='([0-9.lmheofs])')

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
            'This represents a known integer_value when specifying the initial state of the board. '
            '0-9 matches a digit. Later it will be extended to cover Hex. '
            '. represents a cell with no known integer_value. '
            'l is a low integer_value, m is a medium integer_value, h is a high integer_value. '
            'e is an even integer_value, o is an odd integer_value. '
            'f is a fortress cell. Orthogonal neighbors must be less than the fortress cell. '
            's is a fortress cell. Orthogonal neighbors must be greater than the fortress cell.'
        )

    @property
    def example(self) -> str:
        """Get an example of a integer_value matched by the KnownToken.

        Returns:
            str: An example string that the KnownToken would match.
        """
        return 'm'
