"""First N cells from a given side and index."""
from typing import Any, Dict

from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.region import Region
from src.parsers.frame_parser import FrameParser
from src.utils.coord import Coord
from src.utils.side import Side


class FirstN(Region):
    """First N cells from a given side and index."""

    def __init__(self, board: Board, side: Side, index: int, count: int = 3):
        """Initialize a FirstN region on the board.

        Args:
            board (Board): The game board.
            side (Side): The side of the board from which to start.
            index (int): The index on the side to start selecting cells.
            count (int, optional): The number of cells to include. Defaults to 3.
        """
        super().__init__(board)
        self.side: Side = side
        self.index: int = index
        self.count: int = count

        self.offset: Coord = self.side.order_offset()

        self.reference: Coord = self.side.start_cell(self.board, self.index) - self.offset

        self.coords = []
        cell = self.side.start_cell(self.board, self.index)
        for _ in range(self.count):
            self.coords.append(cell)
            cell += self.offset
        self.add_items([Cell.make(self.board, int(coord.row), int(coord.column)) for coord in self.coords])

    @classmethod
    def is_sequence(cls) -> bool:
        """Return True if this item is a sequence."""
        return True

    @classmethod
    def parser(cls) -> FrameParser:
        """Return the parser for this item."""
        return FrameParser()

    @property
    def tags(self) -> set[str]:
        """Return a set of tags associated with the region.

        Returns:
            set[str]: The set of tags, including 'FirstN'.
        """
        return super().tags.union({'FirstN'})

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Any:
        """Extract the necessary information from a YAML file.

        Args:
            board (Board): The game board.
            yaml (Dict): A dictionary containing the YAML data.

        Returns:
            tuple: A tuple containing the side, index, and count values.
        """
        data = yaml[cls.__name__]
        side = Side.create(data[0])
        index = int(data[1])
        count = int(data[2])
        return side, index, count

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        """Create a FirstN region from the extracted YAML data.

        Args:
            board (Board): The game board.
            yaml (Dict): A dictionary containing the YAML data.

        Returns:
            Item: A FirstN region object.
        """
        side, index, count = FirstN.extract(board, yaml)
        return cls(board, side, index, count)

    def to_dict(self) -> Dict:
        """Convert the FirstN region to a dictionary representation.

        Returns:
            Dict: A dictionary representing the region.
        """
        return {self.__class__.__name__: f"{self.side.value}{self.index}{self.count}"}

    def __repr__(self) -> str:
        """Return a string representation of the FirstN region.

        Returns:
            str: The string representation.
        """
        return (
            f"{self.__class__.__name__}("
            f"{self.board!r}, "
            f"{self.side!r}, "
            f"{self.index!r}, "
            f"{self.count!r})"
        )
