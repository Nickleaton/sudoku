from typing import List, Tuple, Dict, Callable, Set, Type

from src.glyphs.glyph import Glyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class ClonedRegion(Item):

    def __init__(self, board, cells_a: List[Cell], cells_b: List[Cell]):
        super().__init__(board)
        assert len(cells_a) == len(cells_b)
        self.region_a: List[Cell] = cells_a
        self.region_b: List[Cell] = cells_b

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"{self.board!r}, "
            f"{repr(self.region_a)}, "
            f"{repr(self.region_b)}"
            f")"
        )

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Tuple[List[Cell], List[Cell]]:
        # Force string conversion because yaml might convert to int which you don't want when just one cell is cloned
        part_a = str(yaml[cls.__name__][0])
        part_b = str(yaml[cls.__name__][1])
        cells_a = [Cell.make(board, int(rc.strip()[0]), int(rc.strip()[1])) for rc in part_a.split(',')]
        cells_b = [Cell.make(board, int(rc.strip()[0]), int(rc.strip()[1])) for rc in part_b.split(',')]
        return cells_a, cells_b

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        cells_a, cells_b = ClonedRegion.extract(board, yaml)
        return ClonedRegion(board, cells_a, cells_b)

    def glyphs(self, selector: Callable[[Item], bool]) -> List[Glyph]:
        # TODO
        return []

    @property
    def used_classes(self) -> Set[Type['Item']]:
        result = super().used_classes
        for item in self.region_a:
            result = result.union(item.used_classes)
        for item in self.region_b:
            result = result.union(item.used_classes)
        return result


    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                "ClonedRegion",
                1,
                "The shaded areas are clones. They contain the same digits at the same locations."
            )
        ]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'ClonedRegion'})

    def add_constraint(self, solver: PulpSolver) -> None:
        for cell_1, cell_2 in zip(self.region_a, self.region_b):
            name = f"{self.__class__.__name__}_{cell_1.row}{cell_1.column}_{cell_2.row}{cell_2.column}"
            value_1 = solver.values[cell_1.row][cell_1.column]
            value_2 = solver.values[cell_2.row][cell_2.column]
            solver.model += value_1 == value_2, name

    def to_dict(self) -> Dict:
        cell_str_a = ",".join([f"{cell.row}{cell.column}" for cell in self.region_a])
        cell_str_b = ",".join([f"{cell.row}{cell.column}" for cell in self.region_b])
        return {self.__class__.__name__: f"{cell_str_a}={cell_str_b}"}

    def css(self) -> Dict:
        return {
            '.ClonedRegion': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 2,
                'fill': 'black'
            },
            '.ClonedRegionForeground': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 1,
                'fill': 'black'
            },
            '.ClonedRegionBackground': {
                'font-size': '30px',
                'stroke': 'white',
                'stroke-width': 8,
                'fill': 'white',
                'font-weight': 'bolder'
            }
        }
