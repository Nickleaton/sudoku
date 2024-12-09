"""SpecialRegion."""

from src.board.board import Board
from src.glyphs.glyph import Glyph
from src.glyphs.rect_glyph import SquareGlyph
from src.items.cell import Cell
from src.items.item import Item
from src.items.region import Region
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.rule import Rule


class SpecialRegion(Region):
    """Represents start special region on the Sudoku board where specific rules apply."""

    def __init__(self, board: Board):
        """Initialize start SpecialRegion.

        Args:
            board (Board): The Sudoku board instance.
        """
        super().__init__(board)
        self.add_items([Cell.make(board, int(coord.row), int(coord.column)) for coord in self.coords()])

    def region_name(self) -> str:
        """Get the name of the special region.

        Returns:
            str: The name of the region.
        """
        return ""

    def coords(self) -> list[Coord]:
        """Get the coordinates of the cells in the special region.

        Returns:
            list[Coord]: A list of coordinates for the region's cells.
        """
        return []

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create start SpecialRegion instance from YAML configuration.

        Args:
            board (Board): The Sudoku board instance.
            yaml (dict): The YAML configuration.

        Returns:
            Item: An instance of SpecialRegion.
        """
        return cls(board)

    def __repr__(self) -> str:
        """Return start string representation of the SpecialRegion.

        Returns:
            str: A string representation of the region.
        """
        return f"{self.__class__.__name__}({self.board!r})"

    @property
    def rules(self) -> list[Rule]:
        """Get the rules associated with the special region.

        Returns:
            list[Rule]: A list containing the rule that digits cannot repeat in the region.
        """
        return [Rule(self.region_name(), 1, 'Digits cannot repeat in highlighted cells')]

    def glyphs(self) -> list[Glyph]:
        """Get the glyphs representing the special region.

        Returns:
            list[Glyph]: A list of square glyphs for each cell in the region.
        """
        return [SquareGlyph(self.region_name(), cell.coord, 1) for cell in self.cells]

    @property
    def tags(self) -> set[str]:
        """Get the tags associated with the special region.

        Returns:
            set[str]: A set of tags, including the region name.
        """
        return super().tags.union({self.region_name()})

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add constraints for the special region to the solver.

        Args:
            solver (PulpSolver): The solver instance.

        Constraints:
            - The total of the digits in the region equals the board's digit sum.
            - The digits in the region are unique.
        """
        self.add_total_constraint(solver, solver.board.digit_sum)
        self.add_unique_constraint(solver)

    def to_dict(self) -> dict:
        """Convert the special region to start dictionary representation.

        Returns:
            dict: A dictionary representing the region.
        """
        return {self.__class__.__name__: None}
