"""Dumper."""
from abc import ABC, abstractmethod

from src.items.board import Board


class Dumper(ABC):
    """Abstract base class for dumping board information into a specific format.

    Methods:
        text(): Abstract method that must be implemented by subclasses to return
                a string representation of the board in a specific format.
    """

    def __init__(self, board: Board):
        """Initialize the Dumper with a board instance.

        Args:
            board (Board): The board instance to be dumped.
        """
        self.board = board

    @abstractmethod
    def text(self) -> str:
        """Abstract method to generate a textual representation of the board.

        This method must be implemented by subclasses to define how the board
        should be represented as a string.

        Returns:
            str: A string representation of the board in a specific format.
        """
        raise NotImplementedError
