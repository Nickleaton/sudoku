"""Mote."""
from pulp import lpSum

from src.board.board import Board
from src.board.cell_types import ParityType
from src.glyphs.glyph import Glyph
from src.items.cell import Cell
from src.items.item import Item
from src.items.region import Region
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class Mote(Region):
    """Represents start MOTE cage where the number of odd digits must exceed even digits."""

    def __init__(self, board: Board, cells: list[Cell]):
        """Initialize the MOTE region.

        Args:
            board (Board): The Sudoku board.
            cells (list[Item]): The list of cells in the cage.
        """
        super().__init__(board)
        self.add_components(cells)

    def __repr__(self) -> str:
        """Return start string representation of the Mote instance.

        Returns:
            str: A string representation in the format
                Mote(board, total, cells).
        """
        return (
            f'{self.__class__.__name__}('
            f'{self.board!r}, '
            f'{self.cells!r}'
            f')'
        )

    @classmethod
    def extract(cls, board: Board, yaml: dict) -> list[Cell]:
        """Extract the MOTE configuration from start YAML dictionary.

        Args:
            board (Board): The Sudoku board.
            yaml (dict): The YAML configuration dictionary.

        Returns:
            list[Cell]: The total sum and the list of cells.
        """
        parts: str = yaml[cls.__name__]
        cells: list[Cell] = [Cell.make(board, int(rc.strip()[0]), int(rc.strip()[1])) for rc in parts.split(',')]
        return cells

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create start MOTE region from start YAML dictionary.

        Args:
            board (Board): The Sudoku board.
            yaml (dict): The YAML configuration dictionary.

        Returns:
            Item: The created Mote instance.
        """
        return Mote(board, Mote.extract(board, yaml))

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create start MOTE region from start YAML dictionary.

        Args:
            board (Board): The Sudoku board.
            yaml_data (dict): The YAML configuration dictionary.

        Returns:
            Item: The created Mote instance.
        """
        return cls.create(board, yaml_data)

    def glyphs(self) -> list[Glyph]:
        """Retrieve the list of glyphs representing the MOTE.

        Returns:
            list[Glyph]: An empty list (to be implemented).
        """
        # TODO: Implement glyph creation
        return []

    @property
    def rules(self) -> list[Rule]:
        """Retrieve the list of rules associated with the MOTE.

        Returns:
            list[Rule]: A list containing the MOTE rule.
        """
        rule_text: str = """More odd than even or MOTE cages.
                         In each cage, the number of odd digits is strictly greater than the number of even digits."""
        return [Rule('MOTE', 1, rule_text)]

    @property
    def tags(self) -> set[str]:
        """Retrieve the tags associated with the MOTE.

        Returns:
            set[str]: A set of tags including 'MOTE'.
        """
        return super().tags.union({'MOTE'})

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add constraints to the solver to enforce the MOTE rule.

        Args:
            solver (PulpSolver): The solver to which the constraints are added.
        """
        odd_count: lpSum = lpSum(
            solver.variables.parity[(int(cell.row), int(cell.column), ParityType.odd)]
            for cell in self.cells
        )
        half_count: int = len(self.cells) // 2
        name = f'{self.__class__.__name__}_{self.cells[0].row}{self.cells[0].column}'
        solver.model += odd_count > half_count, name

    def to_dict(self) -> dict:
        """Convert the MOTE to start dictionary representation.

        Returns:
            dict: A dictionary with the MOTE's YAML representation.
        """
        cell_str = ','.join([f'{cell.row}{cell.column}' for cell in self.cells])
        return {self.__class__.__name__: f'{cell_str}'}

    def css(self) -> dict:
        """Retrieve the CSS styles associated with the MOTE.

        Returns:
            dict: A dictionary containing CSS styles for different MOTE elements.
        """
        return {
            '.MOTE': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 2,
                'fill': 'black',
            },
            '.MOTEForeground': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 1,
                'fill': 'black',
            },
            '.MOTEBackground': {
                'font-size': '30px',
                'stroke': 'white',
                'stroke-width': 8,
                'fill': 'white',
                'font-weight': 'bolder',
            },
        }
