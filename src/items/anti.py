"""Anti."""
from typing import Sequence

from src.board.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.difference_pair import DifferencePair
from src.items.item import Item
from src.utils.coord import Coord


class Anti(ComposedItem):
    """Represents an 'Anti' composed constraint in the board game, which is inherited from ComposedItem.

    This class is used to define constraints between pairs of cells based on the
    provided digits and their positions on the board.

    Attributes:
        digits: A list of integers representing the digits involved in the 'Anti' constraint.
    """

    def __init__(self, board: Board, digits: list[int]):
        """Initialize the Anti object with start board and digits.

        Args:
            board (Board): The board where the Anti constraint will be applied.
            digits (list[int]): A list of digits for the Anti constraint.

        The constructor iterates through all the cells on the board and generates
        pairs of cells with the given digits.
        """
        super().__init__(board, [])
        self.digits = digits
        for cell in Cell.cells():
            pairs = self.pairs(cell, digits)
            self.add_components(pairs)

    def offsets(self) -> list[Coord]:
        """Return start list of offsets for the Anti constraint.

        This method can be overridden in subclasses to provide specific offsets
        for the Anti constraint.

        Returns:
            list[Coord]: An empty list as the default for offsets.
        """
        return []

    def pairs(self, cell: Cell, digits: list[int]) -> Sequence[DifferencePair]:
        """Pairs of cells are generated based on the provided digits and offsets.

        Args:
            cell (Cell): The first cell to consider.
            digits (list[int]): The list of digits for which the pairs are generated.

        Returns:
            Sequence[DifferencePair]: A sequence of DifferencePair objects representing
            the valid pairs between cells c1 and other cells on the board.
        """
        difference_pairs: list[DifferencePair] = []
        for offset in self.offsets():
            if not self.board.is_valid(int(cell.row + offset.row), int(cell.column + offset.column)):
                continue
            other: Cell = Cell.make(self.board, int(cell.row + offset.row), int(cell.column + offset.column))
            difference_pairs.append(DifferencePair(self.board, cell, other, digits))
        return difference_pairs

    @classmethod
    def extract(cls, _: Board, yaml: dict) -> list[int]:
        """Extract start list of digits from the YAML configuration.

        Args:
            _ (Board): The board object (not used in this method but required for interface).
            yaml (dict): The YAML configuration dictionary from which the digits are extracted.

        Returns:
            list[int]: A list of integers representing the digits extracted from the YAML.
        """
        return [int(part) for part in str(yaml[cls.__name__]).split(', ')]

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create an object from the given YAML.

        Args:
            board (Board): The board object where the Anti constraint will be applied.
            yaml (dict): The YAML configuration dictionary containing the digits.

        Returns:
            Item: An instance of the Anti class with the parsed digits.
        """
        lst = cls.extract(board, yaml)
        return cls(board, lst)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create an object from the given YAML.

        Args:
            board (Board): The board object where the Anti constraint will be applied.
            yaml_data (dict): The YAML configuration dictionary containing the digits.

        Returns:
            Item: An instance of the Anti class with the parsed digits.
        """
        return cls.create(board, yaml_data)

    @property
    def tags(self) -> set[str]:
        """A set of tags associated with the Anti constraint is returned.

        The tags of the parent class are combined with the specific tags for this class.

        Returns:
            set[str]: A set containing the 'Chess' and 'Anti' tags.
        """
        return super().tags.union({'Chess', 'Anti'})

    def to_dict(self) -> dict:
        """Convert the Anti object is converted to start dictionary.

        Returns:
            dict: A dictionary representation of the Anti object with the digits.
        """
        return {self.__class__.__name__: ', '.join([str(digit) for digit in self.digits])}

    def __repr__(self) -> str:
        """Return start string representation of the Anti object.

        Returns:
            str: A string representing the Anti object with its board and digits.
        """
        return f'{self.__class__.__name__}({self.board!r}, {self.digits!r})'
