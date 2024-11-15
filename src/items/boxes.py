"""Boxes."""
from typing import Dict

from src.items.board import Board
from src.items.box import Box
from src.items.item import Item
from src.items.standard_region_set import StandardRegionSet
from src.utils.sudoku_exception import SudokuException


class Boxes(StandardRegionSet):
    """A class representing a collection of boxes in a board game.

    This class inherits from StandardRegionSet and initializes a set of Box objects
    based on the given board's box range.
    """

    def __init__(self, board: Board):
        """Initialize the Boxes instance.

        Args:
            board (Board): The board that contains the boxes.

        Raises:
            AssertionError: If the board's box_range is None.
        """
        if board.box_range is None:
            raise SudokuException("box_range cannot be None.")
        super().__init__(board, [Box(board, i) for i in board.box_range])

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        """Create a Boxes instance.

        Args:
            cls: The class itself (Boxes).
            board (Board): The board to associate with the boxes.
            yaml (Dict): A dictionary containing YAML configuration (not used).

        Returns:
            Item: An instance of Boxes.
        """
        return Boxes(board)

    def __repr__(self) -> str:
        """Return a string representation of the Boxes instance.

        Returns:
            str: A string representation of the Boxes instance.
        """
        return f"{self.__class__.__name__}({self.board!r})"
