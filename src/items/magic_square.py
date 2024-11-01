from typing import List, Tuple, Dict

from src.glyphs.glyph import Glyph
from src.glyphs.rect_glyph import SquareGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.region import Region
from src.parsers.cell_parser import CellParser
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.direction import Direction
from src.utils.rule import Rule


class MagicSquare(Region):
    lines = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9],
        [3, 5, 7]
    ]


    def __init__(self, board: Board, center: Coord, corner: Coord):
        super().__init__(board)
        positions = [center + d * corner for d in Direction.all()]
        cells = [Cell.make(board, int(p.row), int(p.column)) for p in positions]
        self.add_items(cells)
        self.center_cell = cells[4]
        self.odd_cells = [cells[0], cells[2], cells[6], cells[8]]
        self.even_cells = [cells[1], cells[3], cells[5], cells[7]]
        self.center = center
        self.corner = corner
        self.strict = True
        self.unique = True

    @classmethod
    def is_sequence(cls) -> bool:
        """ Return True if this item is a sequence. """
        return True

    @classmethod
    def parser(cls) -> CellParser:
        return CellParser()

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"("
            f"{self.board!r}, "
            f"{self.center!r}, "
            f"{self.corner!r}"
            f")"
        )

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                'MagicSquare',
                1,
                "The purple box is a magic square with each three cell "
                "row, column and diagonal adding to the same number"
            )
        ]

    def glyphs(self) -> List[Glyph]:
        return [
            SquareGlyph('MagicSquare', cell.coord, 1)
            for cell in self.cells
        ]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'MagicSquare', 'Sum'})

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Tuple[Coord, Coord]:
        center, corner = yaml['MagicSquare'].split(', ')
        center = Coord(int(center[0]), int(center[1]))
        corner = Coord(int(corner[0]), int(corner[1]))
        return center, corner

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        center, corner = MagicSquare.extract(board, yaml)
        return cls(board, center, corner)

    def add_constraint(self, solver: PulpSolver) -> None:
        solver.model += solver.values[self.center.row][self.center.column] == 5, f"{self.__class__.__name__}_center"
        for i, line in enumerate(MagicSquare.lines):
            cell1 = self.cells[line[0] - 1]
            cell2 = self.cells[line[1] - 1]
            cell3 = self.cells[line[2] - 1]
            value1 = solver.values[cell1.row][cell1.column]
            value2 = solver.values[cell2.row][cell2.column]
            value3 = solver.values[cell3.row][cell3.column]
            solver.model += value1 + value2 + value3 == 15, f"{self.__class__.__name__}_{i}"
        # cells must be unique
        self.add_unique_constraint(solver, self.strict)
        # cells must sum to 45
        self.add_total_constraint(solver, 45)
        # orthogonal cells are even
        self.add_allowed_constraint(solver, [self.center_cell], [5])
        self.add_allowed_constraint(solver, self.odd_cells, [1, 3, 7, 9])
        self.add_allowed_constraint(solver, self.even_cells, [2, 4, 6, 8])

    def to_dict(self) -> Dict:
        return {
            self.__class__.__name__: f"{self.center.row}{self.center.column}, {self.corner.row}{self.corner.column}"
        }

    def css(self) -> Dict:
        return {
            '.MagicSquare': {
                'fill': 'mediumpurple'
            }
        }
