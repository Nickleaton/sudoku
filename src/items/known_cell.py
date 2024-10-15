import re
from typing import List, Tuple, Dict, Callable

from src.glyphs.glyph import Glyph
from src.glyphs.known_glyph import KnownGlyph
from src.items.board import Board
from src.items.box import Box
from src.items.cell_reference import CellReference
from src.items.column import Column
from src.items.item import Item
from src.items.row import Row
from src.utils.coord import Coord


class KnownCell(CellReference):
    """
    Item for a given cell in the board.
    """

    def __init__(self, board: Board, row: int, column: int, digit: int, prefix=None):
        """
        Construct a KnownCell object.

        Args:
        - board (Board): The board this item is attached to.
        - row (int): The row of the cell in the board.
        - column (int): The column of the cell in the board.
        - digit (int): The digit that is placed in this cell.
        - prefix (str): The prefix to be used in the item's name. Defaults to "Known".
        """
        super().__init__(board, row, column)
        self.digit = int(digit)
        self.prefix = "Known" if prefix is None else prefix

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Tuple:
        """
        Extract the row, column, and digit from the given yaml string.

        Example:  12=3

        Would set row=1, column=2, to the value of 3



        Args:
        - board (Board): The board this item is attached to.
        - yaml (Dict): The given yaml string.

        Returns:
        - Tuple[int, int, int]: The row, column, and digit of the item.
        """
        regex = re.compile(f"([{board.digit_values}])([{board.digit_values}])=([{board.digit_values}]+)")
        match = regex.match(yaml[cls.__name__])
        assert match is not None
        row_str, column_string, digit_str = match.groups()
        return int(row_str), int(column_string), int(digit_str)

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        """
        Create an instance of an item from a YAML dictionary.

        Args:
        - board (Board): The board associated with this item.
        - yaml (Dict): A YAML dictionary containing the key-value pair to
            create an item.

        Returns:
        - Item: An instance of the item class associated with the YAML
            dictionary.
        """
        row, column, digit = KnownCell.extract(board, yaml)
        return cls(board, row, column, digit)

    def letter(self) -> str:
        return str(self.digit)

    def glyphs(self) -> List[Glyph]:
        """
        Return a list of SVG glyphs for this item.

        The glyphs are determined by calling the `glyph` method on each item in
        the item tree. The `selector` function is used to determine which items
        to include in the list of glyphs.

        Args:
        - selector (Callable[[Item], bool]): A function that takes an item and
            returns a boolean indicating whether to include it in the list
            of glyphs.

        Returns:
        - List[Glyph]: A list of glyphs.
        """
        return [KnownGlyph('Known', Coord(self.row, self.column), self.digit)]

    def __repr__(self) -> str:
        """
        Return a string representation of this item.

        The string representation is of the form `<class_name>(<board>, <cell>, <digit>)`, where
        `<class_name>` is the name of the class of this item, `<board>` is a string representation
        of the board associated with the item, `<cell>` is a string representation of the cell
        associated with the item, and `<digit>` is the digit associated with the item.

        Returns:
        - str: A string representation of this item.
        """
        return f"{self.__class__.__name__}({self.board!r}, {self.cell!r}, {self.digit!r})"

    def to_dict(self) -> Dict:
        """
        Convert the item to a dictionary for serialisation.

        The dictionary has a single key-value pair where the key is the
        item's class name and the value is a string of the form
        `<row><column>=<digit>`, where `<row>` is the row of the cell,
        `<column>` is the column of the cell, and `<digit>` is the digit
        associated with the cell.

        Returns:
        - Dict: A dictionary containing the item's class name and a string
            representation of the item's data.
        """
        return {self.__class__.__name__: f"{self.row}{self.column}={self.digit}"}

    def css(self) -> Dict:
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
        Perform bookkeeping based on the contents of the cell.

        This means that the cell itself is set to be only the digit given,
        and all other cells in the same row, column, or box are set to
        not be able to contain the digit.

        :return: None
        """
        self.cell.book.set_possible([self.digit])
        raw_regions = [region for region in self.cell.top.regions() if region.__class__ in [Box, Row, Column]]
        filtered_regions = [region for region in raw_regions if self.cell in region]
        for region in filtered_regions:
            for cell in region.cells:
                if cell == self.cell:
                    continue
                cell.book.set_impossible([self.digit])
