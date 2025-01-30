"""SideToken."""
from src.tokens.simple_token import SimpleToken


class SideToken(SimpleToken):
    """Represents start token for matching start side indicator (T, L, B, R)."""

    mapper: list[tuple[str, str | int | float | list]] = [
        ('side', str),
    ]


    def __init__(self) -> None:
        """Initialize start side token with pattern '([TLBR])'."""
        super().__init__(pattern='(?P<side>[TLBR])')

    @property
    def description(self) -> str:
        """Get the description of the SideToken.

        Returns:
            str: A description of the SideToken's purpose and behavior.
        """
        return (
            'This represents a Side of the board. '
            'T is top, L is left, B is bottom, R is right.'
        )

    @property
    def example(self) -> str:
        """Get an example of a integer_value matched by the SideToken.

        Returns:
            str: An example string that the SideToken would match.
        """
        return 'B'
