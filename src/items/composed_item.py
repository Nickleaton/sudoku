from itertools import chain
from typing import List, Set, Type, Sequence, Dict, Callable

from src.glyphs.glyph import Glyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class ComposedItem(Item):

    def __init__(self, board: Board, items: Sequence[Item]):
        super().__init__(board)
        self.items: List[Item] = []
        self.add_items(items)
        self._n: int = 0

    def regions(self) -> Set['Item']:
        result: Set[Item] = {self}
        for item in self.items:
            result |= item.regions()
        return result

    def add(self, item: Item):
        self.items.append(item)
        item.parent = self

    def add_items(self, items: Sequence[Item]):
        for item in items:
            self.add(item)

    @property
    def cells(self) -> List[Cell]:
        return [item for item in self.items if isinstance(item, Cell)]

    @property
    def rules(self) -> List[Rule]:
        result = []
        for item in self.items:
            result.extend(item.rules)
        return result

    def flatten(self) -> List['Item']:
        result = [self]
        for item in self.items:
            result.extend(item.flatten())
        return result

    def glyphs(self) -> List[Glyph]:
        """
        Return a list of glyphs associated with this item.

        The glyphs are determined by recursively traversing the item tree and
        calling the `glyphs` method on each item.

        Returns:
            List[Glyph]: A list of glyphs associated with this item.
        """
        return list(chain.from_iterable(item.glyphs() for item in self.items))


    @property
    def tags(self) -> set[str]:
        result = super().tags
        for item in self.items:
            result = result.union(item.tags)
        return result

    @property
    def used_classes(self) -> Set[Type['Item']]:
        result = super().used_classes
        for item in self.items:
            result |= item.used_classes
        return result

    def add_constraint(self, solver: PulpSolver) -> None:
        for item in self.items:
            item.add_constraint(solver)

    def bookkeeping(self) -> None:
        for item in self.items:
            item.bookkeeping()

    def children(self) -> Set[Item]:
        result = {self}
        for item in self.items:
            result = result.union(item.children())
        return result

    def __iter__(self):
        self._n = 0
        return self

    def __next__(self) -> Item:
        if self._n < len(self.items):
            result = self.items[self._n]
            self._n += 1
        else:
            self._n = 0
            raise StopIteration
        return result

    def __len__(self) -> int:
        return len(self.items)

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        return cls(board, [])

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.items!r})"

    def to_dict(self) -> Dict:
        if len(self.items) == 0:
            return {self.__class__.__name__: None}
        return {self.__class__.__name__: [item.to_dict() for item in self.items]}

    def css(self) -> Dict:
        result = super().css()
        for item in self.items:
            result |= item.css()
        return result
