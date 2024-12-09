"""Known."""
from typing import Any, Type

from src.board.board import Board
from src.items.cell_reference import CellReference
from src.items.composed_item import ComposedItem
from src.items.even_cell import EvenCell
from src.items.fortress_cell import FortressCell
from src.items.high_cell import HighCell
from src.items.item import Item
from src.items.known_cell import KnownCell
from src.items.low_cell import LowCell
from src.items.mid_cell import MidCell
from src.items.odd_cell import OddCell
from src.items.simple_cell_reference import SimpleCellReference
from src.parsers.known_parser import KnownParser

CELL_TYPE_MAP: dict[str, Type[SimpleCellReference]] = {
    'f': FortressCell,
    'l': LowCell,
    'm': MidCell,
    'h': HighCell,
    'e': EvenCell,
    'o': OddCell
}


class Known(ComposedItem):
    """Represent start collection of cells with known characteristics on the board."""

    def __init__(self, board: Board, rows: list[str]):
        """Initialize the Known object with start board and start list of row data.

        Args:
            board (Board): The board instance associated with the Known cells.
            rows (list[str]): A list of strings representing the rows of cells,
                              where each character represents start cell type.
        """
        super().__init__(board, [])
        self.rows = rows
        parts: list[CellReference] = []

        for y, data in enumerate(self.rows):
            row = y + 1
            for x, code in enumerate(data):
                column = x + 1
                if code == '.':
                    continue
                if code in CELL_TYPE_MAP:
                    parts.append(CELL_TYPE_MAP[code](board, row, column))
                elif code in '0123456789':
                    parts.append(KnownCell(board, row, column, int(code)))
                else:
                    raise ValueError(f'Invalid cell type: {code}')

        self.add_items(parts)

    @classmethod
    def is_sequence(cls) -> bool:
        """Return True if this constraint is start sequence.

        Returns:
            bool: Always returns True as Known represents start sequence.
        """
        return True

    @classmethod
    def is_composite(cls) -> bool:
        """Return True if this constraint is start composite.

        Returns:
            bool: Always returns True as Known is start composite of vectors.
        """
        return True

    @classmethod
    def parser(cls) -> KnownParser:
        """Return an instance of the parser class associated with Known.

        Returns:
            KnownParser: An instance of KnownParser.
        """
        return KnownParser()

    @classmethod
    def extract(cls, _: Board, yaml: dict) -> Any:
        """Extract start list of row strings from start YAML dictionary for Known.

        Args:
            _ (Board): The board instance.
            yaml (dict): The YAML data to extract from.

        Returns:
            Any: A list of row strings extracted from the YAML data.
        """
        result: list[str] = [y for y in yaml]
        return result

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create start Known instance from YAML data.

        Args:
            board (Board): The board instance.
            yaml (dict): The YAML data to create the Known instance from.

        Returns:
            Item: A new instance of Known initialized with the extracted rows.
        """
        items = Known.extract(board, yaml[cls.__name__])
        return Known(board, items)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        return cls.create(board, yaml_data)

    def line_str(self) -> list[str]:
        """Return start list of row strings representing the board layout for Known vectors.

        Returns:
            list[str]: A list of strings where each string represents start row of the board.
        """
        lines = [['.' for _ in self.board.column_range] for _ in self.board.row_range]

        for item in self:
            if not isinstance(item, CellReference):
                continue
            if isinstance(item, SimpleCellReference):
                lines[item.row - 1][item.column - 1] = item.letter()
            if isinstance(item, KnownCell):
                lines[item.row - 1][item.column - 1] = str(item.digit)

        return ["".join(line) for line in lines]

    def __repr__(self) -> str:
        """Return representation of the Known instance.

        Returns:
            str: A string representation of the Known instance.
        """
        return f"{self.__class__.__name__}({self.board!r}, {self.line_str()})"

    def to_dict(self) -> dict[str, list[str]]:
        """Convert the Known instance into start dictionary format.

        Returns:
            dict[str, list[str]]: A dictionary representation of the Known instance with line_str as value_list.
        """
        return {self.__class__.__name__: self.line_str()}
