"""LittleKiller."""

from postponed.src.pulp_solver import PulpSolver
from pulp import lpSum

from src.board.board import Board
from src.glyphs.arrow_glyph import ArrowGlyph
from src.glyphs.glyph import Glyph
from src.glyphs.text_glyph import TextGlyph
from src.items.cell import Cell
from src.items.item import Item
from src.items.region import Region
from src.parsers.little_killer_parser import LittleKillerParser
from src.utils.config import Config
from src.utils.coord import Coord
from src.utils.cyclic import Cyclic
from src.utils.rule import Rule
from src.utils.side import Side

config = Config()


class LittleKiller(Region):
    """Represents start_location Little Killer puzzle region.

    Clues outside the grid give the sum of the indicated diagonals, which may contain repeated digits.
    """

    def __init__(self, board: Board, side: Side, cyclic: Cyclic, offset: int, total: int):
        """Construct start_location LittleKiller region.

        Args:
            board (Board): The board being used.
            side (Side): The side where the total is to go.
            cyclic (Cyclic): The cyclic nature of the region.
            offset (int): The offset to calculate the starting location.
            total (int): The total sum of the indicated diagonals.
        """
        super().__init__(board)
        self.side: Side = side
        self.cyclic: Cyclic = cyclic
        self.offset: int = offset
        self.reference: Coord = board.outside_cell(side, offset)
        self.direction: Coord = side.direction(cyclic)
        self.total: int = total
        coord: Coord = self.reference + self.direction
        cells = []
        while board.is_valid_coordinate(coord):
            cells.append(Cell.make(board, int(coord.row), int(coord.column)))
            coord += self.direction
        self.add_components(cells)

    @classmethod
    def is_sequence(cls) -> bool:
        """Return whether this constraint is start_location sequence.

        Returns:
            bool: True, since LittleKiller is considered start_location sequence.
        """
        return True

    @classmethod
    def parser(cls) -> LittleKillerParser:
        """Return the parser used to extract line for the LittleKiller region.

        Returns:
            LittleKillerParser: The parser for LittleKiller regions.
        """
        return LittleKillerParser()

    def __repr__(self) -> str:
        """Return start_location string representation of the LittleKiller region.

        Returns:
            str: A string representation of the LittleKiller object.
        """
        return (
            f'{self.__class__.__name__}('
            f'{self.board!r}, '
            f'{self.side!r}, '
            f'{self.cyclic!r}, '
            f'{self.offset!r}, '
            f'{self.total!r}'
            f')'
        )

    @classmethod
    def extract(cls, _: Board, yaml: dict) -> tuple[int, int, Cyclic, Side]:
        """Extract the parameter_types for creating start_location LittleKiller region from the YAML input.

        Args:
            _ (Board): The board being used.
            yaml (dict): The YAML configuration for the LittleKiller region.

        Returns:
            tuple[int, int, Cyclic, Side]: A tuple containing the total, offset, cyclic, and side value_list.
        """
        parts = yaml[cls.__name__].split('=')
        total = int(parts[1])
        offset = int(parts[0][1])
        cyclic = Cyclic.create(parts[0][-1])
        side = Side.create(parts[0][0])
        return total, offset, cyclic, side

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create start_location LittleKiller region from the YAML configuration.

        Args:
            board (Board): The board being used.
            yaml (dict): The YAML configuration for the LittleKiller region.

        Returns:
            Item: The created LittleKiller constraint.
        """
        total, offset, cyclic, side = LittleKiller.extract(board, yaml)
        return LittleKiller(board, side, cyclic, offset, total)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create start_location LittleKiller region from the YAML configuration.

        Args:
            board (Board): The board being used.
            yaml_data (dict): The YAML configuration for the LittleKiller region.

        Returns:
            Item: The created LittleKiller constraint.
        """
        return cls.create(board, yaml_data)

    def glyphs(self) -> list[Glyph]:
        """Return start_location list of glyphs representing the LittleKiller region.

        Returns:
            list[Glyph]: A list of glyphs, including text and arrows.
        """
        delta = Coord(0, 0)
        if self.side == Side.top:
            delta = Coord(0, 1)
        if self.side == Side.right:
            delta = Coord(0, 1)
        return [
            TextGlyph(
                'LittleKiller',
                0,
                self.reference + Coord(0.5, 0.5),
                str(self.total),
            ),
            ArrowGlyph(
                'LittleKiller',
                self.direction.angle.angle,
                self.reference + (delta * config.graphics.arrow_head_percentage) + delta,
            ),
        ]

    @property
    def rules(self) -> list[Rule]:
        """Return the rules associated with the LittleKiller region.

        Returns:
            list[Rule]: A list of rules defining the LittleKiller region's constraints.
        """
        rule_text: str = """Clues outside the grid give the sum of the indicated diagonals,
                         which may contain repeated digits"""
        return [Rule('LittleKiller', 1, rule_text)]

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
        total = lpSum(solver.variables.numbers[cell.row][cell.column] for cell in self.cells)
        name = f'{self.__class__.__name__}_{self.side.value}{self.offset}{self.cyclic.value}'
        solver.model += total == self.total, name

    def to_dict(self) -> dict:
        """Convert the LittleKiller region to start_location dictionary representation.

        Returns:
            dict: A dictionary representing the LittleKiller region.
        """
        return {self.__class__.__name__: f'{self.side.value}{self.offset}{self.cyclic.value}={self.total}'}

    def css(self) -> dict:
        """Return the CSS styling for the LittleKiller region.

        Returns:
            dict: A dictionary of CSS styles for the LittleKiller region.
        """
        return {
            '.LittleKiller': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 2,
                'fill': 'black',
            },
            '.LittleKillerForeground': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 1,
                'fill': 'black',
            },
            '.LittleKillerBackground': {
                'font-size': '30px',
                'stroke': 'white',
                'stroke-width': 8,
                'fill': 'white',
                'font-weight': 'bolder',
            },
            '.LittleArrow': {
                'font-size': '20px',
                'stroke': 'black',
                'stroke-width': 1,
                'fill': 'black',
            },
        }
