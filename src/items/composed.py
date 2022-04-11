from typing import List, Dict, Set, Type

from src.glyphs.glyph import Glyph
from src.items.board import Board
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class Composed(Item):

    def __init__(self, board: Board, items: List[Item]):
        super().__init__(board)
        self.items = items
        self._n = 0

    def add(self, item: Item):
        self.items.append(item)
        item.parent = self

    def add_items(self, items: List[Item]):
        for item in items:
            self.add(item)

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
            return result
        else:
            self._n = 0
            raise StopIteration

    def __len__(self) -> int:
        return len(self.items)

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict) -> Item:
        return cls(board, [])

    def __repr__(self):
        return f"{self.__class__.__name__}({self.board!r}, {self.items!r})"


class Constraints(Composed):

    def __init__(self, board: Board):
        super().__init__(board, [])
        self._n = 0

    @property
    def used_classes(self) -> Set[Type['Item']]:
        result = super().used_classes
        result = result.union({Constraints})
        return result

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict) -> Item:
        result = cls(board)
        for constraint in yaml:
            if isinstance(constraint, str):
                result.add(Item.create(constraint, board, constraint))
            else:
                for name, sub_constraint in constraint.items():
                    result.add(Item.create(name, board, sub_constraint))

        return result