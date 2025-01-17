"""Board."""
import re
from enum import Enum

import oyaml as yaml
from sortedcontainers import SortedDict
from strictyaml import Map, Optional, Str, Validator

from src.utils.coord import Coord
from src.utils.cyclic import Cyclic
from src.utils.functions import PRIMES
from src.utils.side import Side
from src.utils.sudoku_exception import SudokuException
from src.utils.tags import Tags


class BoardType(Enum):
    """Types of boards.

    This enum defines the available board types.
    """

    b9x9 = '9x9'
    b4x4 = '4x4'
    b6x6 = '6x6'
    b8x8 = '8x8'


class BoxType(Enum):
    """Types of boxes.

    This enum defines the available box types for Sudoku grids.
    """

    b3x3 = '3x3'
    b2x3 = '2x3'
    b3x2 = '3x2'
    b2x2 = '2x2'


class Board:
    """Represents the starting Sudoku board.

    This class represents a Sudoku board with configurable dimensions,
    box sizes, and optional metadata. It supports various validation checks
    and operations to manage the board and its cells.
    """

    def __init__(
        self,
        board_rows: int,
        board_columns: int,
        # box_rows: int = 0,
        # box_columns: int = 0,
        tags: Tags | None = None,
    ):
        """Initialize the Board with dimensions, box size, and optional metadata.

        Args:
            board_rows (int): Number of rows in the board.
            board_columns (int): Number of columns in the board.
            # box_rows (int): Number of rows in each box. Defaults to 0 (no boxes).
            # box_columns (int): Number of columns in each box. Defaults to 0 (no boxes).
            tags (Tags | None): Dictionary containing optional metadata like 'reference', 'video', 'title', 'author'.

        Raises:
            SudokuException: If the board dimensions are not divisible by the box dimensions.
        """
        # Rows and Columns
        self.board_rows = board_rows
        self.board_columns = board_columns
        self.row_range = list(range(1, self.board_rows + 1))
        self.column_range = list(range(1, self.board_columns + 1))
        self.side_bounds: dict[Side, tuple[int, int]] = {
            Side.top: (1, self.board_columns),
            Side.bottom: (1, self.board_columns),
            Side.left: (1, self.board_rows),
            Side.right: (1, self.board_rows),
        }

        # Digits
        self.minimum_digit = 1
        self.maximum_digit = max(self.board_rows, self.board_columns)
        self.digit_range = list(range(self.minimum_digit, self.maximum_digit + 1))
        self.digit_sum = sum(self.digit_range)
        self.primes = [prime for prime in PRIMES if prime in self.digit_range]

        # Digit Levels
        chunk_size: int = self.maximum_digit // 3
        self.levels = ['low', 'mid', 'high']
        self.low = self.digit_range[:chunk_size]
        self.mid = self.digit_range[chunk_size:chunk_size * 2]
        self.high = self.digit_range[chunk_size * 2:]

        # Modulo Buckets
        self.modulos = [0, 1, 2]
        self.mod_buckets = {
            mod: [digit for digit in self.digit_range if digit % 3 == mod]
            for mod in self.modulos
        }

        # # Boxes
        # if box_rows == 0:
        #     self.box_rows = 0
        #     self.box_columns = 0
        #     self.box_count = 0
        #     self.box_range = None
        # else:
        #     if board_rows % box_rows != 0 or board_columns % box_columns != 0:
        #         raise SudokuException(
        #             f'Board dimensions ({board_rows}x{board_columns}) '
        #             f'must be divisible by box dimensions ({box_rows}x{box_columns}).',
        #         )
        #     self.box_rows = box_rows
        #     self.box_columns = box_columns
        #     self.box_count = (board_rows // box_rows) * (board_columns // box_columns)
        #     self.box_range = list(range(1, self.box_count + 1))

        # Metadata
        self.tags: Tags | None = None if tags is None else Tags(tags)

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
        for row in range(self.board_rows):
            # Left side (clockwise and anticlockwise)
            scm[(Side.left, Cyclic.clockwise, row)] = Coord(row - 1, 1)
            scm[(Side.left, Cyclic.anticlockwise, row)] = Coord(row + 1, 1)
            # Right side (clockwise and anticlockwise)
            scm[(Side.right, Cyclic.clockwise, row)] = Coord(row + 1, self.board_columns)
            scm[(Side.right, Cyclic.anticlockwise, row)] = Coord(row - 1, self.board_columns)

        # Top and bottom column connections (top-bottom)
        for column in range(self.board_columns):
            # Top side (clockwise and anticlockwise)
            scm[(Side.top, Cyclic.clockwise, column)] = Coord(1, column + 1)
            scm[(Side.top, Cyclic.anticlockwise, column)] = Coord(1, column - 1)
            # Bottom side (clockwise and anticlockwise)
            scm[(Side.bottom, Cyclic.clockwise, column)] = Coord(self.board_rows, column - 1)
            scm[(Side.bottom, Cyclic.anticlockwise, column)] = Coord(self.board_rows, column + 1)

        return scm

    def is_valid(self, row: int, column: int) -> bool:
        """Check if the given row and column coordinate is valid within the board.

        Args:
            row (int): Row number.
            column (int): Column number.

        Returns:
            bool: True if the coordinates are within bounds, False otherwise.
        """
        return (1 <= row <= self.board_rows) and (1 <= column <= self.board_columns)

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
        is_outer_row = coord.row in {0, self.board_rows + 1}
        is_column_in_range = 0 <= coord.column <= self.board_columns + 1

        is_outer_column = coord.column in {0, self.board_columns + 1}
        is_row_in_range = 0 <= coord.row <= self.board_rows + 1

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
            return Coord(self.board_rows + 1, index)
        if side == Side.left:
            return Coord(index, 0)
        if side == Side.right:
            return Coord(index, self.board_columns + 1)

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
                'Board': Str(),
                # Optional('Box'): Str(),
                Optional('Tags'): tag_schema,
            },
        )

    @staticmethod
    def parse_xy(text: str) -> tuple[int, int]:
        """Parse a string of the form 'NxM' into two integers.

        Args:
            text (str): String representing dimensions, e.g., "9x9".

        Returns:
            tuple[int, int]: Parsed (row, column) dimensions.

        Raises:
            SudokuException: If the string format is invalid.
        """
        regexp = re.compile('([1234567890]+)x([1234567890]+)')
        match = regexp.match(text)
        if match is None:
            raise SudokuException(f'Invalid format: {text}. Expected "NxM".')
        return int(match.group(1)), int(match.group(2))

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
        board_rows: int
        board_columns: int
        board_rows, board_columns = Board.parse_xy(board_data['Board'])
        # box_rows: int = 0
        # box_columns: int = 0
        # if board_data.get('Box') is not None:
        #     box_rows, box_columns = Board.parse_xy(board_data['Box'])
        tags: dict | None = SortedDict(board_data.get('Tags'))
        return Board(board_rows, board_columns, box_rows, box_columns, tags)

    @classmethod
    def create2(cls, name: str, yaml_data: dict) -> 'Board':
        """Create a Board instance using the provided name and YAML line.

        Args:
            name (str): The name key for the board in the YAML line.
            yaml_data (dict): The YAML line dictionary containing the board configuration.

        Returns:
            Board: A new `Board` instance created based on the provided YAML line.
        """
        return cls.create(name, yaml_data)

    def to_dict(self) -> dict:
        """Convert the Board attributes to a dictionary format for YAML serialization.

        Returns:
            dict: A dictionary containing the board configuration.
        """
        board_dict: dict = {'Board': {}}
        board = board_dict['Board']

        board['Board'] = f'{self.board_rows}x{self.board_columns}'

        # if self.box_rows is not None and self.box_columns is not None:
        #     board['Box'] = f'{self.box_rows}x{self.box_columns}'

        if self.tags is not None:
            board['Tags'] = dict(self.tags)
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
            f'{self.board_rows!r}, '
            f'{self.board_columns!r}, '
            # f'{self.box_rows!r}, '
            # f'{self.box_columns!r}, '
            f'{self.tags!r}'
            f')'
        )

    # def box_index(self, row: int, column: int) -> int:
    #     """Determine the box index for a given cell specified by row and column.
    #
    #     Args:
    #         row (int): Row coordinate of the cell.
    #         column (int): Column coordinate of the cell.
    #
    #     Returns:
    #         int: Box index number.
    #     """
    #     return ((row - 1) // self.box_rows) * self.box_rows + (column - 1) // self.box_columns + 1
    #
    @property
    def digit_values(self) -> str:
        """Return a string of valid digits for the board.

        Returns:
            str: A string of digits available on the board.
        """
        return ''.join([str(digit) for digit in self.digit_range])

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
            return Coord(index, self.board_rows + 1)
        if side == Side.bottom:
            return Coord(self.board_columns + 1, index)
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
            return Coord(index, self.board_rows)
        if side == Side.bottom:
            return Coord(self.board_columns, index)
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
            return Coord(index, self.board_rows + 1)
        if side == Side.bottom:
            return Coord(self.board_columns + 1, index)
        if side == Side.left:
            return Coord(index, 0)
        raise ValueError(f'Invalid side: {side}')
