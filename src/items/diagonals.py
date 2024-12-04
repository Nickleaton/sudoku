"""Diagonals."""
from src.items.board import Board
from src.items.item import Item
from src.items.region import Region


class Diagonal(Region):
    """Represents a diagonal region on a Sudoku board."""

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create a Diagonal instance from YAML configuration.

        Args:
            board (Board): The Sudoku board associated with this diagonal.
            yaml (dict): The YAML data to configure the diagonal (unused here).

        Returns:
            Item: A new instance of Diagonal.
        """
        return cls(board)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        return cls.create(board, yaml_data)

    def __repr__(self) -> str:
        """Provide a string representation of the Diagonal instance.

        Returns:
            str: The class name and board representation.
        """
        return f"{self.__class__.__name__}({self.board!r})"

    def to_dict(self) -> dict:
        """Convert the Diagonal instance to a dictionary format.

        Returns:
            dict: A dictionary with the Diagonal class name as the key and None as the value.
        """
        return {self.__class__.__name__: None}

    def css(self) -> dict:
        """Provide CSS styling for the diagonal region.

        Returns:
            dict: A dictionary with CSS properties for the diagonal, including stroke color and width.
        """
        return {
            ".Diagonal": {
                "stroke": "blue",
                "stroke-width": "3px"
            }
        }
