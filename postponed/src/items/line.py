"""Line."""
from collections.abc import Sequence

from src.board.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.region import Region
from src.parsers.cell_list_parser import CellListParser
from src.utils.rule import Rule
from src.validators.line_validator import LineValidator
from src.validators.validator import Validator


class Line(Region):
    """Represents a line consisting of multiple cells on a board."""

    def __init__(self, board: Board, cells: Sequence[Cell]):
        """Initialize a Line instance.

        Args:
            board (Board): The board associated with this line.
            cells (Sequence[Cell]): A sequence of cells that make up this line.
        """
        super().__init__(board)
        self.add_components(cells)

    @classmethod
    def parser(cls) -> CellListParser:
        """Return a CellListParser instance for parsing cell lists.

        Returns:
            CellListParser: An instance for parsing cell lists.
        """
        return CellListParser()

    @classmethod
    def validator(cls) -> Validator:
        """Return the validator for this constraint.

        Returns:
            Validator: The appropriate validator for this constraint.
        """
        return LineValidator()

    @classmethod
    def is_sequence(cls) -> bool:
        """Indicate whether this constraint is a sequence.

        Returns:
            bool: True if this constraint is a sequence.
        """
        return True

    @classmethod
    def extract(cls, board: Board, yaml: dict) -> list[Cell]:
        """Extract a list of Cell instances from the provided YAML dictionary.

        Args:
            board (Board): The board associated with the cells.
            yaml (dict): A dictionary containing the YAML line.

        Returns:
            list[Cell]: A list of Cell instances extracted from the YAML line.
        """
        return [Cell.make(board, int(part.strip()[0]), int(part.strip()[1])) for part in yaml[cls.__name__].split(',')]

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create a Line instance from a YAML dictionary.

        Args:
            board (Board): The board associated with the line.
            yaml (dict): A dictionary containing the YAML line.

        Returns:
            Item: A new instance of Line created from the YAML line.
        """
        cells = cls.extract(board, yaml)
        return cls(board, cells)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create a Line instance from a YAML dictionary using the parser.

        Args:
            board (Board): The board associated with the line.
            yaml_data (dict): A dictionary containing the YAML line.

        Returns:
            Item: A new instance of Line created from the YAML line.
        """
        cell_data = yaml_data[cls.__name__]
        parser = cls.parser()
        parser.parse(cell_data)
        cells = [Cell.make(board, cell['row'], cell['column']) for cell in parser.answer]
        return cls(board, cells)

    def __repr__(self) -> str:
        """Return a string representation of this line.

        Returns:
            str: A string representation of the Line instance, including the board and cells.
        """
        cell_str = ', '.join(repr(cell) for cell in self.cells)
        return f'{self.__class__.__name__}({self.board!r}, [{cell_str}])'

    @property
    def rules(self) -> list[Rule]:
        """Return an empty list of rules associated with this line.

        Returns:
            list[Rule]: An empty list of rules.
        """
        return []

    @property
    def tags(self) -> set[str]:
        """Return a set of tags associated with this line.

        Returns:
            set[str]: A set containing the tags associated with this line.
        """
        return super().tags.union({'Line'})

    def to_dict(self) -> dict:
        """Convert the line to a dictionary representation.

        Returns:
            dict: A dictionary representation of the line, including the cells.
        """
        return {self.__class__.__name__: ', '.join([cell.row_column_string for cell in self.cells])}
