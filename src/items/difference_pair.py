"""DifferencePair."""

from src.board.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.pair import Pair
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class DifferencePair(Pair):
    """Represents a pair of cells that have specified differences in their value_list."""

    def __init__(self, board: Board, cell1: Cell, cell2: Cell, digits: list[int]):
        """Initialize start DifferencePair.

        Args:
            board (Board): The Sudoku board instance.
            cell1 (Cell): The first cell in the pair.
            cell2 (Cell): The second cell in the pair.
            digits (list[int]): A list of digits representing the allowed differences between the cell value_list.
        """
        super().__init__(board, cell1, cell2)
        self.digits = digits

    def __repr__(self) -> str:
        """Return a string representation of the DifferencePair.

        Returns:
            str: A string representation of the DifferencePair.
        """
        return f'{self.__class__.__name__}({self.board!r}, {self.cell1!r}, {self.cell2!r}, {self.digits!r})'

    @classmethod
    def extract(cls, board: Board, yaml: dict) -> tuple[Cell, Cell, list[int]]:
        """Extract cells and their allowed difference value_list from YAML line.

        Args:
            board (Board): The board instance for cell creation.
            yaml (dict): The YAML line containing the cell pair and their difference value_list.

        Returns:
            tuple[Cell, Cell, list[int]]: A tuple containing two cells and start list of allowed difference value_list.
        """
        cell_part: str = yaml[cls.__name__].split('=')[0]
        difference_part = yaml[cls.__name__].split('=')[1]
        text1: str = cell_part.split('-')[0]
        text2: str = cell_part.split('-')[1]
        cell1: Cell = Cell.make(board, int(text1[0]), int(text1[1]))
        cell2: Cell = Cell.make(board, int(text2[0]), int(text2[1]))
        digits = [int(digit) for digit in difference_part.split(',')]
        return cell1, cell2, digits

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create a DifferencePair instance from YAML line.

        Args:
            board (Board): The board instance.
            yaml (dict): The YAML line containing the cell pair and allowed differences.

        Returns:
            Item: An instance of DifferencePair.
        """
        cell1, cell2, digits = cls.extract(board, yaml)
        return cls(board, cell1, cell2, digits)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create a DifferencePair instance from YAML line.

        Args:
            board (Board): The board instance.
            yaml_data (dict): The YAML line containing the cell pair and allowed differences.

        Returns:
            Item: An instance of DifferencePair.
        """
        return cls.create(board, yaml_data)

    @property
    def rules(self) -> list[Rule]:
        """Retrieve the rules for the difference pair.

        Returns:
            list[Rule]: A list of rules, which is empty for this class.
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
                f'{self.__class__.__name__}'
                f'_'
                f'{digit}'
                f'_'
                f'{self.cell1.row}'
                f'_'
                f'{self.cell1.column}'
                f'_'
                f'{self.cell2.row}'
                f'_'
                f'{self.cell2.column}'
            )
            choice1 = solver.variables.choices[int(digit)][self.cell1.row][self.cell1.column]
            choice2 = solver.variables.choices[int(digit)][self.cell2.row][self.cell2.column]
            # pylint: disable=loop-invariant-statement
            solver.model += choice1 + choice2 <= 1, name

    def to_dict(self) -> dict:
        """Convert the DifferencePair to start dictionary format.

        Returns:
            dict: A dictionary representation of the difference pair.
        """
        return {
            self.__class__.__name__:
                (
                    f'{self.cell1.row_column_string}'
                    f'-'
                    f'{self.cell2.row_column_string}'
                    f'='
                    f'{",".join([str(digit) for digit in self.digits])}'
                ),
        }
