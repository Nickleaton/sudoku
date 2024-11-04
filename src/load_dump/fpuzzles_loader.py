import json
from typing import Optional, Any

from src.items.board import Board
from src.load_dump.loader import Loader, LoaderError


class FPuzzlesLoader(Loader):
    """Loader for reading and processing FPuzzles JSON files to create Board objects."""

    def __init__(self, filename: str) -> None:
        """Initializes the loader by reading JSON data from a file.

        Args:
            filename (str): Path to the FPuzzles JSON file.
        """
        super().__init__(filename)
        with open(filename, 'r') as file:
            self.raw = json.load(file)

    def process(self) -> Board:
        """Processes the loaded data to create a Board instance based on board size.

        Returns:
            Board: A Board instance configured for the puzzle's size.

        Raises:
            LoaderError: If the board size is not supported.
        """
        if self.size == 9:
            return Board(
                board_rows=9,
                board_columns=9,
                box_rows=3,
                box_columns=3,
                reference=self.reference,
                video=None,
                title=self.title,
                author=self.author
            )
        if self.size == 6:
            return Board(
                board_rows=6,
                board_columns=6,
                box_rows=3,
                box_columns=2,
                reference=self.reference,
                video=None,
                title=self.title,
                author=self.author
            )
        raise LoaderError(f"{self.size}x{self.size} board not handled")

    @property
    def reference(self) -> Optional[str]:
        """Fetches the puzzle reference URL from the JSON data, cast to a string if not None.

        Returns:
            Optional[str]: URL reference for the puzzle, if available.
        """
        url: Optional[Any] = self.raw.get('data', {}).get('url')
        return str(url) if url is not None else None

    @property
    def title(self) -> Optional[str]:
        """Fetches the puzzle title from the JSON data, cast to a string if not None.

        Returns:
            Optional[str]: Title of the puzzle, if available.
        """
        title: Optional[Any] = self.raw.get('data', {}).get('title')
        return str(title) if title is not None else None

    @property
    def author(self) -> Optional[str]:
        """Fetches the puzzle author from the JSON data, cast to a string if not None.

        Returns:
            Optional[str]: Author of the puzzle, if available.
        """
        author: Optional[Any] = self.raw.get('data', {}).get('author')
        return str(author) if author is not None else None

    @property
    def size(self) -> Optional[int]:
        """Fetches the puzzle board size from the JSON data, cast to an int if not None.

        Returns:
            Optional[int]: Size of the puzzle board, if available.
        """
        size: Optional[Any] = self.raw.get('data', {}).get('size')
        return int(size) if size is not None else None
