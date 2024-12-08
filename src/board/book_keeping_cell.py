"""Base class for tokens representing regex patterns."""
import re
import sys
from typing import Type

from sortedcontainers import SortedDict

from src.utils.sudoku_exception import SudokuException


class Token:
    """Base class for all tokens used to represent regex patterns.

    Attributes:
        pattern (str): The regex pattern associated with the token.
        regexp (re.Pattern): The compiled regex pattern.
    """

    classes: dict[str, Type['Token']] = SortedDict({})

    # Creation Routines

    def __init_subclass__(cls, **kwargs):
        """Register the subclass to be creatable from YAML.

        Args:
            cls (type): The class being initialized.
            kwargs (dict): Additional keyword arguments passed to the method.
        """
        super().__init_subclass__(**kwargs)
        # Register the subclass
        Token.classes[cls.__name__] = cls
        Token.classes[Token.__name__] = Token

    def __init__(self, pattern: str):
        """Initialize a token with a regex pattern.

        Args:
            pattern (str): The regex pattern representing this token.
        """
        self.pattern: str = pattern
        self.regexp: re.Pattern = re.compile(f"^{pattern}$")

    @property
    def name(self) -> str | None:
        """Return the name of the token class.

        Returns:
            str | None: The name of the token (class name without 'Token') or 'Token' for the base class.
        """
        return "Token" if self.__class__.__name__ == "Token" else self.__class__.__name__[:-5]

    def match(self, text: str) -> bool:
        """Match the given text against the token's regex pattern.

        Args:
            text (str): The text to match.

        Returns:
            bool: True if the text matches the pattern, False otherwise.
        """
        return self.regexp.match(text) is not None

    def groups(self, text: str) -> list[str]:
        """Return the matched groups from the text.

        Args:
            text (str): The text to match.

        Returns:
            list[str]: A list of matched groups, or an empty list if no match is found.
        """
        match = self.regexp.match(text)
        return list(match.groups()) if match else []

    def backus_naur_form(self) -> str:
        """Return the Backus-Naur Form (BNF) representation of the token.

        Returns:
            str: The BNF representation of the token (token name in angle brackets).
        """
        return f"<{self.name}>"

    def __repr__(self):
        """Return a string representation of the token.

        Returns:
            str: The string representation of the token, including its pattern.
        """
        return f"{self.__class__.__name__}({self.pattern!r})"

    def __add__(self, other: 'Token') -> 'SequenceToken':
        """Concatenate two tokens into a sequence.

        Args:
            other (Token): Another token to concatenate.

        Returns:
            SequenceToken: A new SequenceToken representing the concatenated tokens.
        """
        return SequenceToken([self, other])

    def __or__(self, other: 'Token') -> 'ChoiceToken':
        """Create an alternation (choice) between two tokens.

        Args:
            other (Token): Another token to alternate with this token.

        Returns:
            ChoiceToken: A new ChoiceToken representing the alternation.
        """
        return ChoiceToken([self, other])

    def __mul__(self, times: int | tuple) -> 'RepeatToken':
        """Repeat the token a specified number of times.

        Args:
            times (int | tuple): An integer or tuple specifying the repetition count.
                - If an integer, it specifies the exact number of repetitions or 0 for unlimited repetitions.
                - If a tuple, it specifies the lower and upper bounds for repetitions.

        Returns:
            RepeatToken: A new RepeatToken with the specified repetition pattern.
        """
        if isinstance(times, tuple):
            return RepeatToken(self, times[0], times[1])
        return RepeatToken(self, times, times)


class SequenceToken(Token):
    """Represent a sequence of tokens concatenated together."""

    def __init__(self, tokens: list[Token]):
        """Initialize a sequence of tokens.

        Args:
            tokens (list[Token]): A list of tokens to concatenate in sequence.
        """
        combined_pattern = ''.join(f"({token.pattern})" for token in tokens)
        super().__init__(combined_pattern)
        self.tokens = tokens

    def backus_naur_form(self) -> str:
        """Return the Backus-Naur Form (BNF) representation of the sequence.

        Returns:
            str: The BNF representation of the token sequence.
        """
        return " ".join(token.backus_naur_form() for token in self.tokens)

    def __repr__(self):
        """Return a string representation of the sequence of tokens.

        Returns:
            str: The string representation of the token sequence.
        """
        return f"{self.__class__.__name__}({', '.join(repr(token) for token in self.tokens)})"


class ChoiceToken(Token):
    """Represent an alternation (choice) between multiple tokens."""

    def __init__(self, tokens: list[Token]):
        """Initialize an alternation pattern between tokens.

        Args:
            tokens (list[Token]): A list of tokens to alternate between.
        """
        alternation_pattern = '|'.join([f"({token.pattern})" for token in tokens])
        super().__init__(alternation_pattern)
        self.tokens = tokens

    def backus_naur_form(self) -> str:
        """Return the Backus-Naur Form (BNF) representation of the alternation.

        Returns:
            str: The BNF representation of the alternation.
        """
        return f"({' | '.join(token.backus_naur_form() for token in self.tokens)})"

    def __repr__(self):
        """Return a string representation of the alternation.

        Returns:
            str: The string representation of the alternation.
        """
        return f"{self.__class__.__name__}({' | '.join(repr(token) for token in self.tokens)})"


class RepeatToken(Token):
    """Represent a repeated pattern of a token."""

    def __init__(self, token: Token, lower: int = 0, upper: int = sys.maxsize):
        """Initialize a token with repetition pattern based on lower and upper bounds.

        Args:
            token (Token): The token to apply repetition pattern to.
            lower (int): Minimum occurrences of the token (default is 0).
            upper (int): Maximum occurrences of the token (default is sys.maxsize).

        Raises:
            AssertionError: If lower is greater than upper.
        """
        if lower < 0:
            raise SudokuException("Lower bound cannot be negative.")
        if lower > upper:
            raise SudokuException("Lower bound must be less than or equal to upper bound.")

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
        """Return the Backus-Naur Form (BNF) representation of the repetition.

        Returns:
            str: The BNF representation of the repetition.
        """
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
        """Return a string representation of the repeated token.

        Returns:
            str: The string representation of the repeated token.
        """
        return f"{self.__class__.__name__}({self.token!r}, {self.lower}, {self.upper})"


class OptionalToken(RepeatToken):
    """Represent an optional pattern of a token (0 or 1 repetition)."""

    def __init__(self, token: Token):
        """Initialize an optional token pattern.

        Args:
            token (Token): The token to make optional.
        """
        super().__init__(token, 0, 1)

    def backus_naur_form(self) -> str:
        """Return the Backus-Naur Form (BNF) representation of the optional token.

        Returns:
            str: The BNF representation of the optional token.
        """
        return f"{self.token.backus_naur_form()} ?"

    def __repr__(self):
        """Return a string representation of the optional token.

        Returns:
            str: The string representation of the optional token.
        """
        return f"{self.__class__.__name__}({self.token!r})"
