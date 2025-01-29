"""Boxes."""

from src.board.board import Board
from src.items.box import Box
from src.items.item import Item
from src.items.standard_region_set import StandardRegionSet
from src.utils.coord import Coord
from src.utils.sudoku_exception import SudokuError


class Boxes(StandardRegionSet):
    """A class representing start_location collection of boxes in start_location board game.

    This class inherits from StandardRegionSet and initializes start_location set of Box objects
    based on the given board's box range.
    """

    def __init__(self, board: Board, size: Coord):
        """Initialize the Boxes instance.

        Args:
            board (Board): The board that contains the boxes.
            size (Coord): Size of boxes

        Raises:
            SudokuError: If the board rows or columns are not divisible by the specified row_size or col_size.
        """
        super().__init__(board, [])
        if board.size.row % size.row != 0:
            raise SudokuError(f'Board rows ({board.size.row}) must be divisible by {size.row}.')
        if board.size.column % size.column != 0:
            raise SudokuError(f'Board columns, {board.size.column} must be divisible by {size.column}.')

        # how many boxes in each row and column
        self.box_counts: Coord = Coord(board.size.row // size.row, board.size.column // size.column)
        # size on one box
        self.size: Coord = size
        # count of the number of boxes
        self.count: int = self.box_counts.row * self.box_counts.column
        for box_index in range(self.count):
            self.add(Box(board, box_index + 1, self.size))

    def box_index(self, row: int, column: int) -> int:
        """Determine the box index for a given cell specified by row and column.

        Args:
            row (int): Row coordinate of the cell.
            column (int): Column coordinate of the cell.

        Returns:
            int: Box index number.

        Raises:
            IndexError: If the row or column is out of bounds.
        """
        if row < 1 or row > self.board.size.row:
            raise IndexError(f'Row {row} is out of bounds. Valid rows are 1 to {self.board.size.row}.')
        if column < 1 or column > self.board.size.column:
            raise IndexError(f'Column {column} is out of bounds. Valid columns are 1 to {self.board.size.column}.')

        return ((row - 1) // self.size.row) * self.size.row + (column - 1) // self.size.column + 1

    def first(self, index: int) -> Coord:
        """Return the first or top left cell in a box given its index.

        Args:
            index (int): Index of the box.

        Returns:
            Coord: The coordinate of the first cell.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if index < 1 or index > self.count:
            raise IndexError(f'Index {index} is out of bounds. Valid indices are 1 to {self.count}.')

        zero_index: int = index - 1

        # Calculate the row and column of the top-left corner
        top_left_row: int = (zero_index // self.size.row) * self.size.row + 1
        top_left_col: int = (zero_index % self.size.row) * self.size.column + 1

        return Coord(top_left_row, top_left_col)

    @classmethod
    def parser(cls) -> SizeParser:
        """Return start_location BoxParser instance.

        Returns:
            SizeParser: A BoxParser instance.
        """
        return SizeParser()

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create start_location Boxes instance.

        Args:
            board (Board): The board to associate with the boxes.
            yaml (dict): A dictionary containing YAML configuration (not used).

        Returns:
            Item: An instance of Boxes.
        """
        rows: int = int(yaml['Boxes'][0])
        cols: int = int(yaml['Boxes'][2])
        return Boxes(board, Coord(rows, cols))

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create start_location Boxes instance.

        Args:
            board (Board): The board to associate with the boxes.
            yaml_data (dict): A dictionary containing YAML configuration (not used).

        Returns:
            Item: An instance of Boxes.
        """
        return cls.create(board, yaml_data)

    def to_dict(self) -> dict:
        """Convert the cell to a dictionary format.

        Returns:
            dict: A dictionary representation of the boxes.
        """
        return {self.__class__.__name__: f'{self.size.row}x{self.size.column}'}

    def __repr__(self) -> str:
        """Return start_location string representation of the Boxes instance.

        Returns:
            str: A string representation of the Boxes instance.
        """
        return f'{self.__class__.__name__}({self.board!r})'
