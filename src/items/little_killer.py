"""LittleKiller."""
from typing import Dict, List, Tuple

from pulp import lpSum

from src.glyphs.arrow_glyph import ArrowGlyph
from src.glyphs.glyph import Glyph
from src.glyphs.text_glyph import TextGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.region import Region
from src.parsers.little_killers_parser import LittleKillersParser
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.cyclic import Cyclic
from src.utils.rule import Rule
from src.utils.side import Side


class LittleKiller(Region):
    """Represents a Little Killer puzzle region.

    Clues outside the grid give the sum of the indicated diagonals, which may contain repeated digits.
    """

    def __init__(self, board: Board, side: Side, cyclic: Cyclic, offset: int, total: int):
        """Construct a LittleKiller region.

        Args:
            board (Board): The board being used.
            side (Side): The side where the total is to go.
            cyclic (Cyclic): The cyclic nature of the region.
            offset (int): The offset to calculate the starting position.
            total (int): The total sum of the indicated diagonals.
        """
        super().__init__(board)
        self.side = side
        self.cyclic = cyclic
        self.offset = offset
        self.total = total
        coord = side.start(board, cyclic, offset)
        self.direction = side.direction(cyclic)
        self.delta = self.direction.offset
        cells = []
        while board.is_valid_coordinate(coord):
            cells.append(Cell.make(board, int(coord.row), int(coord.column)))
            coord += self.delta
        self.add_items(cells)
        self.reference = side.start(board, cyclic, offset) - self.delta

    @classmethod
    def is_sequence(cls) -> bool:
        """Return whether this item is a sequence.

        Returns:
            bool: True, since LittleKiller is considered a sequence.
        """
        return True

    @classmethod
    def parser(cls) -> LittleKillersParser:
        """Return the parser used to extract data for the LittleKiller region.

        Returns:
            LittleKillersParser: The parser for LittleKiller regions.
        """
        return LittleKillersParser()

    def __repr__(self) -> str:
        """Return a string representation of the LittleKiller region.

        Returns:
            str: A string representation of the LittleKiller object.
        """
        return (
            f"{self.__class__.__name__}("
            f"{self.board!r}, "
            f"{self.side!r}, "
            f"{self.cyclic!r}, "
            f"{self.offset!r}, "
            f"{self.total!r}"
            f")"
        )

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Tuple[int, int, Cyclic, Side]:
        """Extract the parameters for creating a LittleKiller region from the YAML input.

        Args:
            board (Board): The board being used.
            yaml (Dict): The YAML configuration for the LittleKiller region.

        Returns:
            Tuple[int, int, Cyclic, Side]: A tuple containing the total, offset, cyclic, and side values.
        """
        parts = yaml[cls.__name__].split("=")
        total = int(parts[1])
        offset = int(parts[0][1])
        cyclic = Cyclic.create(parts[0][-1])
        side = Side.create(parts[0][0])
        return total, offset, cyclic, side

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        """Create a LittleKiller region from the YAML configuration.

        Args:
            board (Board): The board being used.
            yaml (Dict): The YAML configuration for the LittleKiller region.

        Returns:
            Item: The created LittleKiller item.
        """
        total, offset, cyclic, side = LittleKiller.extract(board, yaml)
        return LittleKiller(board, side, cyclic, offset, total)

    def glyphs(self) -> List[Glyph]:
        """Return a list of glyphs representing the LittleKiller region.

        Returns:
            List[Glyph]: A list of glyphs, including text and arrows.
        """
        delta2 = Coord(0, 0)
        if self.side == Side.TOP:
            delta2 = Coord(0, 1)
        if self.side == Side.RIGHT:
            delta2 = Coord(0, 1)
        return [
            TextGlyph('LittleKiller', 0, self.reference + Coord(0.5, 0.5), str(self.total)),
            ArrowGlyph('LittleKiller', self.direction.angle.angle, self.reference + (self.delta * 0.90) + delta2)
        ]

    @property
    def rules(self) -> List[Rule]:
        """Return the rules associated with the LittleKiller region.

        Returns:
            List[Rule]: A list of rules defining the LittleKiller region's constraints.
        """
        return [
            Rule(
                "LittleKiller",
                1,
                "Clues outside the grid give the sum of the indicated diagonals, which may contain repeated digits"
            )
        ]

    @property
    def tags(self) -> set[str]:
        """Return the tags associated with the LittleKiller region.

        Returns:
            set[str]: A set of tags associated with the LittleKiller region.
        """
        return super().tags.union({'LittleKiller', 'Killer'})

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add the constraint for the LittleKiller region to the solver.

        Args:
            solver (PulpSolver): The solver to add the constraint to.
        """
        total = lpSum(solver.values[cell.row][cell.column] for cell in self.cells)
        name = f"{self.__class__.__name__}_{self.side.value}{self.offset}{self.cyclic.value}"
        solver.model += total == self.total, name

    def to_dict(self) -> Dict:
        """Convert the LittleKiller region to a dictionary representation.

        Returns:
            Dict: A dictionary representing the LittleKiller region.
        """
        return {self.__class__.__name__: f"{self.side.value}{self.offset}{self.cyclic.value}={self.total}"}

    def css(self) -> Dict:
        """Return the CSS styling for the LittleKiller region.

        Returns:
            Dict: A dictionary of CSS styles for the LittleKiller region.
        """
        return {
            '.LittleKiller': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 2,
                'fill': 'black'
            },
            '.LittleKillerForeground': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 1,
                'fill': 'black'
            },
            '.LittleKillerBackground': {
                'font-size': '30px',
                'stroke': 'white',
                'stroke-width': 8,
                'fill': 'white',
                'font-weight': 'bolder'
            },
            '.LittleArrow': {
                'font-size': '20px',
                'stroke': 'black',
                'stroke-width': 1,
                'fill': 'black'
            }
        }

