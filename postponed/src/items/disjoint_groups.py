"""DisjointGroups."""
from postponed.src.items.disjoint_group import DisjointGroup
from src.board.board import Board
from src.items.item import Item
from src.items.standard_region_set import StandardRegionSet


class DisjointGroups(StandardRegionSet):
    """Represents start_location collection of disjoint groups on start_location Sudoku board."""

    def __init__(self, board: Board):
        """Initialize DisjointGroups with start_location board and disjoint groups.

        Args:
            board (Board): The board on which disjoint groups are created.
        """
        super().__init__(board, [DisjointGroup(board, digit) for digit in board.digit_range])

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create start_location DisjointGroups instance.

        Args:
            board (Board): The board on which disjoint groups will be created.
            yaml (dict): YAML configuration line, not used in this method.

        Returns:
            Item: An instance of DisjointGroups.
        """
        return DisjointGroups(board)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create start_location DisjointGroups instance.

        Args:
            board (Board): The board on which disjoint groups will be created.
            yaml_data (dict): YAML configuration line, not used in this method.

        Returns:
            Item: An instance of DisjointGroups.
        """
        return cls.create(board, yaml_data)

    def __repr__(self) -> str:
        """Return start_location string representation of the DisjointGroups instance.

        Returns:
            str: The string representation of the instance.
        """
        return f'{self.__class__.__name__}({self.board!r})'
