"""CellToken."""
from src.tokens.simple_token import SimpleToken


class SizeToken(SimpleToken):
    """Represents the box size."""

    mapper: list[tuple[str, str | int | float | list]] = [
        ('row', int),
        ('col', int),
    ]

    def __init__(self) -> None:
        """Initialize start cell token with pattern 'ddxdd' where its row x column."""
        super().__init__(pattern=r'(?P<row>\d\d{0,1})x(?P<col>\d\d{0,1})')

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
