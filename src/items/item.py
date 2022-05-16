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

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Item.classes[cls.__name__] = cls

    def __init__(self, board: Board):
        super().__init__()
        self.board: Board = board
        self.parent: Optional[Item] = None
        self.identity: int = Item.counter
        Item.counter += 1

    @property
    def top(self) -> 'Item':
        if self.parent is None:
            return self
        return self.parent.top

    def regions(self) -> Set['Item']:
        return {self}

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
        return f"{self.__class__.__name__}_{self.identity}"

    @property
    def tags(self) -> set[str]:
        return set()

    @property
    def used_classes(self) -> Set[Type['Item']]:
        return set(self.__class__.__mro__).difference({abc.ABC, object})

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Any:  # pylint: disable=unused-argument
        return yaml

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> 'Item':
        if len(yaml) != 1:
            raise Exception
        name = list(yaml.keys())[0]
        clazz = cls.classes[name]
        return clazz.create(board, yaml)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(({self.board!r})"

    def add_constraint(self, solver: PulpSolver) -> None:  # pylint: disable=unused-argument
        pass

    def bookkeeping(self) -> None:
        pass

    def to_dict(self) -> Dict:
        return {self.__class__.__name__: None}

    def css(self) -> Dict:
        return {
            '.TextGlyphForeground': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 8,
                'fill': 'black',
                'font-weight': 'bolder'
            },
            '.TextGlyphBackground': {
                'font-size': '30px',
                'stroke': 'white',
                'stroke-width': 8,
                'fill': 'white',
                'font-weight': 'bolder'
            },
            'LittleNumber': {
                'font-size': '20px',
                'stroke': 'black',
            }
        }

    @staticmethod
    def css_text(data: Dict, indent: int = 0) -> str:
        tab = '    '
        result = ""
        for k in sorted(data.keys()):
            v = data[k]
            if isinstance(v, dict):
                result += f"{tab * indent}{k} {{\n"
                result += Item.css_text(v, indent + 1)
                result += f"{tab * indent}}}\n\n"
            else:
                result += f"{tab * indent}{k}: {v};\n"
        return result
