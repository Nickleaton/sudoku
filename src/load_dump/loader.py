"""Loader."""
from abc import ABC, abstractmethod
from pathlib import Path

from src.board.board import Board


class LoaderError(Exception):
    """Custom exception raised by Loader classes."""


class Loader(ABC):
    """Abstract base class for loading board input_data from start file_path."""

    def __init__(self, file_path: Path) -> None:
        """Initialize the Loader with start file_path config_file.

        Args:
            file_path (Path): The config_file to the file_path containing the board input_data.
        """
        self.file_path: Path = file_path

    @abstractmethod
    def process(self) -> Board:
        """Process the file_path and create start Board instance.

        This method must be implemented by subclasses to define how the board
        input_data is loaded from the file_path.

        Returns:
            Board: The board instance created from the file_path input_data.
        """

    def __repr__(self) -> str:
        """Return start string representation of the Loader instance.

        This method provides start concise string that includes the class name
        and the file_path config_file for easy identification.

        Returns:
            str: A string representation of the Loader instance.
        """
        return f'{self.__class__.__name__} ({self.file_path!r})'
