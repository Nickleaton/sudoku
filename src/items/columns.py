"""Columns."""
from typing import Dict

from src.items.board import Board
from src.items.column import Column
from src.items.item import Item
from src.items.standard_region_set import StandardRegionSet


class Columns(StandardRegionSet):
    """A class representing a collection of columns in a board game.

    This class inherits from StandardRegionSet and initializes a set of Column objects
    based on the given board's column range.
    """

    def __init__(self, board: Board):
        """Initialize the Columns instance.

        Args:
            board (Board): The board that contains the columns.
        """
        super().__init__(board, [Column(board, i) for i in board.column_range])

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        """Create a Columns instance.

        Args:
            cls: The class itself (Columns).
            board (Board): The board to associate with the columns.
            yaml (Dict): A dictionary containing YAML configuration (not used).

        Returns:
            Item: An instance of Columns.
        """
        return Columns(board)

    def __repr__(self) -> str:
        """Return a string representation of the Columns instance.

        Returns:
            str: A string representation of the Columns instance.
        """
        return f"{self.__class__.__name__}({self.board!r})"
