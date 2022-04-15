from typing import Dict, List

from pulp import lpSum

from src.glyphs.glyph import Glyph, BoxGlyph, SquareGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.rule import Rule

REGION_TOTALS = False


class Region(Composed):
    """ Collection of cells"""

    def __init__(self, board: Board) -> None:
        super().__init__(board, [])

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        Item.check_yaml_none(yaml)
        return cls(board)

    @property
    def cells(self) -> List[Cell]:
        return [item for item in self.items if isinstance(item, Cell)]

    def __in__(self, cell: Cell) -> bool:
        return cell in self.cells

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r})"

    def add_unique_constraint(self, solver: PulpSolver, name, optional: bool = False):
        for digit in self.board.digit_range:
            total = lpSum([solver.choices[digit][cell.row][cell.column] for cell in self.cells])
            if optional:
                solver.model += total <= 1, f"Unique_{name}_{digit}"
            else:
                solver.model += total == 1, f"Unique_{name}_{digit}"

    def add_total_constraint(self, solver: PulpSolver, total: int, name: str) -> None:
        if REGION_TOTALS:
            value = lpSum([solver.values[cell.row][cell.column] for cell in self.cells])
            solver.model += value == total, f"Total_{name}"


class StandardRegion(Region):

    def __init__(self, board: Board, index: int):
        super().__init__(board)
        self.index = index

    @property
    def name(self) -> str:
        return f"{self.__class__.__name__}_{self.index}"

    @property
    def glyphs(self) -> List[Glyph]:
        return []

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        Item.check_yaml_int(yaml)
        return cls(board, yaml)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.index!r}, [])"

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Uniqueness', 'Standard Set'})


class Column(StandardRegion):

    def __init__(self, board: Board, index: int):
        super().__init__(board, index)
        cells = [Cell.make(board, row, index) for row in board.column_range]
        self.add_items(cells)

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        Item.check_yaml_int(yaml)
        return cls(board, yaml)

    @property
    def glyphs(self) -> List[Glyph]:
        return []

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.index!r})"

    @property
    def rules(self) -> List[Rule]:
        return [Rule('Column', 1, 'Digits in each column must be unique')]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Column'})

    def add_constraint(self, solver: PulpSolver) -> None:
        self.add_total_constraint(solver, solver.board.digit_sum, self.name)
        self.add_unique_constraint(solver, f"Column_{self.index!r}")


class Row(StandardRegion):

    def __init__(self, board: Board, index: int):
        super().__init__(board, index)
        cells = [Cell.make(board, index, row) for row in board.row_range]
        self.add_items(cells)

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        Item.check_yaml_int(yaml)
        return cls(board, yaml)

    @property
    def glyphs(self) -> List[Glyph]:
        result = []
        for item in self.items:
            result.extend(item.glyphs)
        return result

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.index!r})"

    @property
    def rules(self) -> List[Rule]:
        return [Rule('Row', 1, 'Digits in each row must be unique')]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Row'})

    def add_constraint(self, solver: PulpSolver) -> None:
        self.add_total_constraint(solver, solver.board.digit_sum, self.name)
        self.add_unique_constraint(solver, f"Row_{self.index!r}")


class Box(StandardRegion):

    def __init__(self, board: Board, index: int):
        super().__init__(board, index)
        self.position = self.start()
        cells = [
            Cell.make(board, self.position.row + ro - 1, self.position.column + co - 1)
            for ro in range(1, board.box_rows + 1)
            for co in range(1, board.box_columns + 1)
        ]
        self.add_items(cells)

    def start(self) -> Coord:
        r = ((self.index - 1) * self.board.box_rows) % self.board.maximum_digit + 1
        c = ((self.index - 1) // self.board.box_columns) * self.board.box_columns + 1
        return Coord(r, c)

    @property
    def size(self) -> Coord:
        return Coord(self.board.box_rows, self.board.box_columns)

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        Item.check_yaml_int(yaml)
        return cls(board, yaml)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.index!r})"

    @property
    def rules(self) -> List[Rule]:
        return [Rule('Box', 1, 'Digits in each box must be unique')]

    @property
    def glyphs(self) -> List[Glyph]:
        return [BoxGlyph('Box', self.position, self.size)]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Box'})

    def add_constraint(self, solver: PulpSolver) -> None:
        self.add_total_constraint(solver, solver.board.digit_sum, self.name)
        self.add_unique_constraint(solver, f"Box_{self.index!r}")


class DisjointGroup(StandardRegion):
    offsets = [
        (0, 0),
        (0, 3),
        (0, 6),
        (3, 0),
        (3, 3),
        (3, 6),
        (6, 0),
        (6, 3),
        (6, 6)
    ]

    def __init__(self, board: Board, index: int):
        r = (index - 1) // 3 + 1  # TODO
        c = (index - 1) % 3 + 1
        super().__init__(board, index)
        cells = [Cell.make(board, r + ro, c + co) for ro, co in DisjointGroup.offsets]
        self.add_items(cells)

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        Item.check_yaml_int(yaml)
        return cls(board, yaml)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.index!r})"

    @property
    def rules(self) -> List[Rule]:
        return [Rule('DisjointGroup', 1, 'Digits in same place each box must be unique')]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Disjoint Group'})

    def add_constraint(self, solver: PulpSolver) -> None:
        self.add_total_constraint(solver, solver.board.digit_sum, self.name)
        self.add_unique_constraint(solver, f"DisjointGroup_{self.index}")


class Window(Region):
    offsets = [
        Coord(-1, -1),
        Coord(-1, 0),
        Coord(-1, 1),
        Coord(0, -1),
        Coord(0, 0),
        Coord(0, 1),
        Coord(1, -1),
        Coord(1, 0),
        Coord(1, 1)
    ]

    def __init__(self, board: Board, center: Coord):
        super().__init__(board)
        self.center = center
        cells = [Cell.make(board, (center + offset).row, (center + offset).column) for offset in Window.offsets]
        self.add_items(cells)

    @property
    def name(self) -> str:
        return f"{self.__class__.__name__}_{self.center.row}_{self.center.column}"

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        Item.check_yaml_str(yaml)
        row = int(yaml.split(',')[0])
        column = int(yaml.split(',')[1])
        coord = Coord(row, column)
        return cls(board, coord)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.center!r})"

    @property
    def rules(self) -> List[Rule]:
        return [Rule('Window', 1, 'Digits in same shaded window must be unique')]

    @property
    def glyphs(self) -> List[Glyph]:
        return [SquareGlyph('Window', self.center - Coord(1, 1), 3)]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Window'})

    def add_constraint(self, solver: PulpSolver) -> None:
        self.add_total_constraint(solver, solver.board.digit_sum, self.name)
        self.add_unique_constraint(solver, f"Window_{self.center.row}_{self.center.column}")
