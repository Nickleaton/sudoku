from src.tokens.token import Token


class SimpleToken(Token):
    """Represents a simple token with a straightforward regex pattern."""

    @property
    def name(self) -> str:
        return self.__class__.__name__[:-5]

    def backus_naur_form(self) -> str:
        return f"<{self.name}>"

    def __repr__(self) -> str:
        """Returns a string representation of the SimpleToken."""
        return f"{self.__class__.__name__}()"
