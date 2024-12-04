"""FixedPair."""

from pulp import LpElement

from src.glyphs.circle_glyph import CircleGlyph
from src.glyphs.glyph import Glyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.pair import Pair
from src.parsers.cell_pair_equal_value_parser import CellPairEqualValueParser
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord


class FixedPair(Pair):
    """Represents a fixed pair constraint between two cells, where the digits in both cells are equal."""

    def __init__(self, board: Board, cell_1: Cell, cell_2: Cell, value: int):
        """Initialize a FixedPair with two cells and a fixed value.

        Args:
            board (Board): The board this pair belongs to.
            cell_1 (Cell): The first cell in the pair.
            cell_2 (Cell): The second cell in the pair.
            value (int): The value that both cells should have.
        """
        super().__init__(board, cell_1, cell_2)
        self.value = value

    @classmethod
    def is_sequence(cls) -> bool:
        """Return True, as FixedPair is considered a sequence.

        Returns:
            bool: True, indicating this is a sequence.
        """
        return True

    @classmethod
    def parser(cls) -> CellPairEqualValueParser:
        """Return the parser for this item to parse cell pairs with equal values.

        Returns:
            CellPairEqualValueParser: The parser that handles this FixedPair item.
        """
        return CellPairEqualValueParser()

    @classmethod
    def extract(cls, board: Board, yaml: dict) -> tuple:
        """Extract the fixed pair information from a YAML dictionary.

        Args:
            board (Board): The board this pair belongs to.
            yaml (dict): The dictionary containing the pair's configuration.

        Returns:
            tuple: A tuple containing the row and column coordinates of the two cells, and the fixed value.
        """
        lhs: str = yaml[cls.__name__].split('=')[0]
        value: int = int(yaml[cls.__name__].split('=')[1])
        a: str = lhs.split('-')[0]
        b: str = lhs.split('-')[1]
        r1: int = int(a[0])
        c1: int = int(a[1])
        r2: int = int(b[0])
        c2: int = int(b[1])
        return r1, c1, r2, c2, value

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create a FixedPair from a YAML dictionary.

        Args:
            board (Board): The board to associate the pair with.
            yaml (dict): The dictionary containing the pair's configuration.

        Returns:
            Item: The created FixedPair item.
        """
        r1, c1, r2, c2, value = cls.extract(board, yaml)
        return cls(board, Cell(board, r1, c1), Cell(board, r2, c2), value)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        return cls.create(board, yaml_data)

    @property
    def tags(self) -> set[str]:
        """Return the tags associated with the FixedPair item.

        Returns:
            set[str]: A set of tags, including 'Fixed Pair', to categorize the item.
        """
        return super().tags.union({'Fixed Pair'})

    @property
    def label(self) -> str:
        """Return an empty label for the FixedPair.

        Returns:
            str: An empty string, as there is no label for this item.
        """
        return ""

    def glyphs(self) -> list[Glyph]:
        """Return the graphical representation of the FixedPair as a circle glyph.

        Returns:
            list[Glyph]: A list containing the glyph for visualizing the FixedPair.
        """
        return [
            CircleGlyph(
                self.__class__.__name__,
                Coord.middle(self.cell_1.coord.center, self.cell_2.coord.center),
                0.15
            )
        ]

    def to_dict(self) -> dict:
        """Return a dictionary representation of the FixedPair.

        Returns:
            dict: A dictionary with the FixedPair's row-column pairs and value.
        """
        return {
            self.__class__.__name__: f"{self.cell_1.row_column_string}-{self.cell_2.row_column_string}={self.value}"
        }

    def target(self, solver: PulpSolver) -> LpElement | None:
        """Return the target constraint for the FixedPair, which is None.

        Returns:
            LpElement | None: None, as there is no specific target for the FixedPair.
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
        """Return a string representation of the FixedPair.

        Returns:
            str: A string that represents the FixedPair object.
        """
        return f"{self.__class__.__name__}({self.board!r}, {self.cell_1!r}, {self.cell_2!r}, {self.value!r})"
