from typing import Dict

from src.items.board import Board
from src.items.item import Item
from src.items.region_sets import StandardRegionSet
from src.items.row import Row


class Rows(StandardRegionSet):
    """A class representing a collection of rows in a board game.

    This class inherits from StandardRegionSet and initializes a set of Row objects
    based on the given board's row range.
    """

    def __init__(self, board: Board):
        """Initializes the Rows instance.

        Args:
            board (Board): The board that contains the rows.
        """
        super().__init__(board, [Row(board, i) for i in board.row_range])

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        """Creates a Rows instance.

        Args:
            cls: The class itself (Rows).
            board (Board): The board to associate with the rows.
            yaml (Dict): A dictionary containing YAML configuration (not used).

        Returns:
            Item: An instance of Rows.
        """
        return Rows(board)



    def __repr__(self) -> str:
        """Returns a string representation of the Rows instance.

        Returns:
            str: A string representation of the Rows instance.
        """
        return f"{self.__class__.__name__}({self.board!r})"
