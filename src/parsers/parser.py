"""Parser."""
import re
from typing import Optional, List, Dict, Type

from sortedcontainers import SortedDict
from strictyaml import Regex

from src.tokens.token import Token
from src.utils.sudoku_exception import SudokuException


class ParserError(SudokuException):
    """Exception raised for errors in the Parser.

    This exception is used when a parsing error occurs, indicating that
    the input string does not match the expected format or is invalid.
    """


class Parser(Regex):
    """Abstract base class for parsers.

    This class extends Regex to provide a foundation for creating
    parsers that validate and process strings according to defined
    patterns. It includes mechanisms for matching input strings with
    regular expressions and handling the results.

    Attributes:
        result (Any): The result of the parsing operation, can vary based on the implementation.
        classes (Dict[str, Type['Parser']]): A dictionary of subclasses, used for dynamic class registration.
        pattern (str): The regular expression pattern used for parsing.
        example_format (Optional[str]): A string example format for expected input.
        token (Optional[Token]): A token used for further processing or validation.
        answer (Optional[Dict[str, str | List] | List]): The parsed result,
                can be a list or a dictionary depending on the implementation.
    """

    DIGIT = r"(\d)"
    CELL = r"(\d\d)"
    VALUE = r"(\d+)"
    SIDE = r"([TLBR])"
    KNOWN = r"([0-9.lmheof])"
    DIRECTION = r"([CA])"
    QUAD = r"([\d?]+)"
    COMMA = r","
    EQUALS = r"="

    classes: Dict[str, Type['Parser']] = SortedDict({})

    # Creation Routines

    def __init_subclass__(cls, **kwargs):
        """Register the class so that it can be created from yaml.

        This method is automatically called when a subclass of `Parser` is defined.
        It registers the subclass in the `Parser.classes` dictionary so that
        it can be dynamically instantiated from YAML input.

        Args:
            **kwargs: Additional keyword arguments passed during subclass initialization.
        """
        super().__init_subclass__(**kwargs)
        Parser.classes[cls.__name__] = cls
        Parser.classes[Parser.__name__] = Parser

    def __init__(self, pattern: str, example_format: Optional[str] = None):
        """Initialize the Parser with a regex pattern.

        This constructor sets up the regular expression for parsing, along with
        an optional example format string that can be used to explain expected
        input formats to the user.

        Args:
            pattern (str): The regex pattern to be used for parsing.
            example_format (Optional[str]): An optional example format for expected input.
        """
        super().__init__(pattern)
        self.regular_expression: re.Pattern = re.compile(pattern)
        self.example_format: Optional[str] = example_format
        self.pattern: str = pattern
        self.token: Optional[Token] = None
        self.result: Optional[List] = None
        self.answer: Optional[Dict[str, str | List] | List] = None

    def help(self) -> str:
        """Provide help or description for the parser.

        This method can be overridden by subclasses to provide specific help text
        explaining the expected format for input strings.

        Returns:
            str: Help text describing the expected input format.
        """
        return ""

    def parse(self, text: str) -> None:
        """Parse the given text according to the implemented pattern.

        This method is meant to be overridden by subclasses, as it will contain
        the specific parsing logic for each type of input string. It validates
        the input string against the pattern and processes it accordingly.

        Args:
            text (str): The input string to parse.

        Raises:
            NotImplementedError: This method should be implemented in subclasses.
        """

    def __repr__(self) -> str:
        """Return a string representation of the Parser object.

        This method provides a string representation of the parser object, excluding
        the regex pattern, which is handled by subclasses. The purpose is to show
        that this class is abstract and not meant to be instantiated directly.

        Returns:
            str: A string representation of the Parser object.
        """
        return f"{self.__class__.__name__}()"

    def raise_error(self) -> None:
        """Raise a ParserError for invalid input.

        This method resets the `result` and `answer` attributes to `None` and raises
        a `ParserError` with a message indicating that the input was not valid.

        Raises:
            ParserError: If the input does not match the expected format.
        """
        self.result = None
        self.answer = None
        raise ParserError(f"{self.__class__.__name__} expects valid input in the format '{self.example_format}'.")
