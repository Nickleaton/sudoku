from src.tokens.simple_token import SimpleToken


class SymbolToken(SimpleToken):
    """Represents a symbol token."""

    def __init__(self, symbol: str):
        super().__init__(symbol)
        self.symbol: str = symbol

    def __repr__(self) -> str:
        return f"SymbolToken('{self.symbol}')"

    def backus_naur_form(self) -> str:
        return f'"{self.symbol}"'


class EqualsToken(SymbolToken):
    """Represents an equals sign token."""

    def __init__(self):
        """Initializes an equals token with pattern '='."""
        super().__init__("=")

    def __repr__(self) -> str:
        return "EqualsToken()"


class CommaToken(SymbolToken):
    """Represents a comma token."""

    def __init__(self):
        """Initializes a comma token with pattern ','."""
        super().__init__(",")

    def __repr__(self) -> str:
        return "CommaToken()"


class DashToken(SymbolToken):
    """Represents a dash token."""

    def __init__(self):
        """Initializes a comma token with pattern '-'."""
        super().__init__("-")

    def __repr__(self) -> str:
        return "DashToken()"
