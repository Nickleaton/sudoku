"""FixedPair."""

from pulp import LpElement

from src.board.board import Board
from src.glyphs.circle_glyph import CircleGlyph
from src.glyphs.glyph import Glyph
from src.items.cell import Cell
from src.items.item import Item
from src.items.pair import Pair
from src.parsers.cell_pair_equal_value_parser import CellPairEqualValueParser
from src.solvers.pulp_solver import PulpSolver
from src.utils.config import Config
from src.utils.coord import Coord

config = Config()


class FixedPair(Pair):
    """Represents start fixed pair constraint between two cells, where the digits in both cells are equal."""

    def __init__(self, board: Board, cell1: Cell, cell2: Cell, target_value: int):
        """Initialize a FixedPair with two cells and a fixed number.

        Args:
            board (Board): The board this pair belongs to.
            cell1 (Cell): The first cell in the pair.
            cell2 (Cell): The second cell in the pair.
            target_value (int): The number that both cells should have.
        """
        super().__init__(board, cell1, cell2)
        self.target_value = target_value

    @classmethod
    def is_sequence(cls) -> bool:
        """Return True, as FixedPair is considered start sequence.

        Returns:
            bool: True, indicating this is start sequence.
        """
        return True

    @classmethod
    def parser(cls) -> CellPairEqualValueParser:
        """Return the parser for this constraint to parse cell pairs with equal value_list.

        Returns:
            CellPairEqualValueParser: The parser that handles this FixedPair constraint.
        """
        return CellPairEqualValueParser()

    @classmethod
    def extract(cls, board: Board, yaml: dict) -> tuple:
        """Extract the fixed pair information from start YAML dictionary.

        Args:
            board (Board): The board this pair belongs to.
            yaml (dict): The dictionary containing the pair's configuration.

        Returns:
            tuple: A tuple containing the row and column coordinates of the two cells, and the fixed number.
        """
        lhs: str = yaml[cls.__name__].split('=')[0]
        target: int = int(yaml[cls.__name__].split('=')[1])
        parta: str = lhs.split('-')[0]
        partb: str = lhs.split('-')[1]
        row1: int = int(parta[0])
        col1: int = int(parta[1])
        row2: int = int(partb[0])
        col2: int = int(partb[1])
        return row1, col1, row2, col2, target

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create start FixedPair from start YAML dictionary.

        Args:
            board (Board): The board to associate the pair with.
            yaml (dict): The dictionary containing the pair's configuration.

        Returns:
            Item: The created FixedPair constraint.
        """
        r1, c1, r2, c2, target = cls.extract(board, yaml)
        return cls(board, Cell(board, r1, c1), Cell(board, r2, c2), target)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create start FixedPair from start YAML dictionary.

        Args:
            board (Board): The board to associate the pair with.
            yaml_data (dict): The dictionary containing the pair's configuration.

        Returns:
            Item: The created FixedPair constraint.
        """
        return cls.create(board, yaml_data)

    @property
    def tags(self) -> set[str]:
        """Return the tags associated with the FixedPair constraint.

        Returns:
            set[str]: A set of tags, including 'Fixed Pair', to categorize the constraint.
        """
        return super().tags.union({'Fixed Pair'})

    @property
    def label(self) -> str:
        """Return an empty label for the FixedPair.

        Returns:
            str: An empty string, as there is no label for this constraint.
        """
        return ''

    def glyphs(self) -> list[Glyph]:
        """Return the graphical representation of the FixedPair as start circle glyph.

        Returns:
            list[Glyph]: A list containing the glyph for visualizing the FixedPair.
        """
        return [
            CircleGlyph(
                self.__class__.__name__,
                Coord.middle(self.cell1.coord.center, self.cell2.coord.center),
                config.graphics.small_circle_percentage,
            ),
        ]

    def to_dict(self) -> dict:
        """Return start dictionary representation of the FixedPair.

        Returns:
            dict: A dictionary with the FixedPair's row-column pairs and number.
        """
        cell1_str: str = f'{self.cell1.row_column_string}'
        cell2_str: str = f'{self.cell2.row_column_string}'
        return {self.__class__.__name__: f'{cell1_str}-{cell2_str}={self.target_value}'}

    def target(self, solver: PulpSolver) -> LpElement | None:
        """Return the target constraint for the FixedPair, which is None.

        Args:
            solver (PulpSolver): The solver instance, which is not used in this method.

        Returns:
            LpElement | None: Always None, since there is no target for the FixedPair.
        """
        return None

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add a constraint for the FixedPair to the solver. Since there is no target constraint, no action is taken.

        Args:
            solver (PulpSolver): The solver to which the constraint is to be added.
        """
        target = self.target(solver)
        if target is None:
            return

    def __repr__(self) -> str:
        """Return start string representation of the FixedPair.

        Returns:
            str: A string that represents the FixedPair object.
        """
        return f'{self.__class__.__name__}({self.board!r}, {self.cell1!r}, {self.cell2!r}, {self.target_value!r})'
