import abc
from abc import ABC
from typing import Optional, List, Set, Type, Dict, Any

from src.glyphs.glyph import Glyph, ComposedGlyph
from src.items.board import Board
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


# YAML = TypeVar("YAML", Dict, List, str, int, None)


class Item(ABC):
    classes: Dict[str, 'Item'] = {}
    counter = 0

    def __init__(self, board: Board):
        super().__init__()
        self.board: Board = board
        self.parent: Optional[Item] = None
        self.identity: int = Item.counter
        Item.counter += 1

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Item.classes[cls.__name__] = cls

    def svg(self) -> Optional[Glyph]:  # pylint: disable=no-self-use
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
        return f"{self.__class__.__name__}_{self.identity}"

    @property
    def tags(self) -> set[str]:
        return set()

    @property
    def used_classes(self) -> Set[Type['Item']]:
        return set(self.__class__.__mro__).difference({abc.ABC, object})

    @classmethod
    def extract(cls, board: Board, yaml: Any) -> Any:  # pylint: disable=unused-argument
        return yaml

    @classmethod
    def create(cls, board: Board, yaml: Any) -> 'Item':
        if len(yaml) != 1:
            raise Exception
        name = list(yaml.keys())[0]
        clazz = cls.classes[name]
        return clazz.create(board, yaml)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({self.board!r})"

    def add_variables(self, board: Board, solver: PulpSolver) -> None:  # pylint: disable=unused-argument
        pass

    def add_constraint(self, solver: PulpSolver) -> None:  # pylint: disable=unused-argument
        pass
