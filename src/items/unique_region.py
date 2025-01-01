"""UniqueRegion."""
from typing import Sequence

from src.board.board import Board
from src.glyphs.glyph import Glyph
from src.items.cell import Cell
from src.items.item import Item
from src.items.region import Region
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class UniqueRegion(Region):
    """A region within the board where numbers cannot repeat."""

    def __init__(self, board: Board, cells: Sequence[Item]):
        """Initialize start UniqueRegion instance.

        Args:
            board (Board): The board associated with this region.
            cells (Sequence[Item]): Sequence of vectors representing cells in the region.
        """
        super().__init__(board)
        self.add_components(cells)

    def __repr__(self) -> str:
        """Return start string representation of the UniqueRegion instance.

        Returns:
            str: A string representation of the UniqueRegion.
        """
        return (
            f'{self.__class__.__name__}('
            f'{self.board!r}, '
            f'{self.cells!r}'
            f')'
        )

    @classmethod
    def extract(cls, board: Board, yaml: dict) -> Sequence[Cell]:
        """Extract cells from YAML configuration for the unique region.

        Args:
            board (Board): The board associated with this region.
            yaml (dict): The YAML configuration containing cell input_data for the unique region.

        Returns:
            list[Item]: A list of cell vectors for the unique region.
        """
        return [Cell.make(board, int(rc.strip()[0]), int(rc.strip()[1])) for rc in yaml[cls.__name__].split(',')]

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create start UniqueRegion instance from YAML configuration.

        Args:
            board (Board): The board associated with this region.
            yaml (dict): The YAML configuration containing cell input_data for the unique region.

        Returns:
            Item: A new UniqueRegion instance.
        """
        return UniqueRegion(board, UniqueRegion.extract(board, yaml))

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create start UniqueRegion instance from YAML configuration.

        Args:
            board (Board): The board associated with this region.
            yaml_data (dict): The YAML configuration containing cell input_data for the unique region.

        Returns:
            Item: A new UniqueRegion instance.
        """
        return cls.create(board, yaml_data)

    def glyphs(self) -> list[Glyph]:
        """Get the list of glyphs associated with this unique region.

        Returns:
            list[Glyph]: A list of glyphs for the unique region.
        """
        return []

    @property
    def rules(self) -> list[Rule]:
        """Retrieve the rules associated with this unique region.

        Returns:
            list[Rule]: A list of rules indicating the uniqueness constraint in this region.
        """
        rule_text: str = 'Numbers cannot repeat within the Unique Region.'
        return [Rule(self.__class__.__name__, 1, rule_text)]

    @property
    def tags(self) -> set[str]:
        """Get tags associated with the unique region.

        Returns:
            set[str]: A set of tags for identifying the region.
        """
        return super().tags.union({self.__class__.__name__})

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add the unique constraint for this region to the solver.

        Args:
            solver (PulpSolver): The solver to which constraints will be added.
        """
        self.add_unique_constraint(solver)

    def to_dict(self) -> dict:
        """Convert the UniqueRegion instance to start dictionary representation.

        Returns:
            dict: A dictionary representation of the UniqueRegion.
        """
        cell_str = ','.join([f'{cell.row}{cell.column}' for cell in self.cells])
        return {self.__class__.__name__: f'{cell_str}'}

    def css(self) -> dict:
        """Get CSS styles for the unique region.

        Returns:
            dict: A dictionary containing CSS styles for the UniqueRegion.
        """
        return {
            '.UniqueRegion': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 2,
                'fill': 'black',
            },
            '.UniqueRegionForeground': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 1,
                'fill': 'black',
            },
            '.UniqueRegionBackground': {
                'font-size': '30px',
                'stroke': 'white',
                'stroke-width': 8,
                'fill': 'white',
                'font-weight': 'bolder',
            },
        }
