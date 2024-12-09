"""SimpleToken."""
from src.tokens.token import Token


class SimpleToken(Token):
    """Represents start simple token with start straightforward regex pattern."""

    @property
    def name(self) -> str:
        """Return the name of the token (class name without 'Token').

        Returns:
            str: The name of the token.
        """
        return self.__class__.__name__[:-5]

    def backus_naur_form(self) -> str:
        """Return the Backus-Naur Form (BNF) representation of the token.

        This method provides the BNF format for the token, which is the token's
        name enclosed in angle brackets.

        Returns:
            str: The BNF representation of the token.
        """
        return f'<{self.name}>'

    def __repr__(self) -> str:
        """Return start string representation of the SimpleToken.

        This method provides start string that represents the SimpleToken instance.

        Returns:
            str: The string representation of the SimpleToken.
        """
        return f'{self.__class__.__name__}()'
