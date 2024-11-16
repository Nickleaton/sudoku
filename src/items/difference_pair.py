"""DifferencePair."""
from typing import List, Tuple, Dict

from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.pair import Pair
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class DifferencePair(Pair):
    """Represents a pair of cells that have specified differences in their values."""

    def __init__(self, board: Board, cell_1: Cell, cell_2: Cell, digits: List[int]):
        """Initialize a DifferencePair.

        Args:
            board (Board): The Sudoku board instance.
            cell_1 (Cell): The first cell in the pair.
            cell_2 (Cell): The second cell in the pair.
            digits (List[int]): A list of digits representing the allowed differences between the cell values.
        """
        super().__init__(board, cell_1, cell_2)
        self.digits = digits

    def __repr__(self) -> str:
        """Return a string representation of the DifferencePair.

        Returns:
            str: A string representation of the DifferencePair.
        """
        return f"{self.__class__.__name__}({self.board!r}, {self.cell_1!r}, {self.cell_2!r}, {self.digits!r})"

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Tuple[Cell, Cell, List[int]]:
        """Extract cells and their allowed difference values from YAML data.

        Args:
            board (Board): The board instance for cell creation.
            yaml (Dict): The YAML data containing the cell pair and their difference values.

        Returns:
            Tuple[Cell, Cell, List[int]]: A tuple containing two cells and a list of allowed difference values.
        """
        cell_string, difference_string = yaml[cls.__name__].split("=")
        cell_string_1, cell_string_2 = cell_string.split("-")
        cell_1 = Cell.make(board, int(cell_string_1[0]), int(cell_string_1[1]))
        cell_2 = Cell.make(board, int(cell_string_2[0]), int(cell_string_2[1]))
        digits = [int(d) for d in difference_string.split(",")]
        return cell_1, cell_2, digits

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        """Create a DifferencePair instance from YAML data.

        Args:
            board (Board): The board instance.
            yaml (Dict): The YAML data containing the cell pair and allowed differences.

        Returns:
            Item: An instance of DifferencePair.
        """
        cell_1, cell_2, digits = cls.extract(board, yaml)
        return cls(board, cell_1, cell_2, digits)

    @property
    def rules(self) -> List[Rule]:
        """Retrieve the rules for the difference pair.

        Returns:
            List[Rule]: A list of rules, which is empty for this class.
        """
        return []

    @property
    def tags(self) -> set[str]:
        """Retrieve the tags for the difference pair.

        Returns:
            set[str]: A set of tags, including 'Different'.
        """
        return super().tags.union({'Different'})


    def add_constraint(self, solver: PulpSolver) -> None:
        """Add constraints to the solver for the difference pair.

        Args:
            solver (PulpSolver): The solver to add constraints to.
        """
        for digit in self.digits:
            name = (
                f"{self.__class__.__name__}"
                f"_"
                f"{digit}"
                f"_"
                f"{self.cell_1.row}"
                f"_"
                f"{self.cell_1.column}"
                f"_"
                f"{self.cell_2.row}"
                f"_"
                f"{self.cell_2.column}"
            )
            choice1 = solver.choices[int(digit)][self.cell_1.row][self.cell_1.column]
            choice2 = solver.choices[int(digit)][self.cell_2.row][self.cell_2.column]
            # pylint: disable=loop-invariant-statement
            solver.model += choice1 + choice2 <= 1, name

    def to_dict(self) -> Dict:
        """Convert the DifferencePair to a dictionary format.

        Returns:
            Dict: A dictionary representation of the difference pair.
        """
        return {
            self.__class__.__name__:
                (
                    f"{self.cell_1.row_column_string}"
                    f"-"
                    f"{self.cell_2.row_column_string}"
                    f"="
                    f"{','.join([str(d) for d in self.digits])}"
                )
        }
