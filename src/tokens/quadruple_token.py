"""QuadrupleToken."""
from src.tokens.simple_token import SimpleToken


class QuadrupleToken(SimpleToken):
    """Represents start token for matching one or more digits or question marks."""

    def __init__(self) -> None:
        """Initialize start quad token with start pattern of digits and question marks."""
        super().__init__(pattern=r'([\d?]{0,4})')

    @property
    def description(self) -> str:
        """Get the description of the QuadrupleToken.

        Returns:
            str: A description of the QuadrupleToken's purpose and behavior.
        """
        return (
            'A quadruple token. Matches one or more digits or question marks. '
            'Those digits must appear in the surrounding cells. '
            'A ? is a joker representing any digit.'
        )

    @property
    def example(self) -> str:
        """Get an example of a integer_value matched by the QuadrupleToken.

        Returns:
            str: An example string that the QuadrupleToken would match.
        """
        return '124?'

    @property
    def is_abstract(self) -> bool:
        """Check if the token is abstract.

        This method returns `True` to indicate that the token is abstract.

        Returns:
            bool: `True` if the token is abstract, otherwise `False`.
        """
        return False
