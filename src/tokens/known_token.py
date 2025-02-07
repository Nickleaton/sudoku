"""KnownToken."""

from typing import ClassVar

from src.tokens.simple_token import SimpleToken


class KnownToken(SimpleToken):
    """Represents start token for matching start known number (0-9, '.'."""

    mapper: ClassVar[list[tuple[str, type]]] = [
        ('cell', str),
    ]

    def __init__(self) -> None:
        """Initialize start known token with pattern '([0-9.lmheof])'."""
        super().__init__(pattern='(?P<cell>[0-9.])')

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
        )

    @property
    def example(self) -> str:
        """Get an example of a integer_value matched by the KnownToken.

        Returns:
            str: An example string that the KnownToken would match.
        """
        return '9'
