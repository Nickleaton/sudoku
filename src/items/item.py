import abc
from abc import ABC
from typing import Optional, List, Set, Type

from src.glyphs.glyph import Glyph, ComposedGlyph
from src.items.board import Board
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class Item(ABC):
    classes = {}

    def __init__(self, board: Board):
        super().__init__()
        self.board = board
        self.parent = None
        self.identity = None

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Item.classes[cls.__name__] = cls

    @property
    def to_yaml(self) -> str:
        return f"{self.__class__.__name__}:"

    def svg(self) -> Optional[Glyph]:
        return None

    @property
    def rules(self) -> List[Rule]:
        return []

    @property
    def sorted_unique_rules(self) -> List[Rule]:
        return sorted(list(set(self.rules)))

    @property
    def glyphs(self) -> List[Glyph]:
        return []

    @property
    def sorted_glyphs(self) -> Glyph:
        return ComposedGlyph('Composed', sorted(self.glyphs))

    @property
    def name(self) -> str:
        return self.__class__.__name__

    @property
    def tags(self) -> set[str]:
        return set()

    @property
    def used_classes(self) -> Set[Type['Item']]:
        return {c for c in self.__class__.__mro__}.difference({abc.ABC, object})

    @classmethod
    def create(cls, name: str, board: Board, yaml: List) -> 'Item':
        return cls.classes[name].create(name, board, yaml)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({self.board!r})"

    def add_variables(self, board: Board, solver: PulpSolver) -> None:
        pass

    def add_constraint(self, solver: PulpSolver) -> None:
        print(f"Add constraint {self.__class__.__name__} - nowt")
