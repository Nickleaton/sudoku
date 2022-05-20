import re
from typing import Optional, List, Dict

from src.glyphs.glyph import Glyph, FortressCellGlyph
from src.items.cell_reference import CellReference
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.direction import Direction
from src.utils.rule import Rule


class FortressCell(CellReference):

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

    def add_constraint(self, solver: PulpSolver, include: re.Pattern, exclude: re.Pattern) -> None:
        cell = Coord(self.row, self.column)
        for offset in Direction.orthogonals():
            other = cell + offset
            if not self.board.is_valid_coordinate(other):
                continue
            solver.model += solver.values[self.row][self.column] >= solver.values[other.row][
                other.column] + 1, f"Fortress_{self.row}_{self.column}_{other.row}_{other.column}"

    def css(self) -> Dict:
        return {
            ".FortressCell": {
                "stroke": "black",
                "stroke-width": 3
            }
        }
