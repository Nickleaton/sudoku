"""Tokens for Symbols."""
from src.tokens.simple_token import SimpleToken


class SymbolToken(SimpleToken):
    """Represents a symbol token.

    Inherits from `SimpleToken` and is used as a base class for tokens
    that represent specific symbols.

    Attributes:
        symbol (str): The symbol represented by this token.
    """

    def __init__(self, symbol: str):
        """Initialize a SymbolToken with a specific symbol.

        Args:
            symbol (str): The symbol for this token.
        """
        super().__init__(symbol)
        self.symbol: str = symbol

    def __repr__(self) -> str:
        """Return a string representation of the SymbolToken.

        Returns:
            str: The representation of the SymbolToken, including the symbol.
        """
        return f"SymbolToken('{self.symbol}')"

    def backus_naur_form(self) -> str:
        """Return the Backus-Naur form representation of the symbol.

        Returns:
            str: The symbol in Backus-Naur form.
        """
        return f'"{self.symbol}"'


class EqualsToken(SymbolToken):
    """Represents an equals sign token."""

    def __init__(self):
        """Initialize an equals token with pattern '='."""
        super().__init__("=")

    def __repr__(self) -> str:
        """Return a string representation of the EqualsToken.

        Returns:
            str: The representation of the EqualsToken.
        """
        return "EqualsToken()"


class CommaToken(SymbolToken):
    """Represents a comma token."""

    def __init__(self):
        """Initialize a comma token with pattern ','."""
        super().__init__(",")

    def __repr__(self) -> str:
        """Return a string representation of the CommaToken.

        Returns:
            str: The representation of the CommaToken.
        """
        return "CommaToken()"


class DashToken(SymbolToken):
    """Represents a dash token."""

    def __init__(self):
        """Initialize a dash token with pattern '-'."""
        super().__init__("-")

    def __repr__(self) -> str:
        """Return a string representation of the DashToken.

        Returns:
            str: The representation of the DashToken.
        """
        return "DashToken()"


class QuestionMarkToken(SymbolToken):
    """Represents a question mark token."""

    def __init__(self):
        """Initialize a question mark token with pattern '?'."""
        super().__init__(r"\?")

    def backus_naur_form(self) -> str:
        """Special to handle escaping."""
        return '"?"'

    def __repr__(self) -> str:
        """Return a string representation of the QuestionMarkToken.

        Returns:
            str: The representation of the QuestionMarkToken.
        """
        return "QuestionMarkToken()"
