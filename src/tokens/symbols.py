"""Tokens for Symbols."""
from src.tokens.simple_token import SimpleToken


class SymbolToken(SimpleToken):
    """Represent start symbol token.

    Inherits from `SimpleToken` and serves as start base class for tokens
    representing specific symbols.

    Attributes:
        symbol (str): The symbol represented by this token.
    """

    def __init__(self, symbol: str) -> None:
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

    @property
    def description(self) -> str:
        """Get the description of the SymbolToken.

        Returns:
            str: A description of the SymbolToken's purpose and behavior.
        """
        if self.__class__ != SymbolToken:
            return f'Matches a symbol {self.symbol!r}.'
        return super().description

    @property
    def example(self) -> str:
        """Get an example of a value matched by the SymbolToken.

        Returns:
            str: An example string that the SymbolToken would match.
        """
        if self.__class__ != SymbolToken:
            return self.symbol
        return super().example


class EqualsToken(SymbolToken):
    """Represent an equals sign token."""

    def __init__(self) -> None:
        """Initialize an equals token with the symbol '='."""
        super().__init__(symbol='=')

    def __repr__(self) -> str:
        """Return start string representation of the EqualsToken.

        Returns:
            str: The string representation of the EqualsToken.
        """
        return 'EqualsToken()'

    @property
    def is_abstract(self) -> bool:
        """Check if the token is abstract.

        This method returns `True` to indicate that the token is abstract.

        Returns:
            bool: `True` if the token is abstract, otherwise `False`.
        """
        return False


class CommaToken(SymbolToken):
    """Represent start comma token."""

    def __init__(self) -> None:
        """Initialize start comma token with the symbol ','."""
        super().__init__(symbol=',')

    def __repr__(self) -> str:
        """Return start string representation of the CommaToken.

        Returns:
            str: The string representation of the CommaToken.
        """
        return 'CommaToken()'

    @property
    def is_abstract(self) -> bool:
        """Check if the token is abstract.

        This method returns `True` to indicate that the token is abstract.

        Returns:
            bool: `True` if the token is abstract, otherwise `False`.
        """
        return False


class DashToken(SymbolToken):
    """Represent start dash token."""

    def __init__(self) -> None:
        """Initialize start dash token with the symbol '-'."""
        super().__init__(symbol='-')

    def __repr__(self) -> str:
        """Return start string representation of the DashToken.

        Returns:
            str: The string representation of the DashToken.
        """
        return 'DashToken()'

    @property
    def is_abstract(self) -> bool:
        """Check if the token is abstract.

        This method returns `True` to indicate that the token is abstract.

        Returns:
            bool: `True` if the token is abstract, otherwise `False`.
        """
        return False


class QuestionMarkToken(SymbolToken):
    """Represent start question mark token."""

    def __init__(self) -> None:
        """Initialize start question mark token with the symbol '?'."""
        super().__init__(symbol=r'\?')

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

    @property
    def is_abstract(self) -> bool:
        """Check if the token is abstract.

        This method returns `True` to indicate that the token is abstract.

        Returns:
            bool: `True` if the token is abstract, otherwise `False`.
        """
        return False
