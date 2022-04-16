import abc
from abc import ABC
from typing import Optional, List, Set, Type, Dict, Any

from src.glyphs.glyph import Glyph, ComposedGlyph
from src.items.board import Board
from src.items.constraint_exception import ConstraintException
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class Item(ABC):
    classes: Dict[str, 'Item'] = {}

    def __init__(self, board: Board):
        super().__init__()
        self.board: Board = board
        self.parent: Optional[Item] = None
        self.identity: Optional[int] = None

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Item.classes[cls.__name__] = cls

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
        return set(self.__class__.__mro__).difference({abc.ABC, object})

    @staticmethod
    def check_yaml_dict(yaml: Dict | List | str | int | None):
        if not isinstance(yaml, dict):
            raise ConstraintException(f"Expecting Dict, got {yaml!r}")

    @staticmethod
    def check_yaml_list(yaml: Dict | List | str | int | None):
        if not isinstance(yaml, list):
            raise ConstraintException(f"Expecting List, got {yaml!r}")

    @staticmethod
    def check_yaml_str(yaml: Dict | List | str | int | None):
        if not isinstance(yaml, str):
            raise ConstraintException(f"Expecting str, got {yaml!r}")

    @staticmethod
    def check_yaml_int(yaml: Dict | List | str | int | None):
        if not isinstance(yaml, int):
            raise ConstraintException(f"Expecting int, got {yaml!r}")

    @staticmethod
    def check_yaml_none(yaml: Dict | List | str | int | None):
        if yaml is not None:
            raise ConstraintException(f"Expecting None, got {yaml!r}")

    @staticmethod
    def validate(board: Board, yaml: Any) -> List[str]:
        return []

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> 'Item':
        return cls.classes[name].create(name, board, yaml)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({self.board!r})"

    def add_variables(self, board: Board, solver: PulpSolver) -> None:
        pass

    def add_constraint(self, solver: PulpSolver) -> None:
        print(f"Add Constraint {solver.__class__.__name__}")
