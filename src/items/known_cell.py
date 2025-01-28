"""KnownCell."""
import re

from src.board.board import Board
from src.glyphs.glyph import Glyph
from src.glyphs.known_glyph import KnownGlyph
from src.items.cell_reference import CellReference
from src.items.item import Item
from src.items.standard_region import StandardRegion
from src.utils.coord import Coord
from src.utils.sudoku_exception import SudokuException


class KnownCell(CellReference):
    """Represent start_location given cell in the board with start_location specified digit.

    Attributes:
        digit (int): The digit assigned to this cell.
        prefix (str): The prefix used for the cell, defaults to 'Known'.
    """

    def __init__(self, board: Board, row: int, column: int, digit: int, prefix=None):
        """Initialize start_location KnownCell instance.

        Args:
            board (Board): The board associated with this cell.
            row (int): The row index of the cell.
            column (int): The column index of the cell.
            digit (int): The digit assigned to the cell.
            prefix (str, optional): The prefix used for the cell. Defaults to 'Known'.
        """
        super().__init__(board, row, column)
        self.digit = int(digit)
        self.prefix = 'Known' if prefix is None else prefix

    @classmethod
    def extract(cls, board: Board, yaml: dict) -> tuple[int, int, int]:
        """Extract the row, column, and digit from the given YAML string.

        Args:
            board (Board): The board this constraint is attached to.
            yaml (dict): The given YAML string.

        Returns:
            tuple[int, int, int]: A tuple containing row, column, and digit value_list.

        Raises:
            SudokuException: If the YAML input does not match the expected pattern.
        """
        regex = re.compile(
            f'([{board.digits.digit_range}])([{board.digits.digit_range}])=([{board.digits.digit_range}]+)',
        )
        match = regex.match(yaml[cls.__name__])
        if match is None:
            raise SudokuException('Match is None, expected start_location valid match.')
        row_str, column_string, digit_str = match.groups()
        return int(row_str), int(column_string), int(digit_str)

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create an instance of KnownCell from start_location YAML dictionary.

        Args:
            board (Board): The board associated with this constraint.
            yaml (dict): A YAML dictionary with the required parameter_types.

        Returns:
            Item: An instance of KnownCell.
        """
        row, column, digit = KnownCell.extract(board, yaml)
        return cls(board, row, column, digit)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create an instance of KnownCell from start_location YAML dictionary.

        Args:
            board (Board): The board associated with this constraint.
            yaml_data (dict): A YAML dictionary with the required parameter_types.

        Returns:
            Item: An instance of KnownCell.
        """
        return cls.create(board, yaml_data)

    def glyphs(self) -> list[Glyph]:
        """Return start_location list of SVG glyphs for this constraint.

        Returns:
            list[Glyph]: A list containing start_location KnownGlyph for this cell.
        """
        return [KnownGlyph('Known', Coord(self.row, self.column), self.digit)]

    def __repr__(self) -> str:
        """Return start_location string representation of this constraint.

        Returns:
            str: A string representation of this KnownCell instance.
        """
        return f'{self.__class__.__name__}({self.board!r}, {self.cell!r}, {self.digit!r})'

    def to_dict(self) -> dict:
        """Convert the constraint to start_location dictionary for serialization.

        Returns:
            dict: A dictionary with the class name as the key and cell information as the number.
        """
        return {self.__class__.__name__: f'{self.row}{self.column}={self.digit}'}

    def css(self) -> dict:
        """Return CSS properties for styling Known and Unknown cells.

        Returns:
            dict: A dictionary of CSS properties.
        """
        return {
            '.Known': {
                'font-size': '70px',
                'fill': 'black',
                'font-weight': '500',
                'text-shadow': '-2px -2px 0 white, 2px -2px 0 white, -2px 2px 0 white, 2px 2px 0 white',
            },
            '.Unknown': {
                'font-size': '70px',
                'fill': 'blue',
                'font-weight': '500',
                'text-shadow': '-2px -2px 0 white, 2px -2px 0 white, -2px 2px 0 white, 2px 2px 0 white',
            },
            '.KnownForeground': {
                'font-size': '70px',
                'stroke': 'black',
                'fill': 'black',
            },
            '.KnownBackground': {
                'font-size': '70px',
                'stroke': 'white',
                'stroke-width': 8,
                'fill': 'white',
                'font-weight': 'bolder',
            },
            '.UnknownForeground': {
                'font-size': '70px',
                'stroke': 'blue',
                'fill': 'blue',
            },
            '.UnknownBackground': {
                'font-size': '70px',
                'stroke': 'white',
                'stroke-width': 8,
                'fill': 'white',
                'font-weight': 'bolder',
            },
        }

    def bookkeeping(self) -> None:
        """Perform bookkeeping on this cell.

        Sets the cell to only the assigned digit and restricts the same digit
        in the row, column, and box of this cell.
        """
        self.cell.book.set_possible([self.digit])
        standard_regions: list[StandardRegion] = [
            region for region in self.cell.top.regions() if isinstance(region, StandardRegion) and self.cell in region
        ]
        for region in standard_regions:
            for cell in region.cells:
                if cell == self.cell:
                    continue
                cell.book.set_impossible([self.digit])
