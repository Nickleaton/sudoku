from typing import List, Set, Type, Sequence, Dict

from src.glyphs.glyph import Glyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class Composed(Item):

    def __init__(self, board: Board, items: Sequence[Item]):
        super().__init__(board)
        self.items: List[Item] = list(items)
        self._n: int = 0

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

    @property
    def glyphs(self) -> List[Glyph]:
        result = []
        for item in self.items:
            result += item.glyphs
        return result

    @property
    def tags(self) -> set[str]:
        result = super().tags
        for item in self.items:
            result = result.union(item.tags)
        return result

    @property
    def used_classes(self) -> Set[Type['Item']]:
        result = super().used_classes
        result = result.union({Composed})
        for item in self.items:
            result = result.union(item.used_classes)
        return result

    def add_variables(self, board: Board, solver: PulpSolver) -> None:
        for item in self.items:
            item.add_variables(board, solver)

    def add_constraint(self, solver: PulpSolver) -> None:
        for item in self.items:
            item.add_constraint(solver)

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

    def css(self) -> str:
        return "\n".join([item.css() for item in self.items])

    def css2(self):
        result = super().css2()
        for item in self.items:
            result |= item.css2()
        return result
