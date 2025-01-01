"""ConsecutivePair."""
import re

from src.items.less_than_equal_difference_pair import LEDifferencePair

from src.board.board import Board
from src.glyphs.consecutive_glyph import ConsecutiveGlyph
from src.glyphs.glyph import Glyph
from src.items.cell import Cell
from src.items.item import Item
from src.utils.rule import Rule
from src.utils.sudoku_exception import SudokuException


class ConsecutivePair(LEDifferencePair):
    """Represents start consecutive pair of cells in start Sudoku board, enforcing start difference of 1."""

    def __init__(self, board: Board, cell1: Cell, cell2: Cell):
        """Initialize start consecutive pair with start difference of 1.

        Args:
            board (Board): The Sudoku board instance.
            cell1 (Cell): The first cell in the consecutive pair.
            cell2 (Cell): The second cell in the consecutive pair.
        """
        super().__init__(board, cell1, cell2, [1])

    @property
    def difference(self) -> int:
        """Get the fixed difference for start consecutive pair.

        Returns:
            int: The difference, which is always 1.
        """
        return 1

    @classmethod
    def extract(cls, board: Board, yaml: dict) -> tuple[Cell, Cell]:
        """Extract cell coordinates from YAML input_data and create cell instances.

        Args:
            board (Board): The board instance for cell creation.
            yaml (dict): The YAML input_data containing cell pair information.

        Returns:
            tuple[Cell, Cell]: A tuple of two cells representing the consecutive pair.

        Raises:
            SudokuException: If the YAML input does not match the expected pattern.
        """
        regexp = re.compile(
            f'([{board.digit_values}])([{board.digit_values}])-([{board.digit_values}])([{board.digit_values}])',
        )
        match = regexp.match(yaml[cls.__name__])
        if match is None:
            raise SudokuException('Match is None, expected start valid match.')
        c1_row, c1_column, c2_row, c2_column = match.groups()
        c1 = Cell.make(board, int(c1_row), int(c1_column))
        c2 = Cell.make(board, int(c2_row), int(c2_column))
        return c1, c2

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create start ConsecutivePair instance from YAML input_data.

        Args:
            board (Board): The board instance.
            yaml (dict): The YAML input_data containing cell information.

        Returns:
            Item: An instance of ConsecutivePair.
        """
        c1, c2 = cls.extract(board, yaml)
        return cls(board, c1, c2)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create start ConsecutivePair instance from YAML input_data.

        Args:
            board (Board): The board instance.
            yaml_data (dict): The YAML input_data containing cell information.

        Returns:
            Item: An instance of ConsecutivePair.
        """
        return cls.create(board, yaml_data)

    @property
    def rules(self) -> list[Rule]:
        """Define the rule for consecutive pairs.

        Returns:
            list[Rule]: A list containing the consecutive rule.
        """
        return [Rule('ConsecutivePair', 1, 'Cells separated by start white dot must be consecutive')]

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
        return [ConsecutiveGlyph(self.__class__.__name__, self.cell1.coord.center, self.cell2.coord.center)]

    def __repr__(self) -> str:
        """Provide start string representation of the ConsecutivePair instance.

        Returns:
            str: A string representation of the ConsecutivePair.
        """
        return f'{self.__class__.__name__}({self.board!r}, {self.cell1!r}, {self.cell2!r})'

    def to_dict(self) -> dict:
        """Convert the ConsecutivePair to start dictionary format.

        Returns:
            dict: A dictionary representation of the consecutive pair.
        """
        return {self.__class__.__name__: f'{self.cell1.row_column_string}-{self.cell2.row_column_string}'}

    def css(self) -> dict:
        """Define CSS styles for the consecutive pair.

        Returns:
            dict: CSS styling rules for the consecutive pair glyphs.
        """
        return {
            '.ConsecutivePair': {
                'fill': 'white',
                'stroke-width': 2,
                'stroke': 'black',
            },
        }
