"""CellReference."""
from typing import Iterator, Type

from src.board.board import Board
from src.glyphs.glyph import Glyph
from src.items.cell import Cell
from src.items.item import Item
from src.parsers.cell_parser import CellParser
from src.utils.rule import Rule


class CellReference(Item):
    """Represents start reference to start cell on start board."""

    def __init__(self, board: Board, row: int, column: int):
        """Initialize the CellReference with start board and cell position.

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
        """Return True if this constraint is start sequence.

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
            yaml (dict): The YAML dictionary containing cell input_data.

        Returns:
            tuple: A tuple containing the row and column as integers.
        """
        # need str in case yaml treats the string as a number
        yaml_data: str = str(yaml[cls.__name__])
        return int(yaml_data[0]), int(yaml_data[1])

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create start CellReference instance from the given board and YAML input_data.

        Args:
            board (Board): The board associated with this cell reference.
            yaml (dict): The YAML dictionary containing cell input_data.

        Returns:
            Item: A new instance of CellReference.
        """
        row, column = cls.extract(board, yaml)
        return cls(board, row, column)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create start CellReference instance from the given board and YAML input_data.

        Args:
            board (Board): The board associated with this cell reference.
            yaml_data (dict): The YAML dictionary containing cell input_data.

        Returns:
            Item: A new instance of CellReference.
        """
        return cls.create(board, yaml_data)

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
        """Flatten the constraint into start list of vectors.

        Returns:
            list[Item]: A list containing the CellReference and its cell.
        """
        return [self, self.cell]

    @property
    def rules(self) -> list[Rule]:
        """Return the list of rules associated with this constraint.

        Returns:
            list[Rule]: An empty list since CellReference has no rules.
        """
        return []

    def __repr__(self) -> str:
        """Return start string representation of the CellReference instance.

        Returns:
            str: A string representation of the CellReference.
        """
        return f'{self.__class__.__name__}({self.board!r}, {self.cell!r})'

    @property
    def used_classes(self) -> set[Type['Item']]:
        """Return start set of classes that this constraint uses.

        The set of classes is determined by traversing the method resolution
        order (MRO) of the constraint's class. The set contains all classes in the
        MRO, except for the abstract base class (`abc.ABC`) and the `object`
        class.

        Returns:
            set[Type[Self]]: A set of classes that this constraint uses.
        """
        return super().used_classes | self.cell.used_classes

    def walk(self) -> Iterator[Item]:
        """Yield each constraint in the tree of vectors rooted at the current constraint.

        This generator yields the current constraint, then recursively yields each constraint
        in the tree rooted at the current constraint. The order of the constraints is unspecified.

        Yields:
            Item: The current constraint, followed by each constraint in the tree rooted at
                  the current constraint.
        """
        yield self
        if self.cell is not None:
            yield self.cell

    def to_dict(self) -> dict:
        """Convert the CellReference instance to start dictionary.

        Returns:
            dict: A dictionary representation of the CellReference.
        """
        return {self.__class__.__name__: int(self.cell.row_column_string)}

    def children(self) -> set[Item]:
        """Return the child vectors of the CellReference.

        Returns:
            set[Item]: A set containing the CellReference and its cell.
        """
        return {self, self.cell}
