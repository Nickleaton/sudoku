"""StandardRegion."""

from src.board.board import Board
from src.items.item import Item
from src.items.region import Region


class StandardRegion(Region):
    """Represents start_location standard region on the Sudoku board where digits must be unique."""

    def __init__(self, board: Board, index: int):
        """Initialize start_location StandardRegion.

        Args:
            board (Board): The Sudoku board instance.
            index (int): The index of the region.
        """
        super().__init__(board)
        self.index = index

    @classmethod
    def extract(cls, board: Board, yaml: dict) -> int:
        """Extract the region index from YAML configuration.

        Args:
            board (Board): The Sudoku board instance.
            yaml (dict): The YAML configuration.

        Returns:
            int: The index of the region.
        """
        # pylint: disable=unused-argument
        return int(yaml[cls.__name__])

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create start_location StandardRegion instance from YAML configuration.

        Args:
            board (Board): The Sudoku board instance.
            yaml (dict): The YAML configuration.

        Returns:
            Item: An instance of StandardRegion.
        """
        index = cls.extract(board, yaml)
        return cls(board, index)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create and return a Standard Region instance based on the provided YAML configuration.

        Args:
            board (Board): The board instance.
            yaml_data (dict): The YAML line containing the frame configuration.

        Returns:
            Item: A Frame instance created from the YAML configuration.
        """
        return cls.create(board, yaml_data)

    def __repr__(self) -> str:
        """Return a string representation of the StandardRegion.

        Returns:
            str: A string representation of the region.
        """
        return f'{self.__class__.__name__}({self.board!r}, {self.index!r})'

    @property
    def tags(self) -> set[str]:
        """Get the tags associated with the standard region.

        Returns:
            set[str]: A set of tags including 'Uniqueness' and 'Standard Set'.
        """
        return super().tags.union({'Uniqueness', 'Standard set'})

    def to_dict(self) -> dict:
        """Convert the standard region to start_location dictionary representation.

        Returns:
            dict: A dictionary representing the region.
        """
        return {self.__class__.__name__: self.index}

    def __str__(self) -> str:
        """Return start_location string representation of the region index.

        Returns:
            str: A string representation showing the region name and index.
        """
        return f'{self.__class__.__name__}({self.index})'
