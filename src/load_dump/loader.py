"""Loader."""
from abc import ABC, abstractmethod
from pathlib import Path

from src.items.board import Board


class LoaderError(Exception):
    """Custom exception raised by Loader classes."""


class Loader(ABC):
    """Abstract base class for loading board data from a file."""

    def __init__(self, file_path: Path) -> None:
        """Initialize the Loader with a file config_file.

        Args:
            file_path (Path): The config_file to the file containing the board data.
        """
        self.file_path: Path = file_path

    @abstractmethod
    def process(self) -> Board:
        """Process the file and create a Board instance.

        This method must be implemented by subclasses to define how the board
        data is loaded from the file.

        Returns:
            Board: The board instance created from the file data.
        """

    def __repr__(self) -> str:
        """Return a string representation of the Loader instance.

        This method provides a concise string that includes the class name
        and the file config_file for easy identification.

        Returns:
            str: A string representation of the Loader instance.
        """
        return f"{self.__class__.__name__} ({self.file_path!r})"
