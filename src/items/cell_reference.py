from typing import List, Set, Tuple, Optional, Dict, Type, Iterator

from src.glyphs.glyph import Glyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.utils.rule import Rule


class CellReference(Item):

    def __init__(self, board: Board, row: int, column: int):
        super().__init__(board)
        self.cell = Cell.make(board, row, column)
        self.row = row
        self.column = column

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Tuple:
        data = yaml[cls.__name__]
        data = str(data)
        return int(data[0]), int(data[1])

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        row, column = cls.extract(board, yaml)
        return cls(board, row, column)

    def svg(self) -> Optional[Glyph]:
        return None

    def letter(self) -> str:  # pylint: disable=no-self-use
        return '.'

    def flatten(self) -> List[Item]:
        return [self, self.cell]

    @property
    def rules(self) -> List[Rule]:
        return []

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.cell!r})"

    @property
    def used_classes(self) -> Set[Type['Item']]:
        """
        Return a set of classes that this item uses.

        The set of classes is determined by traversing the method resolution
        order (MRO) of the item's class. The set contains all classes in the
        MRO, except for the abstract base class (`abc.ABC`) and the `object`
        class.

        Returns:
            Set[Type[Self]]: A set of classes that this item uses.
        """
        return super().used_classes | self.cell.used_classes

    def walk(self) -> Iterator[Item]:
        """
        Yield each item in the tree of items rooted at the current item.

        The generator yields the current item, then recursively yields each item
        in the tree rooted at the current item. The order of the items is
        unspecified.

        Yields:
            Item: The current item, followed by each item in the tree rooted at
                the current item.
        """
        yield self
        yield self.cell

    def to_dict(self) -> Dict:
        return {self.__class__.__name__: int(self.cell.row_column_string)}

    def children(self) -> Set[Item]:
        return {self, self.cell}
