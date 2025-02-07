"""Parser."""
from sortedcontainers import SortedDict
from strictyaml import Regex

from src.tokens.token import Token
from src.utils.regex_utils import RegexUtils
from src.utils.sudoku_exception import SudokuError


class ParserError(SudokuError):
    """Exception raised for errors in the Parser.

    This exception is used when a parsing error occurs, indicating that
    the input string does not match the expected format or is invalid.
    """


class Parser(Regex):
    """Abstract base class for parsers."""

    token: Token = Token()

    classes: dict[str, type['Parser']] = SortedDict({})

    # Creation Routines

    def __init_subclass__(cls, **kwargs) -> None:
        """Register the class so that it can be created from yaml.

        This method is automatically called when a subclass of `Parser` is defined.
        It registers the subclass in the `Parser.classes` dictionary so that
        it can be dynamically instantiated from YAML input.

        Args:
            kwargs: Additional keyword arguments passed during subclass initialization.
        """
        super().__init_subclass__(**kwargs)
        Parser.classes[cls.__name__] = cls
        Parser.classes[Parser.__name__] = Parser

    def __init__(self) -> None:
        """Initialize the Parser with a regex pattern."""
        super().__init__(RegexUtils.strip_names(self.__class__.token.pattern))

    def help(self) -> str:
        """Provide help or description for the parser.

        This method can be overridden by subclasses to provide specific help text
        explaining the expected format for input strings.

        Returns:
            str: Help text describing the expected input format.
        """
        return ''

    def parse(self, text: str) -> dict:
        """Parse the given text according to the implemented pattern.

        Args:
            text (str): The input text to be parsed

        Returns:
            dict: A dictionary containing the parsed data.
        """
        return self.token.parse(text)
