import re
from enum import Enum
from typing import Optional, Dict, Tuple

import oyaml as yaml
import strictyaml
from strictyaml import Validator

from src.utils.coord import Coord
from src.utils.functions import PRIMES


class BoardType(Enum):
    """Types of boards."""

    B9X9 = "9x9"
    B4X4 = "4x4"
    B6X6 = "6x6"
    B8X8 = "8x8"


class BoxType(Enum):
    """Types of boxes."""

    B3X3 = "3x3"
    B2X3 = "2x3"
    B3X2 = "3x2"
    B2X2 = "2x2"


class Board:
    """Represents a Sudoku board."""

    # pylint: disable=too-many-arguments, too-many-instance-attributes
    def __init__(self,
                 board_rows: int,
                 board_columns: int,
                 box_rows: int = 0,
                 box_columns: int = 0,
                 reference: Optional[str] = None,
                 video: Optional[str] = None,
                 title: Optional[str] = None,
                 author: Optional[str] = None
                 ):
        """Initialize the Board with rows, columns, box dimensions, and optional metadata.

        Args:
            board_rows (int): Number of rows in the board.
            board_columns (int): Number of columns in the board.
            box_rows (int, optional): Number of rows in each box. Defaults to 0.
            box_columns (int, optional): Number of columns in each box. Defaults to 0.
            reference (Optional[str], optional): Reference URL for the puzzle, if available. Defaults to None.
            video (Optional[str], optional): Video link related to the puzzle, if available. Defaults to None.
            title (Optional[str], optional): Title of the puzzle, if available. Defaults to None.
            author (Optional[str], optional): Author of the puzzle, if available. Defaults to None.
        """
        # Rows
        self.board_rows = board_rows
        self.row_range = list(range(1, self.board_rows + 1))
        # Columns
        self.board_columns = board_columns
        self.column_range = list(range(1, self.board_columns + 1))
        # Digits
        self.minimum_digit = 1
        self.maximum_digit = max(self.board_rows, self.board_columns)
        self.digit_range = list(range(self.minimum_digit, self.maximum_digit + 1))
        self.digit_sum = sum(self.digit_range)
        self.primes = [p for p in PRIMES if p in self.digit_range]
        chunk_size: int = self.maximum_digit // 3

        self.levels = ['low', 'mid', 'high']
        self.low = self.digit_range[:chunk_size]
        self.mid = self.digit_range[chunk_size:chunk_size * 2]
        self.high = self.digit_range[chunk_size * 2:]

        self.modulos = [0, 1, 2]
        self.mod0 = [d for d in self.digit_range if d % 3 == 0]
        self.mod1 = [d for d in self.digit_range if d % 3 == 1]
        self.mod2 = [d for d in self.digit_range if d % 3 == 2]

        # Boxes
        if box_rows == 0:
            self.box_rows = 0
            self.box_columns = 0
            self.box_count = 0
            self.box_range = None
        else:
            assert board_rows % box_rows == 0
            assert board_columns % box_columns == 0
            self.box_rows = box_rows
            self.box_columns = box_columns
            self.box_count = (board_rows // box_rows) * (board_columns // box_columns)
            self.box_range = list(range(1, self.box_count + 1))
        # meta data
        self.reference = reference
        self.video = video
        self.title = title
        self.author = author

    def is_valid(self, row: int, column: int) -> bool:
        """Check if a given row and column coordinate is valid within the board.

        Args:
            row (int): Row number.
            column (int): Column number.

        Returns:
            bool: True if the coordinate is within bounds, False otherwise.
        """
        return (1 <= row <= self.board_rows) and (1 <= column <= self.board_columns)

    def is_valid_coordinate(self, coord: Coord) -> bool:
        """Check if a given coordinate is valid within the board.

        Args:
            coord (Coord): Coordinate to check.

        Returns:
            bool: True if the coordinate is within bounds, False otherwise.
        """
        return self.is_valid(int(coord.row), int(coord.column))

    @classmethod
    def schema(cls) -> Validator:
        """Define the YAML schema for the board configuration.

        Returns:
            Validator: A `strictyaml` validator for the board configuration.
        """
        return strictyaml.Map(
            {
                'Board': strictyaml.Str(),
                strictyaml.Optional('Box'): strictyaml.Str(),
                strictyaml.Optional('Video'): strictyaml.Str(),
                strictyaml.Optional('Reference'): strictyaml.Str(),
                strictyaml.Optional('Author'): strictyaml.Str(),
                strictyaml.Optional('Title'): strictyaml.Str()
            }
        )

    @staticmethod
    def parse_xy(s: str) -> Tuple[int, int]:
        """Parse a string of the form 'NxM' into two integers.

        Args:
            s (str): String representing dimensions, e.g., "9x9".

        Returns:
            Tuple[int, int]: Parsed (row, column) dimensions.

        Raises:
            AssertionError: If the input string does not match the expected format.
        """
        regexp = re.compile("([1234567890]+)x([1234567890]+)")
        match = regexp.match(s)
        assert match is not None
        row_str, column_str = match.groups()
        return int(row_str), int(column_str)

    @classmethod
    def create(cls, name: str, yaml_data: Dict) -> 'Board':
        """Create a Board instance from a YAML data structure.

        Args:
            name (str): Name key for the board in the YAML data.
            yaml_data (Dict[str, Any]): YAML data dictionary containing board configuration.

        Returns:
            Board: A new `Board` instance.
        """
        y: Dict = yaml_data[name]
        board_rows: int
        board_columns: int
        board_rows, board_columns = Board.parse_xy(y['Board'])
        box_rows: int = 0
        box_columns: int = 0
        if 'Box' in y:
            box_rows, box_columns = Board.parse_xy(y['Box'])

        reference: str | None = y.get('Reference')
        video: str | None = y.get('Video')
        title: str | None = y.get('Title')
        author: str | None = y.get('Author')
        return Board(
            board_rows,
            board_columns,
            box_rows,
            box_columns,
            reference,
            video,
            title,
            author
        )

    def to_dict(self) -> Dict:
        """Convert the Board attributes to a dictionary format for YAML serialization.

        Returns:
            Dict[str, Any]: Dictionary containing board configuration.
        """
        result: Dict = {'Board': {}}
        result['Board']['Board'] = f"{self.board_rows}x{self.board_columns}"
        if self.box_rows is not None:
            result['Board']['Box'] = f"{self.box_rows}x{self.box_columns}"
        if self.reference is not None:
            result['Board']['Reference'] = self.reference
        if self.reference is not None:
            result['Board']['Video'] = self.video
        if self.reference is not None:
            result['Board']['Title'] = self.title
        if self.reference is not None:
            result['Board']['Author'] = self.author
        return result

    def to_yaml(self) -> str:
        """Convert the Board instance to a YAML-formatted string.

        Returns:
            str: YAML-formatted representation of the board configuration.
        """
        return str(yaml.dump(self.to_dict()))

    def __repr__(self) -> str:
        """Provide a string representation of the Board instance for debugging.

        Returns:
            str: A string describing the Board instance with key attributes.
        """
        return (
            f"{self.__class__.__name__}"
            f"("
            f"{self.board_rows!r}, "
            f"{self.board_columns!r}, "
            f"{self.box_rows!r}, "
            f"{self.box_columns!r}, "
            f"{self.reference!r}, "
            f"{self.video!r}, "
            f"{self.title!r}, "
            f"{self.author!r}"
            f")"
        )

    def box_index(self, row: int, column: int) -> int:
        """Determine the box index for a given cell specified by row and column.

        Args:
            row (int): Row coordinate of the cell.
            column (int): Column coordinate of the cell.

        Returns:
            int: Box index number.
        """
        return ((row - 1) // self.box_rows) * self.box_rows + (column - 1) // self.box_columns + 1

    @property
    def digit_values(self) -> str:
        """Return a string of valid digits for the board.

        Returns:
            str: A string of digits available on the board.
        """
        return "".join([str(digit) for digit in self.digit_range])
