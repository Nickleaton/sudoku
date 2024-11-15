"""Known."""
from typing import List, Any, Dict, Type

# Import statements for the required classes and types used in Known
from src.items.board import Board
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

CELL_TYPE_MAP: Dict[str, Type[SimpleCellReference]] = {
    'f': FortressCell,
    'l': LowCell,
    'm': MidCell,
    'h': HighCell,
    'e': EvenCell,
    'o': OddCell
}


class Known(ComposedItem):
    """Represent a collection of cells with known characteristics on the board."""

    def __init__(self, board: Board, rows: List[str]):
        """Initialize the Known object with a board and a list of row data.

        Args:
            board (Board): The board instance associated with the Known cells.
            rows (List[str]): A list of strings representing the rows of cells,
                              where each character represents a cell type.
        """
        super().__init__(board, [])
        self.rows = rows
        parts: List[CellReference] = []

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
        """Return True if this item is a sequence.

        Returns:
            bool: Always returns True as Known represents a sequence.
        """
        return True

    @classmethod
    def is_composite(cls) -> bool:
        """Return True if this item is a composite.

        Returns:
            bool: Always returns True as Known is a composite of items.
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
    def extract(cls, board: Board, yaml: Dict) -> Any:
        """Extract a list of row strings from a YAML dictionary for Known.

        Args:
            board (Board): The board instance.
            yaml (Dict): The YAML data to extract from.

        Returns:
            Any: A list of row strings extracted from the YAML data.
        """
        result: List[str] = [y for y in yaml]
        return result

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        """Create a Known instance from YAML data.

        Args:
            board (Board): The board instance.
            yaml (Dict): The YAML data to create the Known instance from.

        Returns:
            Item: A new instance of Known initialized with the extracted rows.
        """
        items = Known.extract(board, yaml[cls.__name__])
        return Known(board, items)

    def line_str(self) -> List[str]:
        """Return a list of row strings representing the board layout for Known items.

        Returns:
            List[str]: A list of strings where each string represents a row of the board.
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

    def to_dict(self) -> Dict[str, List[str]]:
        """Convert the Known instance into a dictionary format.

        Returns:
            Dict[str, List[str]]: A dictionary representation of the Known instance with line_str as values.
        """
        return {self.__class__.__name__: self.line_str()}
