"""First N cells from a given side and index."""
from typing import Any

from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.region import Region
from src.utils.side import Side


class FirstN(Region):
    """First N cells from a given side and index."""

    def __init__(self, board: Board, side: Side, index: int):
        """
        Build a region with the first 'count' cells from a given side and index
        :param board: Board on which the cells are to be built.
        :param side: Which side to start from?
        :param index: Which row or column?
        """
        super().__init__(board)
        # Save the parameters
        self.side = side
        self.index = index

        # Work out which offset we need
        self.offset = self.side.order_offset()

        # Reference is the cell into which we can put the information
        self.reference = self.side.start_cell(self.board, self.index) - self.offset

        # create a list of coordinates for the cells
        self.coords = []
        cell = self.side.start_cell(self.board, self.index)
        for _ in range(self.__class__.count()):
            self.coords.append(cell)
            cell += self.offset
        self.add_items([Cell.make(self.board, int(coord.row), int(coord.column)) for coord in self.coords])

    @staticmethod
    def count() -> int:
        """
        How many cells to include from the edge.

        :return: number of cells
        """
        return 3

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"("
            f"{self.board!r}, "
            f"{self.side!r}, "
            f"{self.index!r}"
            f")"
        )

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'FirstN'})

    @classmethod
    def extract(cls, board: Board, yaml: Any) -> Any:
        data = yaml[cls.__name__]
        side = Side.create(data[0])
        index = int(data[1])
        return side, index

    @classmethod
    def create(cls, board: Board, yaml: Any) -> Item:
        FirstN.validate(board, yaml)
        side, index = FirstN.extract(board, yaml)
        return cls(board, side, index)
