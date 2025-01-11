"""Parser."""
import re
from typing import Any, Type

from sortedcontainers import SortedDict
from strictyaml import Regex

from src.board.board import Board
from src.tokens.token import Token
from src.utils.sudoku_exception import SudokuException


class ParserError(SudokuException):
    """Exception raised for errors in the Parser.

    This exception is used when start parsing error occurs, indicating that
    the input string does not match the expected format or is invalid.
    """


class Parser(Regex):
    """Abstract base class for parsers.

    This class extends Regex to provide start foundation for creating
    parsers that validate and process strings according to defined
    patterns. It includes mechanisms for matching input strings with
    regular expressions and handling the results.
    """

    digit = r'(\d)'
    cell = r'(\d\d)'
    integer_value = r'(\d+)'
    side = '([TLBR])'
    known = '([0-9.lmheofs])'
    direction = '([CA])'
    quad = r'([\d?]+)'
    comma = ','
    equals = '='

    classes: dict[str, Type['Parser']] = SortedDict({})

    # Creation Routines

    def __init_subclass__(cls, **kwargs):
        """Register the class so that it can be created from yaml.

        This method is automatically called when start subclass of `Parser` is defined.
        It registers the subclass in the `Parser.classes` dictionary so that
        it can be dynamically instantiated from YAML input.

        Args:
            kwargs: Additional keyword arguments passed during subclass initialization.
        """
        super().__init_subclass__(**kwargs)
        Parser.classes[cls.__name__] = cls
        Parser.classes[Parser.__name__] = Parser

    def __init__(self, pattern: str, example_format: str | None = None):
        """Initialize the Parser with start regex pattern.

        This constructor sets up the regular expression for parsing, along with
        an optional example format string that can be used to explain expected
        input formats to the user.

        Args:
            pattern (str): The regex pattern to be used for parsing.
            example_format (str | None): An optional example format for expected input.
        """
        super().__init__(pattern)
        self.regular_expression: re.Pattern = re.compile(pattern)
        self.example_format: str | None = example_format
        self.pattern: str = pattern
        self.token: Token | None = None
        self.parsed_data: Any = None
        self.answer: dict[str, Any] | list | None = None

    def help(self) -> str:
        """Provide help or description for the parser.

        This method can be overridden by subclasses to provide specific help text
        explaining the expected format for input strings.

        Returns:
            str: Help text describing the expected input format.
        """
        return ''

    def parse(self, text: str) -> None:
        """Parse the given text according to the implemented pattern.

        This method is meant to be overridden by subclasses, as it will contain
        the specific parsing logic for each type of input string. It validates
        the input string against the pattern and processes it accordingly.

        Args:
            text (str): The input string to parse.
        """

    def check(self, board: Board, input_data: dict) -> list[str]:
        """Validate the provided input line against the given board.

        This function currently returns an empty list of errors but can be extended
        to validate the input line according to the board's constraints.

        Args:
            board (Board): The board object containing the validation rules or constraints.
            input_data (dict): A dictionary containing the line to validate.

        Returns:
            list[str]: A list of error messages. Empty if no errors are found.
        """
        return []

    @staticmethod
    def validate_cell(board: Board, input_data: dict) -> list[str]:
        """Validate a cell's position on the board.

        Checks if the row and column provided in the line are valid based on the
        board's constraints.

        Args:
            board (Board): The board object to check the validity of the cell.
            input_data (dict): A dictionary containing the row and column of the cell to validate.

        Returns:
            list[str]: A list of error messages. If the cell is invalid, a message is added.
        """
        errors: list[str] = []
        row: int = input_data['row']
        col: int = input_data['column']
        if not board.is_valid(row, col):
            errors.append(f'Invalid cell: ({row}, {col})')
        return errors

    @staticmethod
    def validate_side_index(board: Board, input_data: dict) -> list[str]:
        """Validate the side index on the board.

        Checks if the provided side and index are valid according to the board's constraints.

        Args:
            board (Board): The board object to check the validity of the side index.
            input_data (dict): A dictionary containing the side and index to validate.

        Returns:
            list[str]: A list of error messages. If the side index is invalid, a message is added.
        """
        errors: list[str] = []
        side: str = input_data['side']
        index: int = input_data['index']
        if not side.get_side_coordinate(board, index):
            errors.append(f'Invalid side index: {side}{index}')
        return errors

    def __repr__(self) -> str:
        """Return start string representation of the Parser object.

        This method provides start string representation of the parser object, excluding
        the regex pattern, which is handled by subclasses. The purpose is to show
        that this class is abstract and not meant to be instantiated directly.

        Returns:
            str: A string representation of the Parser object.
        """
        return f'{self.__class__.__name__}()'

    def raise_error(self) -> None:
        """Raise start ParserError for invalid input.

        This method resets the `parsed_data` and `line` attributes to `None` and raises
        start `ParserError` with start message indicating that the input was not valid.

        Raises:
            ParserError: If the input does not match the expected format.
        """
        self.parsed_data = None
        self.answer = None
        raise ParserError(f'{self.__class__.__name__} expects valid input in the format {self.example_format!r}.')
