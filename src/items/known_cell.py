import re
from typing import List, Tuple, Dict

from src.glyphs.glyph import Glyph
from src.glyphs.known_glyph import KnownGlyph
from src.items.board import Board
from src.items.cell_reference import CellReference
from src.items.item import Item
from src.items.standard_region import StandardRegion
from src.utils.coord import Coord


class KnownCell(CellReference):
    """
    Represents a given cell in the board with a specified digit.

    Attributes:
        digit (int): The digit assigned to this cell.
        prefix (str): The prefix used for the cell, defaults to "Known".
    """

    def __init__(self, board: Board, row: int, column: int, digit: int, prefix=None):
        """
        Initializes a KnownCell instance.

        Args:
            board (Board): The board associated with this cell.
            row (int): The row index of the cell.
            column (int): The column index of the cell.
            digit (int): The digit assigned to the cell.
            prefix (str, optional): The prefix used for the cell. Defaults to "Known".
        """
        super().__init__(board, row, column)
        self.digit = int(digit)
        self.prefix = "Known" if prefix is None else prefix

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Tuple[int, int, int]:
        """
        Extracts the row, column, and digit from the given YAML string.

        Args:
            board (Board): The board this item is attached to.
            yaml (Dict): The given YAML string.

        Returns:
            Tuple[int, int, int]: A tuple containing row, column, and digit values.

        Raises:
            AssertionError: If the input format does not match the expected regex pattern.
        """
        regex = re.compile(f"([{board.digit_values}])([{board.digit_values}])=([{board.digit_values}]+)")
        match = regex.match(yaml[cls.__name__])
        assert match is not None
        row_str, column_string, digit_str = match.groups()
        return int(row_str), int(column_string), int(digit_str)

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        """
        Creates an instance of KnownCell from a YAML dictionary.

        Args:
            board (Board): The board associated with this item.
            yaml (Dict): A YAML dictionary with the required parameters.

        Returns:
            Item: An instance of KnownCell.
        """
        row, column, digit = KnownCell.extract(board, yaml)
        return cls(board, row, column, digit)

    def letter(self) -> str:
        """
        Gets the digit as a string.

        Returns:
            str: The digit of the cell.
        """
        return str(self.digit)

    def glyphs(self) -> List[Glyph]:
        """
        Returns a list of SVG glyphs for this item.

        Returns:
            List[Glyph]: A list containing a KnownGlyph for this cell.
        """
        return [KnownGlyph('Known', Coord(self.row, self.column), self.digit)]

    def __repr__(self) -> str:
        """
        Returns a string representation of this item.

        Returns:
            str: A string representation of this KnownCell instance.
        """
        return f"{self.__class__.__name__}({self.board!r}, {self.cell!r}, {self.digit!r})"

    def to_dict(self) -> Dict:
        """
        Converts the item to a dictionary for serialization.

        Returns:
            Dict: A dictionary with the class name as the key and cell information as the value.
        """
        return {self.__class__.__name__: f"{self.row}{self.column}={self.digit}"}

    def css(self) -> Dict:
        """
        Returns CSS properties for styling Known and Unknown cells.

        Returns:
            Dict: A dictionary of CSS properties.
        """
        return {
            ".Known": {
                'font-size': '70px',
                'fill': 'black',
                'font-weight': '500',
                'text-shadow': '-2px -2px 0 white, 2px -2px 0 white, -2px 2px 0 white, 2px 2px 0 white'
            },
            ".Unknown": {
                'font-size': '70px',
                'fill': 'blue',
                'font-weight': '500',
                'text-shadow': '-2px -2px 0 white, 2px -2px 0 white, -2px 2px 0 white, 2px 2px 0 white'
            },
            ".KnownForeground": {
                'font-size': '70px',
                'stroke': 'black',
                'fill': 'black'
            },
            ".KnownBackground": {
                'font-size': '70px',
                'stroke': 'white',
                'stroke-width': 8,
                'fill': 'white',
                'font-weight': 'bolder'
            },
            ".UnknownForeground": {
                'font-size': '70px',
                'stroke': 'blue',
                'fill': 'blue'
            },
            ".UnknownBackground": {
                'font-size': '70px',
                'stroke': 'white',
                'stroke-width': 8,
                'fill': 'white',
                'font-weight': 'bolder'
            }
        }

    def bookkeeping(self) -> None:
        """
        Performs bookkeeping on this cell.

        Sets the cell to only the assigned digit and restricts the same digit
        in the row, column, and box of this cell.

        Returns:
            None
        """
        self.cell.book.set_possible([self.digit])
        standard_regions: List[StandardRegion] = [
            region for region in self.cell.top.regions() if isinstance(region, StandardRegion)
        ]
        for region in standard_regions:
            if self.cell in region:
                for cell in region.cells:
                    if cell == self.cell:
                        continue
                    cell.book.set_impossible([self.digit])
