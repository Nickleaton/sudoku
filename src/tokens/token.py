import re
import sys
from typing import Union, List, Optional


class Token(object):
    """Base class for all tokens used to represent patterns."""

    def __init__(self, pattern: str):
        """Initializes a token with a given regex pattern.

        Args:
            pattern (str): The regex pattern representing this token.
        """
        self.pattern: str = pattern
        self.regexp: re.Pattern = re.compile(f"^{pattern}$")

    @property
    def name(self) -> Optional[str]:
        return "Token" if self.__class__.__name__ == "Token" else self.__class__.__name__[:-5]

    def match(self, text: str) -> bool:
        return self.regexp.match(text) is not None

    def groups(self, text: str) -> List[str]:
        match = self.regexp.match(text)
        if match is None:
            return []
        return list(match.groups())

    def backus_naur_form(self) -> str:
        return f"<{self.name}>"

    def __repr__(self):
        """Returns a string representation of the token."""
        return f"{self.__class__.__name__}({self.pattern!r})"

    def __add__(self, other: 'Token') -> 'SequenceToken':
        """Concatenates two tokens into a sequence.

        Args:
            other (Token): Another token to concatenate with this token.

        Returns:
            SequenceToken: A new SequenceToken representing the concatenated tokens.
        """
        return SequenceToken([self, other])

    def __or__(self, other: 'Token') -> 'ChoiceToken':
        """Creates an alternation between two tokens.

        Args:
            other (Token): Another token to alternate with this token.

        Returns:
            ChoiceToken: A new ChoiceToken representing the alternation.
        """
        return ChoiceToken([self, other])

    def __mul__(self, times: Union[int, tuple]) -> 'RepeatToken':
        """Repeats the token a specified number of times.

        Args:
            times (Union[int, tuple]): Either an integer or a tuple specifying the repetition count.
                - If an integer, it specifies the exact number of repetitions or 0 for unlimited repetitions.
                - If a tuple, it specifies the lower and maximum number of repetitions.

        Returns:
            RepeatToken: A new RepeatToken with the specified repetition.
        """
        if isinstance(times, tuple):
            return RepeatToken(self, times[0], times[1])
        return RepeatToken(self, times, times)


class SequenceToken(Token):
    """Represents a sequence of tokens concatenated together."""

    def __init__(self, tokens: List[Token]):
        """Initializes a sequence of tokens.

        Args:
            tokens (List[Token]): A list of tokens to concatenate in sequence.
        """
        combined_pattern = ''.join(f"({token.pattern})" for token in tokens)
        super().__init__(combined_pattern)
        self.tokens = tokens

    def backus_naur_form(self) -> str:
        return " ".join(token.backus_naur_form() for token in self.tokens)

    def __repr__(self):
        """Returns a string representation of the sequence."""
        return f"{self.__class__.__name__}({', '.join(repr(token) for token in self.tokens)})"


class ChoiceToken(Token):
    """Represents an alternation (either/or) pattern between tokens."""

    def __init__(self, tokens: List[Token]):
        """Initializes an alternation pattern between multiple tokens.

        Args:
            tokens (List[Token]): A list of tokens to alternate between.
        """
        alternation_pattern = '|'.join([f"({token.pattern})" for token in tokens])
        super().__init__(alternation_pattern)
        self.tokens = tokens

    def backus_naur_form(self) -> str:
        return f"({' | '.join(token.backus_naur_form() for token in self.tokens)})"

    def __repr__(self):
        """Returns a string representation of the alternation."""
        return f"{self.__class__.__name__}({' | '.join(repr(token) for token in self.tokens)})"


class RepeatToken(Token):
    """Represents a repeated pattern of a token."""

    def __init__(self, token: Token, lower: int = 0, upper: int = sys.maxsize):
        """
        Initialize with quantifiers for a token pattern based on lower and upper bounds.

        Args:
            token (Token): The token to apply quantifiers to.
            lower (int): Minimum occurrences of the token pattern (default is 0).
            upper (int): Maximum occurrences of the token pattern (default is sys.maxsize).

        Raises:
            AssertionError: If lower is greater than upper.
        """
        assert lower >= 0, "Lower bound cannot be negative."
        assert lower <= upper, "Lower bound must be less than or equal to upper bound."

        self.lower: int = lower
        self.upper: int = upper
        if lower == 0 and upper == 1:
            pattern = f"({token.pattern})?"
        elif lower == 0 and upper == sys.maxsize:
            pattern = f"({token.pattern})*"
        elif lower == 1 and upper == sys.maxsize:
            pattern = f"({token.pattern})+"
        elif lower == upper:
            pattern = f"({token.pattern}){{{lower}}}"
        else:
            pattern = f"({token.pattern}){{{lower},{upper}}}"
        super().__init__(pattern)
        self.token = token

    def backus_naur_form(self) -> str:
        if self.lower == 0 and self.upper == 1:
            return f"{self.token.backus_naur_form()} ?"
        if self.lower == 0 and self.upper == sys.maxsize:
            return f"{self.token.backus_naur_form()} *"
        if self.lower == 1 and self.upper == sys.maxsize:
            return f"{self.token.backus_naur_form()} +"
        if self.lower == self.upper:
            return f"{self.token.backus_naur_form()}{{{self.lower}}}"
        return f"{self.token.backus_naur_form()} {{{self.lower},{self.upper}}}"

    def __repr__(self):
        """Returns a string representation of the repeated token."""
        return f"{self.__class__.__name__}({repr(self.token)}, {self.lower}, {self.upper})"


class OptionalToken(RepeatToken):
    """Represents an optional pattern of a token."""

    def __init__(self, token: Token):
        """Initializes an optional pattern of a token.

        Args:
            token (Token): The token to make optional.
        """
        super().__init__(token, 0, 1)

    def backus_naur_form(self) -> str:
        return f"{self.token.backus_naur_form()} ?"

    def __repr__(self):
        """Returns a string representation of the optional token."""
        return f"{self.__class__.__name__}({repr(self.token)})"


class OneOrMoreToken(RepeatToken):

    def __init__(self, token: Token):
        super().__init__(token, 1, sys.maxsize)

    def backus_naur_form(self) -> str:
        return f"{self.token.backus_naur_form()} +"

    def __repr__(self):
        """Returns a string representation of the optional token."""
        return f"{self.__class__.__name__}({repr(self.token)})"


class ZeroOrMoreToken(RepeatToken):

    def __init__(self, token: Token):
        super().__init__(token, 0, sys.maxsize)

    def backus_naur_form(self) -> str:
        return f"{self.token.backus_naur_form()} *"

    def __repr__(self):
        """Returns a string representation of the optional token."""
        return f"{self.__class__.__name__}({repr(self.token)})"
