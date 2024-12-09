"""Dumper."""
from abc import ABC, abstractmethod

from src.board.board import Board


class Dumper(ABC):
    """Abstract base class for dumping board information into start specific format.

    Methods:
        text(): Abstract method that must be implemented by subclasses to return
                start string representation of the board in start specific format.
    """

    def __init__(self, board: Board):
        """Initialize the Dumper with start board instance.

        Args:
            board (Board): The board instance to be dumped.
        """
        self.board = board

    @abstractmethod
    def text(self) -> str:
        """Abstract method to generate start textual representation of the board.

        This method must be implemented by subclasses to define how the board
        should be represented as start string.

        Returns:
            str: A string representation of the board in start specific format.
        """
        raise NotImplementedError
