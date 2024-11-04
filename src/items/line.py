from typing import List, Sequence, Dict

from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.region import Region
from src.parsers.cell_list_parser import CellListParser
from src.utils.rule import Rule


class Line(Region):
    """Represents a line consisting of multiple cells on a board."""

    def __init__(self, board: Board, cells: Sequence[Cell]):
        """
        Initialize a Line instance.

        Args:
            board (Board): The board associated with this line.
            cells (Sequence[Cell]): A sequence of cells that make up this line.
        """
        super().__init__(board)
        self.add_items(cells)

    @classmethod
    def parser(cls) -> CellListParser:
        """Return a CellListParser instance for parsing cell lists."""
        return CellListParser()

    @classmethod
    def is_sequence(cls) -> bool:
        """Return True if this item is a sequence."""
        return True

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> List[Cell]:
        """
        Extract a list of Cell instances from the provided YAML dictionary.

        Args:
            board (Board): The board associated with the cells.
            yaml (Dict): A dictionary containing the YAML data.

        Returns:
            List[Cell]: A list of Cell instances extracted from the YAML data.
        """
        return [Cell.make(board, int(part.strip()[0]), int(part.strip()[1])) for part in yaml[cls.__name__].split(',')]

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        """
        Create a Line instance from a YAML dictionary.

        Args:
            board (Board): The board associated with the line.
            yaml (Dict): A dictionary containing the YAML data.

        Returns:
            Item: A new instance of Line created from the YAML data.
        """
        cells = cls.extract(board, yaml)
        return cls(board, cells)

    def __repr__(self) -> str:
        """
        Return a string representation of this line.

        Returns:
            str: A string representation of the Line instance, including the board and cells.
        """
        cell_str = ", ".join(repr(cell) for cell in self.cells)
        return f"{self.__class__.__name__}({self.board!r}, [{cell_str}])"

    @property
    def rules(self) -> List[Rule]:
        """Return an empty list of rules associated with this line."""
        return []

    @property
    def tags(self) -> set[str]:
        """
        Return a set of tags associated with this line.

        Returns:
            set[str]: A set containing the tags associated with this line.
        """
        return super().tags.union({'Line'})

    def to_dict(self) -> Dict:
        """
        Convert the line to a dictionary representation.

        Returns:
            Dict: A dictionary representation of the line, including the cells.
        """
        return {self.__class__.__name__: ", ".join([cell.row_column_string for cell in self.cells])}
