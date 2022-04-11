from typing import Optional, List

from src.glyphs.glyph import Glyph, ThermometerGlyph, SimpleThermometerGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.line import Line
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class Thermometer(Line):

    def __init__(self, board: Board, cells: Optional[List[Cell]]):
        super().__init__(board, cells)

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Thermometer', 'Comparison'})


class SimpleThermometer(Thermometer):

    @property
    def rules(self) -> List[Rule]:
        return [Rule('SimpleThermometer', 1, "Cells along a line with a bulb strictly increase from the bulb end")]

    @property
    def glyphs(self) -> List[Glyph]:
        return [
            SimpleThermometerGlyph('SimpleThermometer', [cell.coord for cell in self.cells])
        ]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Simple Thermometer'})

    def add_constraint(self, solver: PulpSolver) -> None:
        for i in range(1, len(self)):
            c1 = self.cells[i - 1]
            c2 = self.cells[i]

            c1_value = solver.values[c1.row][c1.column]
            c2_value = solver.values[c2.row][c2.column]
            name = f"{self.__class__.__name__}_rank_{c1.row}_{c1.column}_{c2.row}_{c2.column}"
            solver.model += c1_value + 1 <= c2_value, name

            name = f"{self.__class__.__name__}_lbound_{c2.row}_{c2.column}"
            solver.model += c2_value >= i + 1, name
            # TODO Digit excludes

            name = f"{self.__class__.__name__}_ubound_{c2.row}_{c2.column}"
            solver.model += c2_value <= self.board.maximum_digit - len(self) + i + 1, name
            # TODO Digit excludes

        c2 = self.cells[0]
        c2_value = solver.values[c2.row][c2.column]
        name = f"{self.__class__.__name__}_lbound_{c2.row}_{c2.column}"
        solver.model += c2_value >= 0 + 1, name

        name = f"{self.__class__.__name__}_ubound_{c2.row}_{c2.column}"
        solver.model += c2_value <= self.board.maximum_digit - len(self) + 0 + 1, name
        # TODO Digit excludes


class FrozenThermometer(Thermometer):

    @property
    def rules(self) -> List[Rule]:
        return [Rule('FrozenThermo', 1, "Cells along a line with a bulb increase or stay the same from the bulb end")]

    @property
    def glyphs(self) -> List[Glyph]:
        return [
            ThermometerGlyph('FrozenThermometer', [cell.coord for cell in self.cells])
        ]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Frozen Thermometer'})

    def add_constraint(self, solver: PulpSolver) -> None:
        for i in range(1, len(self)):
            c1 = self.cells[i - 1]
            c2 = self.cells[i]

            name = f"{self.__class__.__name__}_rank_{c1.row}_{c1.column}_{c2.row}_{c2.column}"
            solver.model += solver.values[c1.row][c1.column] <= solver.values[c2.row][c2.column], name
