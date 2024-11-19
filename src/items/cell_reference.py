"""CellReference."""
from typing import Type, Iterator

from src.glyphs.glyph import Glyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.parsers.cell_parser import CellParser
from src.utils.rule import Rule


class CellReference(Item):
    """Represents a reference to a cell on a board."""

    def __init__(self, board: Board, row: int, column: int):
        """Initialize the CellReference with a board and cell position.

        Args:
            board (Board): The board associated with this cell reference.
            row (int): The row number (1-based).
            column (int): The column number (1-based).
        """
        super().__init__(board)
        self.cell = Cell.make(board, row, column)
        self.row = row
        self.column = column

    @classmethod
    def is_sequence(cls) -> bool:
        """Return True if this item is a sequence.

        Returns:
            bool: Always True for CellReference.
        """
        return True

    @classmethod
    def parser(cls) -> CellParser:
        """Return the parser for CellReference.

        Returns:
            CellParser: An instance of CellParser.
        """
        return CellParser()

    @classmethod
    def extract(cls, board: Board, yaml: dict) -> tuple:
        """Extract the row and column from the given YAML dictionary.

        Args:
            board (Board): The board associated with this cell reference.
            yaml (dict): The YAML dictionary containing cell data.

        Returns:
            tuple: A tuple containing the row and column as integers.
        """
        data = yaml[cls.__name__]
        data = str(data)
        return int(data[0]), int(data[1])

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create a CellReference instance from the given board and YAML data.

        Args:
            board (Board): The board associated with this cell reference.
            yaml (dict): The YAML dictionary containing cell data.

        Returns:
            Item: A new instance of CellReference.
        """
        row, column = cls.extract(board, yaml)
        return cls(board, row, column)

    def svg(self) -> Glyph | None:
        """Return an SVG representation of the cell.

        Returns:
            Glyph | None: Always returns None for CellReference.
        """
        return None

    def letter(self) -> str:
        """Return the letter representation of the cell.

        Returns:
            str: A string representing the cell, default is '.'.
        """
        return '.'

    def flatten(self) -> list[Item]:
        """Flatten the item into a list of items.

        Returns:
            list[Item]: A list containing the CellReference and its cell.
        """
        return [self, self.cell]

    @property
    def rules(self) -> list[Rule]:
        """Return the list of rules associated with this item.

        Returns:
            list[Rule]: An empty list since CellReference has no rules.
        """
        return []

    def __repr__(self) -> str:
        """Return a string representation of the CellReference instance.

        Returns:
            str: A string representation of the CellReference.
        """
        return f"{self.__class__.__name__}({self.board!r}, {self.cell!r})"

    @property
    def used_classes(self) -> set[Type['Item']]:
        """Return a set of classes that this item uses.

        The set of classes is determined by traversing the method resolution
        order (MRO) of the item's class. The set contains all classes in the
        MRO, except for the abstract base class (`abc.ABC`) and the `object`
        class.

        Returns:
            set[Type[Self]]: A set of classes that this item uses.
        """
        return super().used_classes | self.cell.used_classes

    def walk(self) -> Iterator[Item]:
        """Yield each item in the tree of items rooted at the current item.

        The generator yields the current item, then recursively yields each item
        in the tree rooted at the current item. The order of the items is
        unspecified.

        Yields:
            Item: The current item, followed by each item in the tree rooted at
                the current item.
        """
        yield self
        yield self.cell

    def to_dict(self) -> dict:
        """Convert the CellReference instance to a dictionary.

        Returns:
            dict: A dictionary representation of the CellReference.
        """
        return {self.__class__.__name__: int(self.cell.row_column_string)}

    def children(self) -> set[Item]:
        """Return the child items of the CellReference.

        Returns:
            set[Item]: A set containing the CellReference and its cell.
        """
        return {self, self.cell}
