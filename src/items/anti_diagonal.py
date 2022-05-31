import re
from typing import List, Optional

from pulp import lpSum

from src.items.board import Board
from src.items.diagonals import Diagonal
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class AntiDiagonal(Diagonal):

    def __init__(self, board: Board):
        assert board.box_rows == board.box_columns
        assert board.board_rows == board.board_rows
        assert board.board_rows % board.box_rows == 0
        super().__init__(board)
        self.size = board.box_rows
        self.count = board.board_rows // board.box_rows

    @property
    def rules(self) -> List[Rule]:
        return [Rule('AntiDiagonal', 1, f"Each marked main diagonal contains exactly {self.size} different digits")]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Diagonal', 'Uniqueness'})

    def add_constraint(self, solver: PulpSolver, include: Optional[re.Pattern], exclude: Optional[re.Pattern]) -> None:
        # example. In a 9x9 with 3x3 boxes
        # In box 1 we add up the number of used digits for each digit on the diagonal.
        # In box 5 we add up the number of used digits for each digit on the diagonal.
        # The sums must be the same
        # So if the diagonal in box one is 1,2,3 Then the total for digit 1 is 1, same for 2, 3, The others are 0
        # Same applies to box 5. By equating the sums, we enforce the constraint.
        if len(self.cells) == 0:
            return
        for b in range(0, self.count - 1):
            for digit in self.board.digit_range:
                first = lpSum(
                    solver.choices[digit][self.cells[x].row][self.cells[x].column]
                    for x in range(b * self.size, (b + 1) * self.size)
                )
                second = lpSum(
                    solver.choices[digit][self.cells[x].row][self.cells[x].column]
                    for x in range((b + 1) * self.size, (b + 2) * self.size)
                )
                solver.model += first == second, f"{self.name}_{b + 1}_{digit}"
