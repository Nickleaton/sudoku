"""ConsecutivePair."""
import re

from src.board.board import Board
from src.glyphs.consecutive_glyph import ConsecutiveGlyph
from src.glyphs.glyph import Glyph
from src.items.cell import Cell
from src.items.item import Item
from src.items.less_than_equal_difference_pair import LessThanEqualDifferencePair
from src.utils.rule import Rule
from src.utils.sudoku_exception import SudokuException


class ConsecutivePair(LessThanEqualDifferencePair):
    """Represents a consecutive pair of cells in a Sudoku board, enforcing a difference of 1."""

    def __init__(self, board: Board, cell_1: Cell, cell_2: Cell):
        """Initialize a consecutive pair with a difference of 1.

        Args:
            board (Board): The Sudoku board instance.
            cell_1 (Cell): The first cell in the consecutive pair.
            cell_2 (Cell): The second cell in the consecutive pair.
        """
        super().__init__(board, cell_1, cell_2, [1])

    @property
    def difference(self) -> int:
        """Get the fixed difference for a consecutive pair.

        Returns:
            int: The difference, which is always 1.
        """
        return 1

    @classmethod
    def extract(cls, board: Board, yaml: dict) -> tuple[Cell, Cell]:
        """Extract cell coordinates from YAML data and create cell instances.

        Args:
            board (Board): The board instance for cell creation.
            yaml (dict): The YAML data containing cell pair information.

        Returns:
            tuple[Cell, Cell]: A tuple of two cells representing the consecutive pair.
        """
        regexp = re.compile(
            f"([{board.digit_values}])([{board.digit_values}])-([{board.digit_values}])([{board.digit_values}])"
        )
        match = regexp.match(yaml[cls.__name__])
        if match is None:
            raise SudokuException("Match is None, expected a valid match.")
        c1_row, c1_column, c2_row, c2_column = match.groups()
        c1 = Cell.make(board, int(c1_row), int(c1_column))
        c2 = Cell.make(board, int(c2_row), int(c2_column))
        return c1, c2

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create a ConsecutivePair instance from YAML data.

        Args:
            board (Board): The board instance.
            yaml (dict): The YAML data containing cell information.

        Returns:
            Item: An instance of ConsecutivePair.
        """
        c1, c2 = cls.extract(board, yaml)
        return cls(board, c1, c2)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        return cls.create(board, yaml_data)

    @property
    def rules(self) -> list[Rule]:
        """Define the rule for consecutive pairs.

        Returns:
            list[Rule]: A list containing the consecutive rule.
        """
        return [Rule("ConsecutivePair", 1, "Cells separated by a white dot must be consecutive")]

    @property
    def tags(self) -> set[str]:
        """Retrieve tags for the consecutive pair.

        Returns:
            set[str]: A set of tags, including 'Consecutive'.
        """
        return super().tags.union({'Consecutive'})

    def glyphs(self) -> list[Glyph]:
        """Define the glyphs associated with the consecutive pair.

        Returns:
            list[Glyph]: A list containing the glyph for the consecutive pair.
        """
        return [ConsecutiveGlyph(self.__class__.__name__, self.cell_1.coord.center, self.cell_2.coord.center)]

    def __repr__(self) -> str:
        """Provide a string representation of the ConsecutivePair instance.

        Returns:
            str: A string representation of the ConsecutivePair.
        """
        return f"{self.__class__.__name__}({self.board!r}, {self.cell_1!r}, {self.cell_2!r})"

    def to_dict(self) -> dict:
        """Convert the ConsecutivePair to a dictionary format.

        Returns:
            dict: A dictionary representation of the consecutive pair.
        """
        return {self.__class__.__name__: f"{self.cell_1.row_column_string}-{self.cell_2.row_column_string}"}

    def css(self) -> dict:
        """Define CSS styles for the consecutive pair.

        Returns:
            dict: CSS styling rules for the consecutive pair glyphs.
        """
        return {
            '.ConsecutivePair': {
                'fill': 'white',
                'stroke-width': 2,
                'stroke': 'black'
            }
        }
