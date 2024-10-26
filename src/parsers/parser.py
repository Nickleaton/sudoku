import re
from abc import abstractmethod
from typing import Any

from strictyaml import Regex


class ParserError(Exception):
    """Exception raised for errors in the Parser.

    Attributes:
        message (str): Explanation of the error.
    """

    def __init__(self, message: str):
        """Initializes ParserError with a message.

        Args:
            message (str): Explanation of the error.
        """
        super().__init__(message)


class Parser(Regex):
    """Abstract base class for parsers.

    This class extends Regex to provide a foundation for creating
    parsers that validate and process strings according to defined
    patterns.

    Attributes:
        result (Any): The result of the parsing operation.
    """

    def __init__(self, pattern: str):
        """Initializes the Parser with a regex pattern.

        Args:
            pattern (str): The regex pattern to be used for parsing.
        """
        super().__init__(pattern)
        self.regular_expression: re.Pattern = re.compile(pattern)
        self.pattern: str = pattern
        self.result: Any = None

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