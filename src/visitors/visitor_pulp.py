from pulp import LpProblem, LpMinimize, LpVariable, LpInteger, lpSum, LpStatus, LpStatusOptimal

from src.items.item import Item
from src.items.anti import AntiKnight, AntiKing, Anti
from src.items.region_sets import Columns, Rows, Boxes, DisjointGroups
from src.items.knowns import Knowns
from src.items.board import Board
from src.items.little_killer import LittleKiller
from src.items.line import Line
from src.items.palindrome import Palindrome
from src.items.thermometer import Thermometer, SimpleThermometer, FrozenThermometer
from src.items.arrow import Arrow
from src.items.renban import Renban
from src.items.region import Region, StandardRegion, Column, Row, Box, DisjointGroup, Window
from src.items.diagonals import TLBR, BLTR
from src.items.solution import Solution
from src.items.pair import Pair
from src.items.greater_than_pair import GreaterThanPair
from src.items.different_pair import DifferentPair
from src.items.xi_pair import XIPair
from src.items.vi_pair import VIPair
from src.items.consecutive_pair import ConsecutivePair
from src.items.v_pair import VPair
from src.items.x_pair import XPair
from src.items.difference_pair import DifferencePair
from src.items.kropki import KropkiPair
from src.items.composed import Composed
from src.items.cell import Cell, Even, Odd, Fortress, Known
from src.visitors.visitor import Visitor


class PULPVisitor(Visitor):



    def __init__(self):
        self.objective = 0, "Objective"
        self.model = LpProblem("Sudoku", LpMinimize)
        self.status = 'Pending'
        self.choices = None
        self.values = None
        self.digit_range = None
        self.row_range = None
        self.column_range = None
        self.disjoint_group_range = None
        self.renbans = []
        self.solution = None

    def save(self, filename: str) -> None:
        self.model.writeLP(filename)

    def solve(self):
        self.model.solve()
        self.status = LpStatus[self.model.status]
        if self.model.status != LpStatusOptimal:
            return
        for row in self.row_range:
            for column in self.column_range:
                self.solution.set_value(row, column, self.values[row][column].varValue)

    def problem(self, problem: Board) -> None:
        self.digit_range = problem.digit_range
        self.row_range = problem.row_range
        self.column_range = problem.column_range
        self.disjoint_group_range = problem.disjoint_group_range
        self.choices = LpVariable.dicts("Choice",
                                        (problem.digit_range, problem.row_range, problem.column_range),
                                        0,
                                        1,
                                        LpInteger
                                        )
        self.values = LpVariable.dicts("Values",
                                       (problem.row_range, problem.column_range),
                                       1,
                                       problem.maximum_digit,
                                       LpInteger
                                       )
        self.solution = Solution(problem)

    def columns(self, item: Columns) -> None:
        pass

    def rows(self, item: Rows) -> None:
        pass

    def boxes(self, item: Boxes) -> None:
        pass

    def row(self, item: Row) -> None:
        for digit in self.digit_range:
            total = lpSum([self.choices[digit][cell.row][cell.column] for cell in item])
            self.model += total == 1, f"Unique_row_{item.index}_value_{digit}"

    def column(self, item: Column) -> None:
        # Unique values
        for digit in self.digit_range:
            total = lpSum([self.choices[digit][cell.row][cell.column] for cell in item])
            self.model += total == 1, f"Unique_column_{item.index}_value_{digit}"

    def box(self, item: Box) -> None:
        # Unique values
        for digit in self.digit_range:
            total = lpSum([self.choices[digit][cell.row][cell.column] for cell in item])
            self.model += total == 1, f"Unique_box_{item.index}_value_{digit}"

    def disjoint_group(self, item: DisjointGroup) -> None:
        # Unique values
        for digit in self.digit_range:
            total = lpSum([self.choices[digit][cell.row][cell.column] for cell in item])
            self.model += total == 1, f"Unique_disjoint_group_{item.index}_value_{digit}"

    def disjoint_groups(self, item: DisjointGroups) -> None:
        pass

    def knowns(self, item: Knowns) -> None:
        pass

    def cell(self, item: Cell) -> None:
        if not isinstance(item.parent, Board):
            return
        # only one digit in each cell
        total = lpSum([self.choices[digit][item.row][item.column] for digit in self.digit_range])
        self.model += total == 1, f"Unique_in_cell_{item.row}_{item.column}"

        # Value in each cell
        total = lpSum([digit * self.choices[digit][item.row][item.column] for digit in self.digit_range])
        self.model += total == self.values[item.row][item.column], f"Value_{item.row}_{item.column}"

    def even(self, item: Even) -> None:
        for digit in self.digit_range:
            name = f"Even_{item.row}_{item.column}_{digit}"
            if not item.included(digit):
                self.model += self.choices[digit][item.row][item.column] == 0, name

    def odd(self, item: Odd) -> None:
        for digit in self.digit_range:
            name = f"Odd_{item.row}_{item.column}_{digit}"
            if not item.included(digit):
                self.model += self.choices[digit][item.row][item.column] == 0, name

    def known(self, item: Known) -> None:
        for digit in self.digit_range:
            name = f"Known_{item.row}_{item.column}_{digit}"
            if digit == item.digit:
                self.model += self.choices[digit][item.row][item.column] == 1, name
            else:
                self.model += self.choices[digit][item.row][item.column] == 0, name

    def anti_knight(self, item: AntiKnight) -> None:
        pass

    def different_pair(self, item: DifferentPair) -> None:
        1 / 0

    def tlbr(self, item: TLBR) -> None:
        for digit in self.digit_range:
            total = lpSum([self.choices[digit][cell.row][cell.column] for cell in item])
            self.model += total == 1, f"Unique_tlbr_value_{digit}"

    def bltr(self, item: BLTR) -> None:
        for digit in self.digit_range:
            total = lpSum([self.choices[digit][cell.row][cell.column] for cell in item])
            self.model += total == 1, f"Unique_bltr_value_{digit}"

    def fortress(self, item: Fortress) -> None:
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            row = item.row + y
            column = item.column + x
            if not Cell.is_valid(row, column):
                continue
            name = f"Fortress_{item.row}_{item.column}_gt_{row}_{column}"
            # Note. The values can never be equal because of row and column constraints.
            self.model += self.values[item.row][item.column] >= self.values[row][column], name

    def little_killer(self, item: LittleKiller) -> None:
        total = lpSum([self.values[cell.row][cell.column] for cell in item])
        self.model += total == item.total, f"Little_Killer_{item.side.value}{item.offset}"

    def simple_thermo(self, item: SimpleThermometer) -> None:
        for i in range(0, len(item.items) - 1):
            c1 = item.items[i]
            c2 = item.items[i + 1]
            name = f"Simple_Thermo_{c1.row}_{c1.column}_{c2.row}_{c2.column}"
            self.model += self.values[c1.row][c1.column] + 1 - self.values[c2.row][c2.column] <= 0, name

    def frozen_thermo(self, item: FrozenThermometer) -> None:
        for i in range(0, len(item.items) - 1):
            c1 = item.items[i]
            c2 = item.items[i + 1]
            name = f"Simple_Thermo_{c1.row}_{c1.column}_{c2.row}_{c2.column}"
            self.model += self.values[c1.row][c1.column] <= self.values[c2.row][c2.column], name

    def arrow(self, item: Arrow) -> None:
        total = lpSum([self.values[item.items[i].row][item.items[i].column] for i in range(1, (len(item.items)))])
        name = f"Arrow_{item.items[0].row}_{item.items[0].column}"
        self.model += self.values[item.items[0].row][item.items[0].column] == total, name

    def renban(self, item: Renban) -> None:
        i = len(self.renbans) + 1
        lower_name = f"Renban_Lower_{i}"
        upper_name = f"Renban_Upper_{i}"
        lower = LpVariable(lower_name,  # TODO
                           lowBound=-9,
                           upBound=9,
                           cat=LpInteger)
        upper = LpVariable(upper_name,
                           lowBound=-9,
                           upBound=9,
                           cat=LpInteger)
        self.renbans.append([lower, upper])
        for cell in item.items:
            self.model += lower <= self.values[cell.row][cell.column]
            self.model += upper >= self.values[cell.row][cell.column]
        self.model += upper - lower == len(item.items) - 1

        # Plus unique on the line. A digit doesn't have to appear.
        for digit in self.digit_range:
            total = lpSum([self.choices[digit][cell.row][cell.column] for cell in item.items])
            self.model += total <= 1, f"Unique_renban_value_{i}_{digit}"

    # def s159(self, item: S159) -> None:
    #     for column in item.column_set:
    #         for row in self.row_range:
    #             for d in self.digit_range:
    #                 self.model += self.choices[d][row][column] == self.choices[column][row][d]

    def palindrome(self, item: Palindrome) -> None:
        l = len(item.items)
        m = int(l / 2)
        for i in range(0, m):
            a = item.items[i]
            b = item.items[l - i - 1]
            name = f"Palindrome_{a.row}_{a.column}__{b.row}_{b.column}"
            self.model += self.values[a.row][a.column] == self.values[b.row][b.column], name

    def window(self, item: Window) -> None:
        # Plus unique on the window
        for digit in self.digit_range:
            total = lpSum([self.choices[digit][cell.row][cell.column] for cell in item.items])
            self.model += total == 1, f"Unique_window_value_{item.index}_{digit}"

    def region(self, item: Region) -> None:
        pass

    def composed(self, item: Composed) -> None:
        pass

    def thermo(self, item: Thermometer) -> None:
        pass

    def pair(self, item: Pair) -> None:
        pass

    def difference_pair(self, item: DifferencePair) -> None:
        pass

    def line(self, item: Line) -> None:
        pass

    def greater_than_pair(self, item: GreaterThanPair) -> None:
        pass

    def anti(self, item: Anti) -> None:
        pass

    def anti_king(self, item: AntiKing) -> None:
        pass

    def kropki_pair(self, item: KropkiPair) -> None:
        pass

    def x_pair(self, item: XPair) -> None:
        pass

    def xi_pair(self, item: XIPair) -> None:
        pass

    def v_pair(self, item: VPair) -> None:
        pass

    def vi_pair(self, item: VIPair) -> None:
        pass

    def consecutive_pair(self, item: ConsecutivePair) -> None:
        pass

    def item(self, item: Item) -> None:
        pass

    def standard_region(self, item: StandardRegion) -> None:
        pass
