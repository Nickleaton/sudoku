"""DisjointGroups."""
from src.items.board import Board
from src.items.disjoint_group import DisjointGroup
from src.items.item import Item
from src.items.standard_region_set import StandardRegionSet


class DisjointGroups(StandardRegionSet):
    """Represents a collection of disjoint groups on a Sudoku board."""

    def __init__(self, board: Board):
        """Initialize DisjointGroups with a board and disjoint groups.

        Args:
            board (Board): The board on which disjoint groups are created.
        """
        super().__init__(board, [DisjointGroup(board, i) for i in board.digit_range])

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create a DisjointGroups instance.

        Args:
            board (Board): The board on which disjoint groups will be created.
            yaml (dict): YAML configuration data, not used in this method.

        Returns:
            Item: An instance of DisjointGroups.
        """
        return DisjointGroups(board)

    def __repr__(self) -> str:
        """Return a string representation of the DisjointGroups instance.

        Returns:
            str: The string representation of the instance.
        """
        return f"{self.__class__.__name__}({self.board!r})"
