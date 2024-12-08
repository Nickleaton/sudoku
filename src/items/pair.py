"""Pair."""

from src.board.board import Board
from src.glyphs.edge_text_glyph import EdgeTextGlyph
from src.glyphs.glyph import Glyph
from src.items.cell import Cell
from src.items.item import Item
from src.items.region import Region
from src.parsers.cell_pairs_parser import CellPairsParser
from src.utils.rule import Rule


class Pair(Region):
    """Represents a pair of cells that are linked together for a constraint.

    This class defines a pair of cells and provides the functionality for associating them in the puzzle.
    """

    def __init__(self, board: Board, cell_1: Cell, cell_2: Cell):
        """Initialize a pair of cells on the board.

        Args:
            board (Board): The board on which the pair is defined.
            cell_1 (Cell): The first cell in the pair.
            cell_2 (Cell): The second cell in the pair.
        """
        super().__init__(board)
        self.cell_1 = cell_1
        self.cell_2 = cell_2
        self.add(cell_1)
        self.add(cell_2)

    @classmethod
    def is_sequence(cls) -> bool:
        """Indicate whether this item is a sequence.

        Returns:
            bool: True, since the pair is treated as a sequence.
        """
        return True

    @classmethod
    def parser(cls) -> CellPairsParser:
        """Return the parser for this item.

        Returns:
            CellPairsParser: The parser for extracting pairs of cells from the YAML configuration.
        """
        return CellPairsParser()

    @classmethod
    def extract(cls, board: Board, yaml: dict) -> tuple:
        """Extract the pair of cells from the YAML configuration.

        Args:
            board (Board): The board on which the pair is defined.
            yaml (dict): The YAML configuration that defines the pair.

        Returns:
            tuple: A tuple containing the two cells in the pair.
        """
        c1_str, c2_str = yaml[cls.__name__].split('-')
        c1 = Cell.make(board, int(c1_str[0]), int(c1_str[1]))
        c2 = Cell.make(board, int(c2_str[0]), int(c2_str[1]))
        return c1, c2

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create a new Pair instance from the given board and YAML configuration.

        Args:
            board (Board): The board on which the pair is defined.
            yaml (dict): The YAML configuration that defines the pair.

        Returns:
            Item: A new Pair instance.
        """
        c1, c2 = cls.extract(board, yaml)
        return cls(board, c1, c2)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        return cls.create(board, yaml_data)

    @property
    def rules(self) -> list[Rule]:
        """Return a list of rules associated with the pair.

        Returns:
            list[Rule]: An empty list, as there are no specific rules defined for pairs.
        """
        return []

    @property
    def tags(self) -> set[str]:
        """Return the tags associated with this pair.

        Returns:
            set[str]: A set containing the tag 'Pair', in addition to any tags from the parent class.
        """
        return super().tags.union({'Pair'})

    @property
    def label(self) -> str:
        """Return the label for the pair.

        Returns:
            str: An empty string, as labels are not set by default.
        """
        return ""

    def glyphs(self) -> list[Glyph]:
        """Generate the glyphs for the pair.

        If a label is set, it returns a glyph representing the edge between the two cells with the label.

        Returns:
            list[Glyph]: A list of glyphs, or an empty list if no label is set.
        """
        if self.label != "":
            return [
                EdgeTextGlyph(
                    self.__class__.__name__,
                    0,
                    self.cell_1.coord.center,
                    self.cell_2.coord.center,
                    self.label
                )
            ]
        return []

    def to_dict(self) -> dict:
        """Return a dictionary representation of the pair.

        Returns:
            dict: A dictionary where the key is the class name and the value is a string representing the pair of cells.
        """
        return {self.__class__.__name__: f"{self.cell_1.row_column_string}-{self.cell_2.row_column_string}"}

    def __repr__(self) -> str:
        """Return a string representation of the Pair instance.

        Returns:
            str: A string representing the Pair instance with its board, cell_1, and cell_2.
        """
        return f"{self.__class__.__name__}({self.board!r}, {self.cell_1!r}, {self.cell_2!r})"
