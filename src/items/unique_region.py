from typing import List, Dict, Sequence
from src.glyphs.glyph import Glyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.region import Region
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class UniqueRegion(Region):
    """A region within the board where numbers cannot repeat."""

    def __init__(self, board: Board, cells: Sequence[Item]):
        """Initialize a UniqueRegion instance.

        Args:
            board (Board): The board associated with this region.
            cells (Sequence[Item]): Sequence of items representing cells in the region.
        """
        super().__init__(board)
        self.add_items(cells)

    def __repr__(self) -> str:
        """Return a string representation of the UniqueRegion instance.

        Returns:
            str: A string representation of the UniqueRegion.
        """
        return (
            f"{self.__class__.__name__}("
            f"{self.board!r}, "
            f"{repr(self.cells)}"
            f")"
        )

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Sequence[Cell]:
        """Extract cells from YAML configuration for the unique region.

        Args:
            board (Board): The board associated with this region.
            yaml (Dict): The YAML configuration containing cell data for the unique region.

        Returns:
            List[Item]: A list of cell items for the unique region.
        """
        return [Cell.make(board, int(rc.strip()[0]), int(rc.strip()[1])) for rc in yaml['UniqueRegion'].split(',')]

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        """Create a UniqueRegion instance from YAML configuration.

        Args:
            board (Board): The board associated with this region.
            yaml (Dict): The YAML configuration containing cell data for the unique region.

        Returns:
            Item: A new UniqueRegion instance.
        """
        return UniqueRegion(board, UniqueRegion.extract(board, yaml))

    def glyphs(self) -> List[Glyph]:
        """Get the list of glyphs associated with this unique region.

        Returns:
            List[Glyph]: A list of glyphs for the unique region.
        """
        return []

    @property
    def rules(self) -> List[Rule]:
        """Retrieve the rules associated with this unique region.

        Returns:
            List[Rule]: A list of rules indicating the uniqueness constraint in this region.
        """
        return [
            Rule(
                "UniqueRegion",
                1,
                "Numbers cannot repeat within the Unique Region."
            )
        ]

    @property
    def tags(self) -> set[str]:
        """Get tags associated with the unique region.

        Returns:
            set[str]: A set of tags for identifying the region.
        """
        return super().tags.union({'UniqueRegion'})

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add the unique constraint for this region to the solver.

        Args:
            solver (PulpSolver): The solver to which constraints will be added.
        """
        self.add_unique_constraint(solver)

    def to_dict(self) -> Dict:
        """Convert the UniqueRegion instance to a dictionary representation.

        Returns:
            Dict: A dictionary representation of the UniqueRegion.
        """
        cell_str = ",".join([f"{cell.row}{cell.column}" for cell in self.cells])
        return {self.__class__.__name__: f"{cell_str}"}

    def css(self) -> Dict:
        """Get CSS styles for the unique region.

        Returns:
            Dict: A dictionary containing CSS styles for the UniqueRegion.
        """
        return {
            '.UniqueRegion': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 2,
                'fill': 'black'
            },
            '.UniqueRegionForeground': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 1,
                'fill': 'black'
            },
            '.UniqueRegionBackground': {
                'font-size': '30px',
                'stroke': 'white',
                'stroke-width': 8,
                'fill': 'white',
                'font-weight': 'bolder'
            }
        }
