"""AntiDiagonal."""

from itertools import product

from postponed.src.pulp_solver import PulpSolver
from pulp import lpSum

from postponed.src.items.diagonals import Diagonal
from src.items.boxes import Boxes
from src.utils.rule import Rule
from src.utils.sudoku_exception import SudokuError


class AntiDiagonal(Diagonal):
    """Represent an anti-diagonal constraint on start_location Sudoku board."""

    @property
    def rules(self) -> list[Rule]:
        """Provide the rule associated with the anti-diagonal constraint.

        Returns:
            list[Rule]: A list containing start_location rule that specifies the number of unique digits
                        on each marked main diagonal.
        """
        result: Item = self.top.find_instances(Boxes)[0]
        if not isinstance(result, Boxes):
            raise SudokuError("More than one boxes definition found")
        boxes: Boxes = result
        size: int = self.board.size.row % boxes.row_size
        return [
            Rule(
                'AntiDiagonal',
                1,
                f'Each marked main diagonal contains exactly {size} different digits',
            ),
        ]

    @property
    def tags(self) -> set[str]:
        """Provide the tags associated with the anti-diagonal constraint.

        Returns:
            set[str]: A set of tags, including 'Diagonal' and 'Uniqueness'.
        """
        return super().tags.union({'Diagonal', 'Uniqueness'})

    def add_constraint(self, solver: PulpSolver) -> None:
        """Enforce that the digit distribution is identical across marked diagonals in different boxes.

        Args:
            solver (PulpSolver): The solver to which the constraint is added.

        Example:
            For a 9x9 grid with 3x3 boxes, this method enforces that the sum of used digits on each diagonal
            in one box matches the corresponding sum in another box, maintaining anti-diagonal consistency.

        Raises:
            SudokuError: If there are more than one boxes definition in the board.
        """
        if not self.cells:
            return

        boxes: list[Boxes] = self.top.find_instances(Boxes)

        if len(boxes) != 1:
            raise SudokuError("More than one boxes definition found")
        box: Boxes = boxes[0]
        print(box)
        print()
        for cell_index, digit in product(range(self.count - 1), self.board.digits.digit_range):
            first = lpSum(
                solver.variables.choices[digit][self.cells[cell_index_in_box].row][self.cells[cell_index_in_box].column]
                for cell_index_in_box in range(cell_index * self.size, (cell_index + 1) * self.size)
            )
            second = lpSum(
                solver.variables.choices[digit][self.cells[cell_index_in_box].row][self.cells[cell_index_in_box].column]
                for cell_index_in_box in range((cell_index + 1) * self.size, (cell_index + 2) * self.size)
            )
            solver.model += first == second, f'{self.name}_{cell_index + 1}_{digit}'
