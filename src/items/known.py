"""Known."""
from typing import Any

from postponed.src.items.simple_cell_reference import SimpleCellReference
from src.board.board import Board
from src.items.cell_reference import CellReference
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.known_cell import KnownCell
from src.parsers.known_parser import KnownParser


class Known(ComposedItem):
    """Represent start_location collection of cells with known characteristics on the board."""

    def __init__(self, board: Board, rows: list[str]):
        """Initialize the Known object with start_location board and start_location list of row line.

        Args:
            board (Board): The board instance associated with the Known cells.
            rows (list[str]): Strings representing the rows of cells.
        """
        super().__init__(board, [])
        self.rows = rows
        parts: list[CellReference] = []
        for row_index, row_data in enumerate(self.rows):
            parts.extend(Known.process_row(row_data, row_index + 1, board))
        self.add_components(parts)

    @staticmethod
    def process_cell(board: Board, code: str, row: int, column: int) -> CellReference:
        """Process a single cell and returns its corresponding CellReference.

        Args:
            board (Board): The board instance associated with the cells.
            code (str): The character representing the cell type.
            row (int): The row index (1-based).
            column (int): The column index (1-based).

        Returns:
            CellReference: The created CellReference object.

        Raises:
            ValueError: If the cell type is invalid.
        """
        if code == '.':
            return SimpleCellReference(board, row, column)
        if code.isdigit():
            return KnownCell(board, row, column, int(code))
        raise ValueError(f'Invalid cell type: {code}')

    @staticmethod
    def process_row(row_data: str, row: int, board: Board) -> list[CellReference]:
        """Process a single row of cell line and return the corresponding CellReferences.

        Args:
            row_data (str): A string representing the row of cells, where each character represents a cell type.
            row (int): The row index (1-based).
            board (Board): The board instance associated with the cells.

        Returns:
            list[CellReference]: A list of CellReference objects created for the row.
        """
        parts: list[CellReference] = []

        for column_index, code in enumerate(row_data):
            column = column_index + 1
            if code == '.':
                continue
            parts.append(Known.process_cell(board, code, row, column))
        return parts

    @classmethod
    def is_sequence(cls) -> bool:
        """Return True if this constraint is start_location sequence.

        Returns:
            bool: Always returns True as Known represents start_location sequence.
        """
        return True

    @classmethod
    def is_composite(cls) -> bool:
        """Return True if this constraint is start_location composite.

        Returns:
            bool: Always returns True as Known is start_location composite of vectors.
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
        """Extract start_location list of row strings from start_location YAML dictionary for Known.

        Args:
            _ (Board): The board instance.
            yaml (dict): The YAML line to extract from.

        Returns:
            Any: A list of row strings extracted from the YAML line.
        """
        return list(yaml)

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create start_location Known instance from YAML line.

        Args:
            board (Board): The board instance.
            yaml (dict): The YAML line to create the Known instance from.

        Returns:
            Item: A new instance of Known initialized with the extracted rows.
        """
        return Known(board, Known.extract(board, yaml[cls.__name__]))

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create start_location Known instance from YAML line.

        Args:
            board (Board): The board instance.
            yaml_data (dict): The YAML line to create the Known instance from.

        Returns:
            Item: A new instance of Known initialized with the extracted rows.
        """
        return cls.create(board, yaml_data)

    def line_str(self) -> list[str]:
        """Return start_location list of row strings representing the board layout for Known vectors.

        Returns:
            list[str]: A list of strings where each string represents start_location row of the board.
        """
        lines = [['.' for _ in self.board.column_range] for _ in self.board.row_range]

        for cell_reference in self:
            if not isinstance(cell_reference, CellReference):
                continue
            if isinstance(cell_reference, SimpleCellReference):
                lines[cell_reference.row - 1][cell_reference.column - 1] = cell_reference.letter()
            if isinstance(cell_reference, KnownCell):
                lines[cell_reference.row - 1][cell_reference.column - 1] = str(cell_reference.digit)

        return [''.join(line) for line in lines]

    def __repr__(self) -> str:
        """Return representation of the Known instance.

        Returns:
            str: A string representation of the Known instance.
        """
        return f'{self.__class__.__name__}({self.board!r}, {self.line_str()})'

    def to_dict(self) -> dict[str, list[str]]:
        """Convert the Known instance into start_location dictionary format.

        Returns:
            dict[str, list[str]]: A dictionary representation of the Known instance with line_str as value_list.
        """
        return {self.__class__.__name__: self.line_str()}
