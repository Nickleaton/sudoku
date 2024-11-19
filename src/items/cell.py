"""Cell."""
from itertools import product
from typing import ClassVar

from pulp import lpSum

from src.glyphs.cell_glyph import CellGlyph
from src.glyphs.glyph import Glyph
from src.items.board import Board
from src.items.book_keeping import BookKeeping
from src.items.item import Item, SudokuException
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.rule import Rule


class CellException(SudokuException):
    """Exception for Cell-specific errors."""


class Cell(Item):
    """Represents a cell in a Sudoku board."""

    cache: ClassVar[dict[tuple[int, int], 'Cell']] = {}

    @classmethod
    def clear(cls):
        """Clear the cell cache."""
        cls.cache.clear()

    def __init__(self, board: Board, row: int, column: int):
        """Initialize a Cell with a board, row, and column.

        Args:
            board (Board): The Sudoku board the cell belongs to.
            row (int): The row position of the cell.
            column (int): The column position of the cell.
        """
        super().__init__(board)
        self.row = row
        self.column = column
        self.book = BookKeeping(self.board.maximum_digit)

    def __repr__(self) -> str:
        """Return a detailed string representation of the cell.

        Returns:
            str: A string representation including board, row, and column.
        """
        return f"{self.__class__.__name__}({self.board!r}, {self.row!r}, {self.column!r})"

    def __hash__(self):
        """Compute a unique hash for the cell based on row and column.

        Returns:
            int: The hash value of the cell.
        """
        return self.row * self.board.maximum_digit + self.column

    def __str__(self) -> str:
        """Return a string identifier for the cell.

        Returns:
            str: A string in the format 'Cell(row, column)'.
        """
        return f"Cell({self.row}, {self.column})"

    def marked_book(self) -> BookKeeping | None:
        """Return the bookkeeping instance for the cell.

        Returns:
            BookKeeping | None: The BookKeeping instance for tracking digit possibilities.
        """
        return self.book

    @staticmethod
    def letter() -> str:
        """Return the letter used for cell representation.

        Returns:
            str: A placeholder letter for the cell.
        """
        return '.'

    @property
    def rules(self) -> list[Rule]:
        """Return the list of rules associated with the cell.

        Returns:
            list[Rule]: A list of Rule instances.
        """
        return []

    @staticmethod
    def cells() -> list['Cell']:
        """Return all cached cells.

        Returns:
            list[Cell]: A list of all cached Cell instances.
        """
        return list(Cell.cache.values())

    def glyphs(self) -> list[Glyph]:
        """Return the glyph representation of the cell.

        Returns:
            list[Glyph]: A list containing the CellGlyph for the cell.
        """
        return [CellGlyph('Cell', Coord(self.row, self.column))]

    @classmethod
    def make(cls, board: Board, row: int, column: int) -> 'Cell':
        """Create a new cell or retrieve it from the cache.

        Args:
            board (Board): The Sudoku board the cell belongs to.
            row (int): The row position of the cell.
            column (int): The column position of the cell.

        Returns:
            Cell: The created or cached cell.
        """
        key = (row, column)
        if key in Cell.cache:
            return Cell.cache[key]
        cell = Cell(board, row, column)
        Cell.cache[key] = cell
        return cell

    @classmethod
    def make_board(cls, board: Board):
        """Generate all cells for a given board and cache them.

        Args:
            board (Board): The board for which cells are created.
        """
        for row, column in product(board.row_range, board.column_range):
            Cell.make(board, row, column)

    @classmethod
    def extract(cls, board: Board, yaml: dict) -> Coord:
        """Extract coordinates from a YAML representation.

        Args:
            board (Board): The board the coordinates belong to.
            yaml (dict): A dictionary containing coordinate data.

        Returns:
            Coord: The extracted coordinate.
        """
        return Coord.create_from_int(yaml[cls.__name__])

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create a cell from YAML data.

        Args:
            board (Board): The board the cell belongs to.
            yaml (dict): A dictionary with cell data.

        Returns:
            Item: The created cell instance.
        """
        coord: Coord = Cell.extract(board, yaml)
        return cls(board, int(coord.row), int(coord.column))

    @property
    def valid(self) -> bool:
        """Check if the cell is valid on the board.

        Returns:
            bool: True if the cell is valid, False otherwise.
        """
        return self.board.is_valid(self.row, self.column)

    @property
    def row_column(self) -> tuple[int, int]:
        """Return the row and column of the cell.

        Returns:
            tuple[int, int]: The (row, column) tuple of the cell.
        """
        return self.row, self.column

    def __eq__(self, other: object) -> bool:
        """Compare the cell with another cell for equality.

        Args:
            other (object): The object to compare.

        Returns:
            bool: True if both cells have the same row and column, False otherwise.
        """
        if isinstance(other, Cell):
            return self.row == other.row and self.column == other.column
        return False

    def __lt__(self, other: object) -> bool:
        """Compare the cell with another cell based on row and column.

        Args:
            other (object): The object to compare.

        Returns:
            bool: True if this cell is less than the other cell.
        """
        if isinstance(other, Cell):
            if self.row < other.row:
                return True
            if self.row == other.row:
                return self.column < other.column
            return False
        raise CellException(f"Cannot compare {object.__class__.__name__} with {self.__class__.__name__}")

    @property
    def coord(self) -> Coord:
        """Return the coordinate of the cell.

        Returns:
            Coord: The coordinate of the cell.
        """
        return Coord(self.row, self.column)

    @property
    def row_column_string(self) -> str:
        """Return a string representation of the cell's row and column.

        Returns:
            str: A string combining row and column numbers.
        """
        return f"{self.row}{self.column}"

    def parity(self, solver) -> lpSum:
        """Compute the parity constraint for the cell.

        Args:
            solver (PulpSolver): The solver instance.

        Returns:
            lpSum: A linear program sum for even digits in the cell.
        """
        return lpSum(
            [
                solver.choices[digit][self.row][self.column]
                for digit in self.board.digit_range
                if digit % 2 == 0
            ]
        )

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add a unique digit constraint for the cell.

        Args:
            solver (PulpSolver): The solver instance.
        """
        solver.model += lpSum(
            [
                solver.choices[digit][self.row][self.column]
                for digit in self.board.digit_range
            ]
        ) == 1, f'Unique_digit_{self.row}_{self.column}'

    # pylint: disable=loop-invariant-statement
    def add_bookkeeping_constraint(self, solver: PulpSolver) -> None:
        """Add constraints based on bookkeeping for the cell.

        Args:
            solver (PulpSolver): The solver instance.
        """
        print(f"Bookkeeping {self.row} {self.column}")
        for digit in self.board.digit_range:
            if not self.book.is_possible(digit):
                name = f"Impossible_cell_bookkeeping_{digit}_{self.row}_{self.column}"
                solver.model += solver.choices[digit][self.row][self.column] == 0, name

    def to_dict(self) -> dict:
        """Convert the cell to a dictionary format.

        Returns:
            dict: A dictionary representation of the cell.
        """
        return {self.__class__.__name__: int(self.row_column_string)}

    def css(self) -> dict:
        """Return CSS styling for the cell.

        Returns:
            dict: A dictionary containing CSS styles for the cell.
        """
        return {
            '.Cell': {
                'stroke': 'black',
                'stroke-width': 1,
                'fill-opacity': 0
            }
        }
