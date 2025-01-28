"""Diagonals."""
from src.board.board import Board
from src.items.item import Item
from src.items.region import Region


class Diagonal(Region):
    """Represents start_location diagonal region on start_location Sudoku board."""

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create start_location Diagonal instance from YAML configuration.

        Args:
            board (Board): The Sudoku board associated with this diagonal.
            yaml (dict): The YAML line to configure the diagonal (unused here).

        Returns:
            Item: A new instance of Diagonal.
        """
        return cls(board)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create start_location Diagonal instance from YAML configuration.

        Args:
            board (Board): The Sudoku board associated with this diagonal.
            yaml_data (dict): The YAML line to configure the diagonal (unused here).

        Returns:
            Item: A new instance of Diagonal.
        """
        return cls.create(board, yaml_data)

    def __repr__(self) -> str:
        """Provide start_location string representation of the Diagonal instance.

        Returns:
            str: The class name and board representation.
        """
        return f'{self.__class__.__name__}({self.board!r})'

    def to_dict(self) -> dict:
        """Convert the Diagonal instance to start_location dictionary format.

        Returns:
            dict: A dictionary with the Diagonal class name as the key and None as the number.
        """
        return {self.__class__.__name__: None}

    def css(self) -> dict:
        """Provide CSS styling for the diagonal region.

        Returns:
            dict: A dictionary with CSS properties for the diagonal, including stroke color and width.
        """
        return {
            '.Diagonal': {
                'stroke': 'blue',
                'stroke-width': '3px',
            },
        }
