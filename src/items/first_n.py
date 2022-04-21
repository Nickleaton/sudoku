"""First N cells from a given side and index."""
from typing import List, Dict, Any

from src.items.board import Board
from src.items.cell import Cell
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

    @staticmethod
    def validate(board: Board, yaml: Any) -> List[str]:
        if not isinstance(yaml, str):
            return [f"Expected str, got {yaml!r}"]
        if len(yaml) != 2:
            return [f"Expected side|index, got {yaml!r}"]
        result = []
        if not Side.valid(yaml[0]):
            result.append(f"Side not valid {yaml[0]}")
        if not yaml[1].isdigit():
            result.append(f"Index not valid {yaml[1]}")
            return result
        if len(result) > 0:
            return result
        if Side(yaml[0]) in [Side.LEFT, Side.RIGHT]:
            if int(yaml[1]) not in board.column_range:
                result.append(f'Index outside range {yaml[1]}')
        else:
            if int(yaml[1]) not in board.row_range:
                result.append(f'Index outside range {yaml[1]}')
        return result

    @staticmethod
    def extract(board: Board, yaml: Any) -> Any:
        side = Side.create(yaml[0])
        index = int(yaml[1])
        return side, index

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> 'FirstN':
        FirstN.validate(board, yaml)
        side, index = FirstN.extract(board, yaml)
        return cls(board, side, index)
