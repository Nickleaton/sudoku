"""Board."""
import re
from enum import Enum

import oyaml as yaml
from strictyaml import Map, Optional, Str, Validator

from src.board.digits import Digits
from src.parsers.board_digits_parser import BoardDigitsParser
from src.parsers.size_parser import SizeParser
from src.utils.coord import Coord
from src.utils.cyclic import Cyclic
from src.utils.side import Side
from src.utils.sudoku_exception import SudokuError
from src.utils.tags import Tags


class BoardType(Enum):
    """Types of boards.

    This enum defines the available board types.
    """

    b9x9 = '9x9'
    b4x4 = '4x4'
    b6x6 = '6x6'
    b8x8 = '8x8'
    b16x16 = '16x16'


class BoxType(Enum):
    """Types of boxes.

    This enum defines the available box types for Sudoku grids.
    """

    b2x2 = '2x2'
    b3x3 = '3x3'
    b2x3 = '2x3'
    b3x2 = '3x2'
    b4x4 = '4x4'


class Board:
    """Represents the starting Sudoku board.

    This class represents a Sudoku board with configurable dimensions,
    box sizes, and optional metadata. It supports various validation checks
    and operations to manage the board and its cells.
    """

    def __init__(
        self,
        size: Coord,
        digits: Digits,
        tags: Tags,
    ):
        """Initialize the Board with dimensions, box size, and optional metadata.little_killer_validator.

        Args:
            size (Coord): Number of rows in the board.
            digits (Digits): Collection of digits used in the board.
            tags (Tags): Dictionary containing optional metadata like 'reference', 'video', 'title', 'author'.
        """
        self.size: Coord = size
        self.row_range = list(range(1, self.size.row + 1))
        self.column_range = list(range(1, self.size.column + 1))
        self.side_bounds: dict[Side, tuple[int, int]] = {
            Side.top: (1, self.size.column),
            Side.bottom: (1, self.size.column),
            Side.left: (1, self.size.row),
            Side.right: (1, self.size.row),
        }

        self.digits: Digits = digits

        # Metadata
        self.tags: Tags = tags

        # Cyclic Map

        self.side_cyclic_map: dict[tuple[Side, Cyclic, int], Coord] = self.generate_cyclic_map()

    def generate_cyclic_map(self) -> dict[tuple[Side, Cyclic, int], Coord]:
        """Generate a cyclic map for a board with cyclic connections along each side.

        The map contains the following entries:
        - Top row: connects left and right sides in both clockwise and anticlockwise directions.
        - Bottom row: connects left and right sides in both clockwise and anticlockwise directions.
        - Left column: connects top and bottom sides in both clockwise and anticlockwise directions.
        - Right column: connects top and bottom sides in both clockwise and anticlockwise directions.

        Returns:
            dict: A dictionary where the keys are tuples of (Side, Cyclic, integer). The cell_values are Coord objects
            representing the corresponding board coordinates.
        """
        scm: dict[tuple[Side, Cyclic, int], Coord] = {}

        # Top and bottom row connections (left-right)
        for row in range(self.size.row):
            # Left side (clockwise and anticlockwise)
            scm[(Side.left, Cyclic.clockwise, row)] = Coord(row - 1, 1)
            scm[(Side.left, Cyclic.anticlockwise, row)] = Coord(row + 1, 1)
            # Right side (clockwise and anticlockwise)
            scm[(Side.right, Cyclic.clockwise, row)] = Coord(row + 1, self.size.column)
            scm[(Side.right, Cyclic.anticlockwise, row)] = Coord(row - 1, self.size.column)

        # Top and bottom column connections (top-bottom)
        for column in range(self.size.column):
            # Top side (clockwise and anticlockwise)
            scm[(Side.top, Cyclic.clockwise, column)] = Coord(1, column + 1)
            scm[(Side.top, Cyclic.anticlockwise, column)] = Coord(1, column - 1)
            # Bottom side (clockwise and anticlockwise)
            scm[(Side.bottom, Cyclic.clockwise, column)] = Coord(self.size.row, column - 1)
            scm[(Side.bottom, Cyclic.anticlockwise, column)] = Coord(self.size.row, column + 1)

        return scm

    def is_valid(self, row: int, column: int) -> bool:
        """Check if the given row and column coordinate is valid within the board.

        Args:
            row (int): Row number.
            column (int): Column number.

        Returns:
            bool: True if the coordinates are within bounds, False otherwise.
        """
        return (1 <= row <= self.size.row) and (1 <= column <= self.size.column)

    def is_valid_coordinate(self, coord: Coord) -> bool:
        """Check if start_location given coordinate is valid within the board.

        Args:
            coord (Coord): Coordinate to check.

        Returns:
            bool: True if the coordinate is within bounds, False otherwise.
        """
        return self.is_valid(int(coord.row), int(coord.column))

    def is_valid_side_index(self, coord: Coord) -> bool:
        """Check if the coordinate refers to a cell just outside the board boundary.

        Args:
            coord (Coord): Coordinate to check.

        Returns:
            bool: True if the coordinate is just outside the boundary, False otherwise.
        """
        is_outer_row = coord.row in {0, self.size.row + 1}
        is_column_in_range = 0 <= coord.column <= self.size.column + 1

        is_outer_column = coord.column in {0, self.size.column + 1}
        is_row_in_range = 0 <= coord.row <= self.size.row + 1

        return (is_outer_row and is_column_in_range) or (is_outer_column and is_row_in_range)

    def get_side_coordinate(self, side: Side, index: int) -> Coord:
        """Get the coordinate for the given side of the board and index.

        Args:
            side (Side): The side of the board (top, bottom, left, right).
            index (int): The index along the side (1-based for rows/columns).

        Returns:
            Coord: The coordinate representing the location on the board's boundary.

        Raises:
            ValueError: If the side is invalid or the index is out of range.
        """
        if side not in self.side_bounds:
            raise ValueError(f'Invalid side: {side}')

        min_index, max_index = self.side_bounds[side]

        if index < min_index or index > max_index:
            raise ValueError(f'Index {index} out of range for {side.name} side.')

        if side == Side.top:
            return Coord(0, index)
        if side == Side.bottom:
            return Coord(self.size.row + 1, index)
        if side == Side.left:
            return Coord(index, 0)
        if side == Side.right:
            return Coord(index, self.size.column + 1)

        # Should never reach here due to the initial side validation
        raise ValueError(f'Unhandled side: {side}')

    @classmethod
    def schema(cls) -> Validator:
        """Define the YAML schema for the board configuration.

        Returns:
            Validator: A `strictyaml` validator for the board configuration.
        """
        valid_tags: list[str] = ['Title', 'Reference', 'Video', 'Author']
        tag_schema: Map = Map({Optional(key): Str() for key in valid_tags})
        return Map(
            {
                'Size': SizeParser(),
                'Digits': BoardDigitsParser(),
                Optional('Tags'): tag_schema,
            },
        )

    @staticmethod
    def parse_size(text: str) -> Coord:
        """Parse a string of the form 'NxM' into two integers.

        Args:
            text (str): String representing dimensions, exp.g., "9x9".

        Returns:
            Coord: Parsed (row, column) dimensions as a Coord object.

        Raises:
            SudokuError: If the string format is invalid.
        """
        regexp = re.compile('([1234567890]+)x([1234567890]+)')
        match = regexp.match(text)
        if match is None:
            raise SudokuError(f'Invalid format: {text}. Expected "NxM".')
        return Coord(int(match.group(1)), int(match.group(2)))

    @staticmethod
    def parse_digits(text: str) -> Digits:
        """Parse a string of the form 'a..b' into two integers.

        Args:
            text (str): String representing digits, exp.g., "1..9".

        Returns:
            Digits: Parsed (start, end) digits.

        Raises:
            SudokuError: If the string format is invalid.
        """
        regexp = re.compile('([123456789])..([123456789])')
        match = regexp.match(text)
        if match is None:
            raise SudokuError(f'Invalid format: {text}. Expected "a..b".')
        return Digits(int(match.group(1)), int(match.group(2)))

    @classmethod
    def create(cls, name: str, yaml_data: dict) -> 'Board':
        """Create start_location Board instance from start_location YAML line structure.

        Args:
            name (str): Name key for the board in the YAML line.
            yaml_data (dict): YAML line dictionary containing board configuration.

        Returns:
            Board: A new `Board` instance.
        """
        board_data: dict = yaml_data[name]
        size: Coord = Board.parse_size(board_data['Size'])
        digits: Digits = Board.parse_digits(board_data['Digits'])
        tags: Tags = Tags(board_data.get('Tags'))
        return Board(size, digits, tags)

    @classmethod
    def create2(cls, yaml_data: dict) -> 'Board':
        """Create a Board instance using the provided name and YAML line.

        Args:
            yaml_data (dict): The YAML line dictionary containing the board configuration.

        Returns:
            Board: A new `Board` instance created based on the provided YAML line.
        """
        return Board(Coord(9, 9), Digits(1, 9), Tags({'len': len(yaml_data)}))

    def to_dict(self) -> dict:
        """Convert the Board attributes to a dictionary format for YAML serialization.

        Returns:
            dict: A dictionary containing the board configuration.
        """
        board_dict: dict = {'Board': {}}
        board_dict['Board']['Size'] = f'{self.size.row}x{self.size.column}'
        board_dict['Board']['Digits'] = f'{self.digits.minimum}..{self.digits.maximum}'
        board_dict['Board']['Tags'] = dict(self.tags)
        return board_dict

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
            f'{self.__class__.__name__}'
            f'('
            f'{self.size!r}, '
            f'{self.digits!r}, '
            f'{self.tags!r}'
            f')'
        )

    def marker(self, side: Side, index: int) -> Coord:
        """Get the marker coordinate for a specified side on the board.

        Args:
            side (Side): The side of the board.
            index (int): The index for the side.

        Returns:
            Coord: The coordinate of the marker.

        Raises:
            ValueError: If the side is invalid.
        """
        if side == Side.top:
            return Coord(0, index)
        if side == Side.right:
            return Coord(index, self.size.row + 1)
        if side == Side.bottom:
            return Coord(self.size.column + 1, index)
        if side == Side.left:
            return Coord(index, 0)
        raise ValueError(f'Invalid side: {side}')

    def start_cell(self, side: Side, index: int) -> Coord:
        """Get the starting cell coordinate for a specified side on the board.

        Args:
            side (Side): The side of the board.
            index (int): The index for the side.

        Returns:
            Coord: The coordinate of the starting cell.

        Raises:
            ValueError: If the side is invalid.
        """
        if side == Side.top:
            return Coord(1, index)
        if side == Side.right:
            return Coord(index, self.size.row)
        if side == Side.bottom:
            return Coord(self.size.column, index)
        if side == Side.left:
            return Coord(index, 1)
        raise ValueError(f'Invalid side: {side}')

    def outside_cell(self, side: Side, index: int) -> Coord:
        """Get the outside cell coordinate for a specified side on the board. Used by little killers.

        Args:
            side (Side): The side of the board.
            index (int): The index for the side.

        Returns:
            Coord: The coordinate of the starting cell.

        Raises:
            ValueError: If the side is invalid.
        """
        if side == Side.top:
            return Coord(0, index)
        if side == Side.right:
            return Coord(index, self.size.row + 1)
        if side == Side.bottom:
            return Coord(self.size.column + 1, index)
        if side == Side.left:
            return Coord(index, 0)
        raise ValueError(f'Invalid side: {side}')
