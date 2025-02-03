"""CellToken."""
from typing import Type

from src.tokens.simple_token import SimpleToken


class SizeToken(SimpleToken):
    """Represents the box size."""

    mapper: list[tuple[str, Type]] = [
        ('rows', int),
        ('cols', int),
    ]

    def __init__(self) -> None:
        """Initialize start cell token with pattern 'ddxdd' where its rows x columns."""
        super().__init__(pattern=r'(?P<rows>\d\d{0,1})x(?P<cols>\d\d{0,1})')

    @property
    def description(self) -> str:
        """Get the description of the SizeToken.

        Returns:
            str: A description of the SizeToken's purpose and behavior.
        """
        return 'A box size dxd where its rxc for rows by columns.'

    @property
    def example(self) -> str:
        """Get an example of digit matched by the SizeToken.

        Returns:
            str: An example string that the SizeToken would match.
        """
        return '9x9'
