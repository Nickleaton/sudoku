"""CycleToken."""

from typing import ClassVar

from src.tokens.simple_token import SimpleToken


class CycleToken(SimpleToken):
    """Represents a token for matching a orientation indicator (C, A)."""

    mapper: ClassVar[list[tuple[str, type]]] = [
        ('cycle', str),
    ]

    def __init__(self) -> None:
        """Initialize token with pattern '([CA])' for clockwise and anticlockwise."""
        super().__init__(pattern='(?P<cycle>[CA])')

    @property
    def description(self) -> str:
        """Get the description of the CycleToken.

        Returns:
            str: A description of the CycleToken's purpose and behavior.
        """
        return 'A clockwise/anticlockwise indicator. C for clockwise, A for anticlockwise.'

    @property
    def example(self) -> str:
        """Get an example of a integer_value matched by the CycleToken.

        Returns:
            str: An example string that the CycleToken would match.
        """
        return 'A'
