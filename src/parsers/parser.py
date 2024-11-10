import re
from abc import abstractmethod
from typing import Optional, List, Dict, Type

from sortedcontainers import SortedDict
from strictyaml import Regex

from src.tokens.token import Token
from src.utils.sudoku_exception import SudokuException


class ParserError(SudokuException):
    """Exception raised for errors in the Parser."""
    pass


class Parser(Regex):
    """Abstract base class for parsers.

    This class extends Regex to provide a foundation for creating
    parsers that validate and process strings according to defined
    patterns.

    Attributes:
        result (Any): The result of the parsing operation.
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
        """
        Register the class so that it can be created from yaml.
        """
        super().__init_subclass__(**kwargs)
        # Register the class
        Parser.classes[cls.__name__] = cls
        Parser.classes[Parser.__name__] = Parser

    def __init__(self, pattern: str, example_format: Optional[str] = None):
        """Initializes the Parser with a regex pattern.

        Args:
            pattern (str): The regex pattern to be used for parsing.
        """
        super().__init__(pattern)
        self.regular_expression: re.Pattern = re.compile(pattern)
        self.example_format: str | None = example_format
        self.pattern: str = pattern
        self.token: Optional[Token] = None
        self.result: Optional[List] = None
        self.answer: Optional[Dict[str, str | List] | List] = None

    def help(self) -> str:
        return ""

    @abstractmethod
    def parse(self, text: str) -> None:
        """Parses the given text according to the implemented pattern.

        Args:
            text (str): The input string to parse.

        Raises:
            NotImplementedError: This method should be implemented in subclasses.
        """
        pass

    def __repr__(self) -> str:
        """Returns a string representation of the Parser object.

        Does not include the pattern for this class. This is because subclasses
        pass the pattern up from their __init__ method, and this would be redundant
        information. This clas is not meant to be instantiated directly.

        """
        return f"{self.__class__.__name__}()"

    def raise_error(self) -> None:
        self.result = None
        self.answer = None
        raise ParserError(f"{self.__class__.__name__} expects valid input in the format '{self.example_format}'.")
