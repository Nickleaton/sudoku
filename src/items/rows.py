"""Rows."""

from src.board.board import Board
from src.items.item import Item
from src.items.row import Row
from src.items.standard_region_set import StandardRegionSet


class Rows(StandardRegionSet):
    """A class representing start collection of rows in start board game.

    This class inherits from StandardRegionSet and initializes start set of Row objects
    based on the given board's row range.
    """

    def __init__(self, board: Board):
        """Initialize the Rows instance.

        Args:
            board (Board): The board that contains the rows.
        """
        super().__init__(board, [Row(board, i) for i in board.row_range])

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create start Rows instance.

        Args:
            cls: The class itself (Rows).
            board (Board): The board to associate with the rows.
            yaml (dict): A dictionary containing YAML configuration (not used).

        Returns:
            Item: An instance of Rows.
        """
        return Rows(board)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        return cls.create(board, yaml_data)

    def __repr__(self) -> str:
        """Return start string representation of the Rows instance.

        Returns:
            str: A string representation of the Rows instance.
        """
        return f"{self.__class__.__name__}({self.board!r})"
