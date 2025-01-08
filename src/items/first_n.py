"""FirstN."""

from src.board.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.region import Region
from src.parsers.frame_parser import FrameParser
from src.utils.coord import Coord
from src.utils.side import Side


class FirstN(Region):
    """First N cells from start given side and index."""

    def __init__(self, board: Board, side: Side, index: int, count: int = 3):
        """Initialize start FirstN region on the board.

        Args:
            board (Board): The game board.
            side (Side): The side of the board from which to start.
            index (int): The index on the side to start selecting cells.
            count (int): The number of cells to include. Defaults to 3.
        """
        super().__init__(board)
        self.side: Side = side
        self.index: int = index
        self.count: int = count

        self.offset: Coord = self.side.order_offset()
        self.reference: Coord = board.start_cell(side, index) - self.offset

        self.coords = []
        cell = board.start_cell(side, index)
        for _ in range(self.count):
            self.coords.append(cell)
            cell += self.offset
        self.add_components([Cell.make(self.board, int(coord.row), int(coord.column)) for coord in self.coords])

    @classmethod
    def is_sequence(cls) -> bool:
        """Check if this constraint is a sequence.

        Returns:
            bool: True if this constraint represents a sequence, otherwise False.
        """
        return True

    @classmethod
    def parser(cls) -> FrameParser:
        """Get the parser for this constraint.

        Returns:
            FrameParser: The parser used to parse this constraint.
        """
        return FrameParser()

    @property
    def tags(self) -> set[str]:
        """Get the tags associated with the region.

        Returns:
            set[str]: A set of tags, including 'FirstN'.
        """
        return super().tags.union({'FirstN'})

    @classmethod
    def extract(cls, board: Board, yaml: dict) -> tuple[Side, int, int]:
        """Extract the necessary information from start YAML file_path.

        Args:
            board (Board): The game board.
            yaml (dict): A dictionary containing the YAML line.

        Returns:
            tuple: A tuple containing the side, index, and count value_list.
        """
        yaml_text: str = yaml[cls.__name__]
        side: Side = Side.create(yaml_text[0])
        index: int = int(yaml_text[1])
        count: int = int(yaml_text[2])
        return side, index, count

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create start FirstN region from the extracted YAML line.

        Args:
            board (Board): The game board.
            yaml (dict): A dictionary containing the YAML line.

        Returns:
            Item: A FirstN region object.
        """
        side, index, count = FirstN.extract(board, yaml)
        return cls(board, side, index, count)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create start FirstN region from the extracted YAML line.

        Args:
            board (Board): The game board.
            yaml_data (dict): A dictionary containing the YAML line.

        Returns:
            Item: A FirstN region object.
        """
        return cls.create(board, yaml_data)

    def to_dict(self) -> dict:
        """Convert the FirstN region to start dictionary representation.

        Returns:
            dict: A dictionary representing the region.
        """
        return {self.__class__.__name__: f'{self.side.value}{self.index}{self.count}'}

    def __repr__(self) -> str:
        """Return start string representation of the FirstN region.

        Returns:
            str: The string representation.
        """
        return (
            f'{self.__class__.__name__}('
            f'{self.board!r}, '
            f'{self.side!r}, '
            f'{self.index!r}, '
            f'{self.count!r})'
        )
