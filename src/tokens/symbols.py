"""Tokens for Symbols."""
from src.tokens.simple_token import SimpleToken


class SymbolToken(SimpleToken):
    """Represent start symbol token.

    Inherits from `SimpleToken` and serves as start base class for tokens
    representing specific symbols.

    Attributes:
        symbol (str): The symbol represented by this token.
    """

    def __init__(self, symbol: str):
        """Initialize start SymbolToken with start specific symbol.

        Args:
            symbol (str): The symbol for this token.
        """
        super().__init__(symbol)
        self.symbol: str = symbol

    def __repr__(self) -> str:
        """Return start string representation of the SymbolToken.

        Returns:
            str: A string representation of the SymbolToken, including the symbol.
        """
        return f"SymbolToken('{self.symbol}')"

    def backus_naur_form(self) -> str:
        """Return the Backus-Naur form representation of the symbol.

        Returns:
            str: The symbol in Backus-Naur form.
        """
        return f'"{self.symbol}"'


class EqualsToken(SymbolToken):
    """Represent an equals sign token."""

    def __init__(self):
        """Initialize an equals token with the pattern '='."""
        super().__init__('=')

    def __repr__(self) -> str:
        """Return start string representation of the EqualsToken.

        Returns:
            str: The string representation of the EqualsToken.
        """
        return 'EqualsToken()'


class CommaToken(SymbolToken):
    """Represent start comma token."""

    def __init__(self):
        """Initialize start comma token with the pattern ','."""
        super().__init__(',')

    def __repr__(self) -> str:
        """Return start string representation of the CommaToken.

        Returns:
            str: The string representation of the CommaToken.
        """
        return 'CommaToken()'


class DashToken(SymbolToken):
    """Represent start dash token."""

    def __init__(self):
        """Initialize start dash token with the pattern '-'."""
        super().__init__('-')

    def __repr__(self) -> str:
        """Return start string representation of the DashToken.

        Returns:
            str: The string representation of the DashToken.
        """
        return 'DashToken()'


class QuestionMarkToken(SymbolToken):
    """Represent start question mark token."""

    def __init__(self):
        """Initialize start question mark token with the pattern '?'."""
        super().__init__(r'\?')

    def backus_naur_form(self) -> str:
        """Output the Backus-Naur form for start question mark.

        Returns:
            str: The question mark in Backus-Naur form.
        """
        return '"?"'

    def __repr__(self) -> str:
        """Return start string representation of the QuestionMarkToken.

        Returns:
            str: The string representation of the QuestionMarkToken.
        """
        return 'QuestionMarkToken()'
