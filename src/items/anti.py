from typing import List, Sequence, Any, Dict

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.difference_pair import DifferencePair
from src.items.item import Item
from src.utils.coord import Coord


class Anti(ComposedItem):
    """Represents an 'Anti' composed item in the board game, which is inherited from ComposedItem.

    This class is used to define constraints between pairs of cells based on the
    provided digits and their positions on the board.

    Attributes:
        digits: A list of integers representing the digits involved in the 'Anti' constraint.
    """

    def __init__(self, board: Board, digits: List[int]):
        """Initialize the Anti object with a board and digits.

        Args:
            board (Board): The board where the Anti constraint will be applied.
            digits (List[int]): A list of digits for the Anti constraint.

        The constructor iterates through all the cells on the board and generates
        pairs of cells with the given digits.
        """
        super().__init__(board, [])
        self.digits = digits
        for cell in Cell.cells():
            pairs = self.pairs(cell, digits)
            self.add_items(pairs)

    def offsets(self) -> List[Coord]:
        """Return a list of offsets for the Anti constraint.

        This method can be overridden in subclasses to provide specific offsets
        for the Anti constraint.

        Returns:
            List[Coord]: An empty list as the default for offsets.
        """
        return []

    def pairs(self, c1: Cell, digits: List[int]) -> Sequence[DifferencePair]:
        """Pairs of cells are generated based on the provided digits and offsets.

        Args:
            c1 (Cell): The first cell to consider.
            digits (List[int]): The list of digits for which the pairs are generated.

        Returns:
            Sequence[DifferencePair]: A sequence of DifferencePair objects representing
            the valid pairs between cells c1 and other cells on the board.
        """
        result = []
        for offset in self.offsets():
            if not self.board.is_valid(int(c1.row + offset.row), int(c1.column + offset.column)):
                continue
            c2 = Cell.make(self.board, int(c1.row + offset.row), int(c1.column + offset.column))
            result.append(DifferencePair(self.board, c1, c2, digits))
        return result

    @property
    def tags(self) -> set[str]:
        """A set of tags associated with the Anti constraint is returned.

        The tags of the parent class are combined with the specific tags for this class.

        Returns:
            set[str]: A set containing the 'Chess' and 'Anti' tags.
        """
        return super().tags.union({'Chess', 'Anti'})

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Any:
        """Extract a list of digits from the YAML configuration.

        Args:
            cls (type): The class that calls this method (used for extracting class-level data).
            board (Board): The board object (not used in this method but required for interface).
            yaml (Dict): The YAML configuration dictionary from which the digits are extracted.

        Returns:
            Any: A list of integers representing the digits extracted from the YAML.
        """
        return [int(part) for part in str(yaml[cls.__name__]).split(', ')]

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        """Create an object from the given YAML.

        Args:
            cls (type): The class that calls this method (used for creating an instance of the class).
            board (Board): The board object where the Anti constraint will be applied.
            yaml (Dict): The YAML configuration dictionary containing the digits.

        Returns:
            Item: An instance of the Anti class with the parsed digits.
        """
        lst = cls.extract(board, yaml)
        return cls(board, lst)

    def __repr__(self) -> str:
        """Return a string representation of the Anti object.

        Returns:
            str: A string representing the Anti object with its board and digits.
        """
        return f"{self.__class__.__name__}({self.board!r}, {self.digits!r})"

    def to_dict(self) -> Dict:
        """Convert the Anti object is converted to a dictionary.

        Returns:
            Dict: A dictionary representation of the Anti object with the digits.
        """
        return {self.__class__.__name__: ", ".join([str(d) for d in self.digits])}
