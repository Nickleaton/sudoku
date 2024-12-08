"""Window."""

from src.board.board import Board
from src.glyphs.glyph import Glyph
from src.glyphs.rect_glyph import SquareGlyph
from src.items.cell import Cell
from src.items.item import Item
from src.items.region import Region
from src.parsers.cell_parser import CellParser
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.rule import Rule


class Window(Region):
    """Represents a window in a Sudoku-like board."""

    # TODO Offsets in Coords

    offsets = (
        Coord(-1, -1),
        Coord(-1, 0),
        Coord(-1, 1),
        Coord(0, -1),
        Coord(0, 0),
        Coord(0, 1),
        Coord(1, -1),
        Coord(1, 0),
        Coord(1, 1)
    )

    @classmethod
    def is_sequence(cls) -> bool:
        """Check if this item is a sequence.

        Returns:
            bool: True if this item is a sequence, otherwise False.
        """
        return True

    @classmethod
    def parser(cls) -> CellParser:
        """Get the parser for this class.

        Returns:
            CellParser: An instance of CellParser.
        """
        return CellParser()

    def __init__(self, board: Board, center: Coord):
        """Initialize the Window instance.

        Args:
            board (Board): The board on which the window exists.
            center (Coord): The center coordinate of the window.
        """
        super().__init__(board)
        self.center = center
        self.add_items(
            [
                Cell.make(board, int((center + offset).row), int((center + offset).column))
                for offset in Window.offsets
            ]
        )

    @classmethod
    def extract(cls, _: Board, yaml: dict) -> Coord:
        """Extract the center coordinate from the YAML data.

        Args:
            _ (Board): The board to extract data for.
            yaml (dict): The YAML data containing coordinates.

        Returns:
            Coord: The extracted coordinate.
        """
        data = str(yaml[cls.__name__])
        return Coord(int(data[0]), int(data[1]))

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create a Window instance from the YAML data.

        Args:
            board (Board): The board to create the window on.
            yaml (dict): The YAML data for the window.

        Returns:
            Item: The created Window instance.
        """
        coord: Coord = Window.extract(board, yaml)
        return cls(board, coord)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        return cls.create(board, yaml_data)

    def __repr__(self) -> str:
        """Return a string representation of the Window instance.

        Returns:
            str: A string representation of the Window.
        """
        return f"{self.__class__.__name__}({self.board!r}, {self.center!r})"

    @property
    def rules(self) -> list[Rule]:
        """Get the rules associated with this window.

        Returns:
            list[Rule]: A list of rules for the window.
        """
        return [Rule('Window', 1, 'Digits in same shaded window must be unique')]

    def glyphs(self) -> list[Glyph]:
        """Get the glyphs representing this window.

        Returns:
            list[Glyph]: A list of glyphs for the window.
        """
        return [SquareGlyph('Window', self.center - Coord(1, 1), 3)]

    @property
    def tags(self) -> set[str]:
        """Get the tags associated with this window.

        Returns:
            set[str]: A set of tags for the window.
        """
        return super().tags.union({'Window'})

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add constraints related to this window to the solver.

        Args:
            solver (PulpSolver): The solver to add constraints to.
        """
        self.add_total_constraint(solver, solver.board.digit_sum)
        self.add_unique_constraint(solver)

    def to_dict(self) -> dict:
        """Convert the window to a dictionary representation.

        Returns:
            dict: A dictionary representation of the window.
        """
        return {self.__class__.__name__: self.center.row * 10 + self.center.column}

    def css(self) -> dict:
        """Get the CSS styles for this window.

        Returns:
            dict: A dictionary of CSS styles for the window.
        """
        return {
            '.Window': {
                'fill': 'lightcyan'
            }
        }
