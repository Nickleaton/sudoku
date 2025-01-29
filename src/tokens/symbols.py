"""Tokens for Symbols."""
from src.tokens.simple_token import SimpleToken


class SymbolToken(SimpleToken):
    """Represents a symbol token.

    Inherits from `SimpleToken` and serves as the base class for tokens
    representing specific symbols.

    Attributes:
        symbol (str): The symbol represented by this token.
        pattern (str | None): An optional regex pattern to match the symbol.
    """

    def __init__(self, symbol: str, pattern: str | None = None) -> None:
        """Initialize a SymbolToken with a specific symbol.

        Args:
            symbol (str): The symbol for this token.
            pattern (str | None): The pattern if different from the symbol.
        """
        super().__init__(symbol if pattern is None else pattern)
        self.symbol: str = symbol

    def __repr__(self) -> str:
        """Return a string representation of the SymbolToken.

        Returns:
            str: A string representation of the SymbolToken, including the symbol
                 and pattern if applicable.
        """
        if self.__class__ == SymbolToken:
            return f"{self.__class__.__name__}({self.symbol!r}, {self.pattern!r})"
        return f"{self.__class__.__name__}()"

    def backus_naur_form(self) -> str:
        """Return the Backus-Naur form representation of the symbol.

        Returns:
            str: The symbol in Backus-Naur form (quoted).
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

    @property
    def is_abstract(self) -> bool:
        """Check if the token is abstract.

        This method returns `True` to indicate that the token is abstract.

        Returns:
            bool: `True` if the token is abstract, otherwise `False`.
        """
        return self.__class__ == SymbolToken


class EqualsToken(SymbolToken):
    """Represents an equals sign ('=') token."""

    def __init__(self) -> None:
        """Initialize an equals token with the symbol '='."""
        super().__init__(symbol='=')


class CommaToken(SymbolToken):
    """Represents a comma (',') token."""

    def __init__(self) -> None:
        """Initialize a comma token with the symbol ','."""
        super().__init__(symbol=',')


class DashToken(SymbolToken):
    """Represents a dash ('-') token."""

    def __init__(self) -> None:
        """Initialize a dash token with the symbol '-'."""
        super().__init__(symbol='-')


class QuestionMarkToken(SymbolToken):
    """Represents a question mark ('?') token."""

    def __init__(self) -> None:
        """Initialize a question mark token with the symbol '?'."""
        super().__init__(symbol='?', pattern=r"\?")


class XToken(SymbolToken):
    """Represents an 'x' token."""

    def __init__(self) -> None:
        """Initialize an 'x' token with the symbol 'x'."""
        super().__init__(symbol='x')


class DotDotToken(SymbolToken):
    """Represents a dot-dot ('..') token."""

    def __init__(self) -> None:
        """Initialize a dot-dot token with the symbol '..'."""
        super().__init__(symbol='..', pattern=r"\.\.")
