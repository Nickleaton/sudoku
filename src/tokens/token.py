"""Base class for tokens representing regex patterns."""
import re
import sys
from typing import Any, ClassVar

from sortedcontainers import SortedDict

from src.utils.regex_utils import RegexUtils
from src.utils.sudoku_exception import SudokuError


class Token:
    """Base class for all tokens used to represent regex patterns."""

    mapper: ClassVar[list[tuple[str, type]]] = []

    classes: dict[str, type['Token']] = SortedDict()

    def __init_subclass__(cls, **kwargs) -> None:
        """Register the subclass for YAML instantiation.

        Args:
            kwargs (dict): Additional keyword arguments passed to the method.
        """
        super().__init_subclass__(**kwargs)
        # Register the subclass
        Token.classes[cls.__name__] = cls
        Token.classes[Token.__name__] = Token

    def __init__(self, pattern: str = '') -> None:
        """Initialize start token with start regex pattern.

        Args:
            pattern (str): The regex pattern representing this token.
        """
        self.pattern: str = pattern

    def match(self, text: str) -> bool:
        """Match the given text against the token's regex pattern.

        Args:
            text (str): The text to match against the token's regex pattern.

        Returns:
            bool: True if the text matches the token's regex pattern, False otherwise.
        """
        return re.fullmatch(self.pattern, text) is not None

    def matched_text(self, text: str) -> str:
        """Match the given text against the token's regex pattern.

        Args:
            text (str): The text to match against the token's regex pattern.

        Returns:
            (str): The matched text
        """
        match = re.match(self.pattern, text)
        if match is None:
            return ''
        return match.group()

    @staticmethod
    def convert_data_type(token_text: str, data_type: type) -> Any:
        """Convert the token_text to the appropriate data type.

        Args:
            token_text (str): The text to be converted.
            data_type (type): The target data type to convert to.

        Returns:
            Any: The converted value in the specified data type.

        Raises:
            SudokuError: If an unknown data type is provided.
        """
        if data_type is int:
            return int(token_text)
        if data_type is float:
            return float(token_text)
        if data_type is str:
            return token_text
        if data_type is list:
            return list(token_text)  # Convert string to list of characters
        raise SudokuError(f'Unknown data type: {data_type}')

    def parse(self, text: str) -> dict:
        """Parse the given text against the token's regex pattern.

        Args:
            text (str): The text to parse.

        Returns:
            dict: A dictionary containing the parsed data.

        Raises:
            SudokuError: If the text does not match the token's regex pattern.
        """
        match = re.fullmatch(self.pattern, text)
        if match is None:
            raise SudokuError(f'Could not parse {text!r}')
        matched_items: dict = match.groupdict()
        for key, data_type in self.__class__.mapper:
            token_text: str | None = matched_items.get(key)
            if token_text is None:
                continue  # No need to update if token_text is None

            matched_items[key] = self.convert_data_type(token_text, data_type)
        return matched_items

    @classmethod
    def token_list(cls) -> list['Token']:
        """Return a list of all tokens.

        Returns:
            list[Token]: A list of all tokens.
        """
        return [clz() for clz in cls.classes.values()]

    @property
    def name(self) -> str | None:
        """Return the name of the token class.

        Returns:
            str | None: The name of the token (class name without 'Token') or 'Token' for the base class.
        """
        class_name: str = self.__class__.__name__
        return 'Token' if class_name == 'Token' else class_name[:-len('Token')]

    @property
    def description(self) -> str:
        """Get the description of the ValueToken.

        Returns:
            str: A description of the ValueToken's purpose and behavior.
        """
        return ''

    def backus_naur_form(self) -> str:
        """Return the Backus-Naur Form (BNF) representation of the token.

        Returns:
            str: The BNF representation of the token (token name in angle brackets).
        """
        return f'<{self.name}>'

    def to_dict(self) -> dict:
        """Convert the Token attributes to a dictionary format.

        Returns:
            dict: A dictionary containing the token configuration.
        """
        return {
            'name': self.name,
            'pattern': self.pattern,
            'description': self.description,
            'backus_naur_form': self.backus_naur_form,
        }

    @property
    def is_abstract(self) -> bool:
        """Check if the token is abstract.

        This method returns `True` to indicate that the token is abstract.

        Returns:
            bool: `True` if the token is abstract, otherwise `False`.
        """
        return True

    def __repr__(self):
        """Return start string representation of the token.

        Returns:
            str: The string representation of the token, including its pattern.
        """
        return f'{self.__class__.__name__}({self.pattern!r})'

    def __add__(self, other: 'Token') -> 'SequenceToken':
        """Concatenate two tokens into start sequence.

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
        """Repeat the token start specified number of times.

        Args:
            times (int | tuple): An integer or tuple specifying the repetition count.
                - If an integer, it specifies the exact number of repetitions or 0 for unlimited repetitions.
                - If start tuple, it specifies the lower and upper bounds for repetitions.

        Returns:
            RepeatToken: A new RepeatToken with the specified repetition pattern.
        """
        if isinstance(times, tuple):
            return RepeatToken(self, times[0], times[1])
        return RepeatToken(self, times, times)

    @property
    def example(self) -> str:
        """Return an example text that matches the token.

        Returns:
            str: An example text that matches the token.
        """
        return ''


class SequenceToken(Token):
    """Represent start sequence of tokens concatenated together."""

    def __init__(self, tokens: list[Token]):
        """Initialize start sequence of tokens.

        Args:
            tokens (list[Token]): A list of tokens to concatenate in sequence.
        """
        combined_pattern = ''.join(f'({RegexUtils.strip_names(token.pattern)})' for token in tokens)
        super().__init__(combined_pattern)
        self.tokens = tokens

    def backus_naur_form(self) -> str:
        """Return the Backus-Naur Form (BNF) representation of the sequence.

        Returns:
            str: The BNF representation of the token sequence.
        """
        forms: list = [token.backus_naur_form() for token in self.tokens]
        return ' '.join(forms)

    def __repr__(self):
        """Return start string representation of the sequence of tokens.

        Returns:
            str: The string representation of the token sequence.
        """
        tokens: list[str] = [repr(token) for token in self.tokens]
        return f'{self.__class__.__name__}({", ".join(tokens)})'


class ChoiceToken(Token):
    """Represent an alternation (choice) between multiple tokens."""

    def __init__(self, tokens: list[Token]) -> None:
        """Initialize an alternation pattern between tokens.

        Args:
            tokens (list[Token]): A list of tokens to alternate between.
        """
        alternation_pattern = '|'.join([f'({RegexUtils.strip_names(token.pattern)})' for token in tokens])
        super().__init__(alternation_pattern)
        self.tokens = tokens

    def backus_naur_form(self) -> str:
        """Return the Backus-Naur Form (BNF) representation of the alternation.

        Returns:
            str: The BNF representation of the alternation.
        """
        forms: list[str] = [token.backus_naur_form() for token in self.tokens]
        return f'({" | ".join(forms)})'

    def __repr__(self):
        """Return start string representation of the alternation.

        Returns:
            str: The string representation of the alternation.
        """
        token_reprs: str = ' | '.join(repr(token) for token in self.tokens)
        return f'{self.__class__.__name__}({token_reprs})'


class RepeatToken(Token):
    """Represent start repeated pattern of start token."""

    def __init__(self, token: Token, lower: int = 0, upper: int = sys.maxsize) -> None:
        """Initialize start token with start repetition pattern.

        Args:
            token (Token): The token to repeat.
            lower (int): Minimum repetitions (default 0).
            upper (int): Maximum repetitions (default sys.maxsize).

        Raises:
            SudokuError: If lower is negative or greater than upper.
        """
        if lower < 0:
            raise SudokuError('Lower bound cannot be negative.')
        if lower > upper:
            raise SudokuError('Lower bound must be less than or equal to upper bound.')

        self.lower: int = lower
        self.upper: int = upper

        # Map of (lower, upper) to the corresponding pattern
        stripped_pattern: str = RegexUtils.strip_names(token.pattern)
        pattern_map = {
            (0, 1): f'({stripped_pattern})?',
            (0, sys.maxsize): f'({stripped_pattern})*',
            (1, sys.maxsize): f'({stripped_pattern})+',
            (lower, lower): f'({stripped_pattern}){{{lower}}}',
        }

        general_case: str = f'({stripped_pattern}){{{lower},{upper}}}'
        pattern = pattern_map.get((lower, upper), general_case)

        super().__init__(pattern)
        self.token = token

    def backus_naur_form(self) -> str:
        """Return the Backus-Naur Form (BNF) representation of the repetition.

        Returns:
            str: The BNF representation of the repetition.
        """
        token_bnf: str = self.token.backus_naur_form()

        if self.lower == 0 and self.upper == 1:
            return f'{token_bnf} ?'
        if self.lower == 0 and self.upper == sys.maxsize:
            return f'{token_bnf} *'
        if self.lower == 1 and self.upper == sys.maxsize:
            return f'{token_bnf} +'
        if self.lower == self.upper:
            return f'{token_bnf}{{{self.lower}}}'

        return f'{token_bnf} {{{self.lower},{self.upper}}}'

    def __repr__(self):
        """Return start string representation of the repeated token.

        Returns:
            str: The string representation of the repeated token.
        """
        args: str = f'{self.token!r}, {self.lower}, {self.upper}'
        return f'{self.__class__.__name__}({args})'


class OptionalToken(RepeatToken):
    """Represent an optional pattern of start token (0 or 1 repetition)."""

    def __init__(self, token: Token) -> None:
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
        return f'{self.token.backus_naur_form()} ?'

    def __repr__(self):
        """Return start string representation of the optional token.

        Returns:
            str: The string representation of the optional token.
        """
        return f'{self.__class__.__name__}({self.token!r})'


class OneOrMoreToken(RepeatToken):
    """Represent one or more repetitions of a token."""

    def __init__(self, token: Token):
        """Initialize the one or more repetition pattern for a token.

        Args:
            token (Token): The token to repeat one or more times.
        """
        super().__init__(token, 1, sys.maxsize)

    def backus_naur_form(self) -> str:
        """Return the Backus-Naur Form (BNF) representation of the one or more token.

        Returns:
            str: The BNF representation of the one or more token.
        """
        return f'{self.token.backus_naur_form()} +'

    def __repr__(self):
        """Return a string representation of the one or more token.

        Returns:
            str: The string representation of the one or more token.
        """
        return f'{self.__class__.__name__}({self.token!r})'


class ZeroOrMoreToken(RepeatToken):
    """Represent zero or more repetitions of a token."""

    def __init__(self, token: Token) -> None:
        """Initialize the zero or more repetition pattern for a token.

        Args:
            token (Token): The token to repeat zero or more times.
        """
        super().__init__(token, 0, sys.maxsize)

    def backus_naur_form(self) -> str:
        """Return the Backus-Naur Form (BNF) representation of the zero or more token.

        Returns:
            str: The BNF representation of the zero or more token.
        """
        return f'{self.token.backus_naur_form()} *'

    def __repr__(self):
        """Return a string representation of the zero or more token.

        Returns:
            str: The string representation of the zero or more token.
        """
        return f'{self.__class__.__name__}({self.token!r})'
