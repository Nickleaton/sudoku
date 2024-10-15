from typing import List, Dict, Callable

from src.glyphs.glyph import Glyph
from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.items.item import Item
from src.items.renban import Renban
from src.utils.rule import Rule


class DistinctRenban(Renban):

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                'DistinctRenban',
                1,
                "Pink lines must contain a set of consecutive, non-repeating digits, in any order,"
                "No two purple lines can contain exactly the same digits"
            )
        ]

    def glyphs(self) -> List[Glyph]:
        return [PolyLineGlyph('DistinctRenban', [cell.coord for cell in self.cells], False, False)]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'DistinctRenban', 'Renban', 'Adjacent', 'Set'})

    @staticmethod
    def power(digit: int):
        return 2 ** (digit - 1)

    @staticmethod
    def power_str(power: int):
        return "".join([str(i + 1) for i, c in enumerate(f"{power:b}"[::-1]) if c == '1'])

    @staticmethod
    def digits_to_str(digits: List[int]):
        return sum([DistinctRenban.power(digit) for digit in digits])

    # def add_constraint(self, solver: PulpSolver) -> None:
    # solver.renbans[self.name] = LpVariable(f"{self.name}", 1, int(10 ** self.board.maximum_digit), LpInteger)
    # solver.distinct_renbans.append(solver.renbans[self.name])
    # total = lpSum(
    #     [
    #         DistinctRenban.power(digit) * solver.choices[digit][cell.row][cell.column]
    #         for digit in self.board.digit_range
    #         for cell in self.cells
    #     ]
    # )
    # solver.model += solver.distinct_renbans[self.name] == total, self.name
    # for dr in solver.distinct_renbans:
    #     solver.model + not_equal(dr, solver.renbans[self.name])

    def css(self) -> Dict:
        return {
            '.DistinctRenban': {
                'stroke': 'purple',
                'stroke-width': 20,
                'stroke-linecap': 'round',
                'stroke-linejoin': 'round',
                'fill-opacity': 0
            }
        }
