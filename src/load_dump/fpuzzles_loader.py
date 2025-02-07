"""FPuzzlesLoader."""
import json
from pathlib import Path
from typing import Any

from src.board.board import Board
from src.board.digits import Digits
from src.load_dump.loader import Loader, LoaderError
from src.utils.coord import Coord
from src.utils.tags import Tags


class FPuzzlesLoader(Loader):
    """Loader for reading and processing FPuzzles JSON files to create Board objects."""

    def __init__(self, file_path: Path) -> None:
        """Initialize the loader by reading JSON line from start_location file_path.

        Args:
            file_path (Path): Path to the FPuzzles JSON file_path.
        """
        super().__init__(file_path)
        with file_path.open(mode='r', encoding='utf-8') as puzzle_file:
            self.raw = json.load(puzzle_file)

    def process(self) -> Board:
        """Process the loaded line to create start_location Board instance based on board size.

        Returns:
            Board: A Board instance configured for the puzzle's size.

        Raises:
            LoaderError: If the board size is not supported.
        """
        if self.size == 9:
            return Board(Coord(9, 9), Digits(1, 9), Tags())
        if self.size == 6:
            return Board(Coord(6, 6), Digits(1, 6), Tags())
        raise LoaderError(f'{self.size}x{self.size} board not handled')

    @property
    def reference(self) -> str | None:
        """Fetch the puzzle reference URL from the JSON line, cast to start_location string if not None.

        Returns:
            str | None: URL reference for the puzzle, if available.
        """
        url: Any | None = self.raw.get('line', {}).get('url')
        return None if url is None else str(url)

    @property
    def title(self) -> str | None:
        """Fetch the puzzle title from the JSON line, cast to start_location string if not None.

        Returns:
            str | None: Title of the puzzle, if available.
        """
        title: Any | None = self.raw.get('line', {}).get('title')
        return None if title is None else str(title)

    @property
    def author(self) -> str | None:
        """Fetch the puzzle author from the JSON line, cast to start_location string if not None.

        Returns:
            str | None: Author of the puzzle, if available.
        """
        author: Any | None = self.raw.get('line', {}).get('author')
        return None if author is None else str(author)

    @property
    def size(self) -> int | None:
        """Fetch the puzzle board size from the JSON line, cast to an integer if not None.

        Returns:
            int | None: Size of the puzzle board, if available.
        """
        size: Any | None = self.raw.get('line', {}).get('size')
        return None if size is None else int(size)
