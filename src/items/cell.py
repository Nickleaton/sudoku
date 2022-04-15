from itertools import product
from typing import Optional, Dict, Tuple, List, Type, Set

from pulp import lpSum

from src.glyphs.glyph import Glyph, CellGlyph, KnownGlyph, EvenCellGlyph, OddCellGlyph, FortressCellGlyph
from src.items.board import Board
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.direction import Direction
from src.utils.rule import Rule


class Cell(Item):
    cache = {}

    def __init__(self, board: Board, row: int, column: int):
        super().__init__(board)
        self.row = row
        self.column = column

    @property
    def name(self) -> str:
        return f"{self.__class__.__name__}_{self.row}_{self.column})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.row!r}, {self.column!r})"

    def letter(self) -> str:
        return '.'

    @property
    def rules(self) -> List[Rule]:
        return []

    @staticmethod
    def cells() -> List['Cell']:
        return Cell.cache.values()

    @property
    def glyphs(self) -> List[Glyph]:
        return [CellGlyph('Cell', Coord(self.row, self.column))]

    @classmethod
    def make(cls, board: Board, row: int, column: int) -> 'Cell':
        key = (row, column)
        if key in Cell.cache:
            return Cell.cache[key]
        cell = Cell(board, row, column)
        Cell.cache[key] = cell
        return cell

    @classmethod
    def make_board(cls, board: Board):
        for row, column in product(board.row_range, board.column_range):
            Cell.make(board, row, column)

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        Item.check_yaml_dict(yaml)
        row = yaml['Row']
        column = yaml['Column']
        return cls(board, row, column)

    @property
    def valid(self) -> bool:
        return self.board.is_valid(self.row, self.column)

    @property
    def row_column(self) -> Tuple[int, int]:
        return self.row, self.column

    def __eq__(self, other: 'Cell') -> bool:
        return self.row == other.row and self.column == other.column

    def __lt__(self, other: 'Cell') -> bool:
        if self.row < other.row:
            return True
        if self.row == other.row:
            return self.column < other.column
        return False

    @property
    def coord(self) -> Coord:
        return Coord(self.row, self.column)

    def add_constraint(self, solver: PulpSolver) -> None:
        solver.model += lpSum(
            [
                solver.choices[digit][self.row][self.column]
                for digit in self.board.digit_range
            ]
        ) == 1


class CellReference(Item):

    def __init__(self, board: Board, row: int, column: int):
        super().__init__(board)
        self.cell = Cell.make(board, row, column)
        self.row = row
        self.column = column

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        Item.check_yaml_dict(yaml)
        row = yaml['Row']
        column = yaml['Column']
        return cls(board, row, column)

    def letter(self) -> str:
        return '.'  # pragma: no cover

    @property
    def rules(self) -> List[Rule]:
        return []

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.cell!r})"

    @property
    def used_classes(self) -> Set[Type['Item']]:
        result = super().used_classes
        result = result.union(self.cell.used_classes)
        return result


class Even(CellReference):

    @staticmethod
    def included(digit: int) -> bool:
        return digit % 2 == 0

    def letter(self) -> str:
        return 'e'

    def svg(self) -> Optional[Glyph]:
        return None

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Parity'})

    @property
    def rules(self) -> List[Rule]:
        return [Rule("Odd", 1, "An opaque grey square must contain an even digit")]

    @property
    def glyphs(self) -> List[Glyph]:
        return [EvenCellGlyph('EvenCell', Coord(self.row, self.column))]

    def add_constraint(self, solver: PulpSolver) -> None:
        solver.model += lpSum(
            [
                solver.choices[digit][self.row][self.column]
                for digit in self.board.digit_range
                if not Even.included(digit)
            ]
        ) == 0, f"{self.__class__.__name__}_{self.row}_{self.column}"


class Odd(CellReference):

    @staticmethod
    def included(digit: int) -> bool:
        return digit % 2 == 1

    def svg(self) -> Optional[Glyph]:
        return None

    def letter(self) -> str:
        return 'o'

    @property
    def rules(self) -> List[Rule]:
        return [Rule("Odd", 1, "An opaque grey circle must contain an odd digit")]

    @property
    def glyphs(self) -> List[Glyph]:
        return [OddCellGlyph('OddCell', Coord(self.row, self.column))]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Parity'})

    def add_constraint(self, solver: PulpSolver) -> None:
        solver.model += lpSum(
            [
                solver.choices[digit][self.row][self.column]
                for digit in self.board.digit_range
                if not Odd.included(digit)
            ]
        ) == 0, f"{self.__class__.__name__}_{self.row}_{self.column}"


class Fortress(CellReference):

    def svg(self) -> Optional[Glyph]:
        return None

    def letter(self) -> str:
        return 'f'

    @property
    def rules(self) -> List[Rule]:
        return [Rule("Odd", 1, "The digit in a fortress cell must be bigger than its orthogonal neighbours")]

    @property
    def glyphs(self) -> List[Glyph]:
        return [FortressCellGlyph('FortressCell', Coord(self.row, self.column))]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Comparison'})

    def add_constraint(self, solver: PulpSolver) -> None:
        cell = Coord(self.row, self.column)
        for offset in Direction.orthogonals():
            other = cell + offset
            if not self.board.is_valid_coordinate(other):
                continue
            solver.model += solver.values[self.row][self.column] >= solver.values[other.row][
                other.column] + 1, f"Fortress_{self.row}_{self.column}_{other.row}_{other.column}"


class Known(CellReference):

    def __init__(self, board: Board, row: int, column: int, digit: int):
        super().__init__(board, row, column)
        self.digit = int(digit)

    def add_constraint(self, solver: PulpSolver) -> None:
        solver.model += solver.choices[self.digit][self.row][self.column] == 1, \
                        f"Known_{self.row}_{self.column}_eq_{self.digit}"

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        Item.check_yaml_dict(yaml)
        row = yaml['Row']
        column = yaml['Column']
        digit = yaml['Digit']
        return cls(board, row, column, digit)

    def letter(self) -> str:
        return str(self.digit)

    @property
    def glyphs(self) -> List[Glyph]:
        return [KnownGlyph('Known', Coord(self.row, self.column), self.digit)]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.cell!r}, {self.digit!r})"
