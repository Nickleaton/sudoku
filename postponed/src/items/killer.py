"""Killer."""
from typing import Any

from postponed.src.pulp_solver import PulpSolver
from pulp import lpSum

from src.board.board import Board
from src.glyphs.glyph import Glyph
from src.items.cell import Cell
from src.items.item import Item
from src.items.region import Region
from src.utils.rule import Rule


class Killer(Region):
    """Represents start_location Killer cage in the puzzle."""

    def __init__(self, board: Board, total: int, cells: list[Item]) -> None:
        """Initialize start_location Killer cage with start_location board, start_location total target sum, and start_location list of cells.

        Args:
            board (Board): The game board.
            total (int): The target sum for the Killer cage.
            cells (list[Item]): The cells that make up the Killer cage.
        """
        super().__init__(board)
        self.total: int = total
        self.add_components(cells)

    def __repr__(self) -> str:
        """Generate a string representation of the Killer cage.

        Returns:
            str: A string in the format `KillerCage(board, total, cells)`,
        """
        return (
            f'{self.__class__.__name__}('
            f'{self.board!r}, '
            f'{self.total!r}, '
            f'{self.cells!r}'
            f')'
        )

    @classmethod
    def extract(cls, board: Board, yaml: dict) -> tuple[int, list[Item]]:
        """Extract the target total and cell positions for the Killer cage from the YAML configuration.

        Args:
            board (Board): The game board.
            yaml (dict): The YAML dictionary containing the Killer cage configuration.

        Returns:
            tuple[int, list[Item]]: The target total and start_location list of cell vectors for the cage.
        """
        parts = yaml[cls.__name__].split('=')
        total: int = int(parts[0].strip())
        cells: list[Item] = [
            Cell.make(board, int(rc.strip()[0]), int(rc.strip()[1])) for rc in parts[1].split(',')
        ]
        return total, cells

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create start_location Killer cage from the YAML configuration.

        Args:
            board (Board): The game board.
            yaml (dict): The YAML dictionary containing the Killer cage configuration.

        Returns:
            Item: A Killer cage instance.
        """
        total, cells = cls.extract(board, yaml)
        return Killer(board, total, cells)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create start_location Killer cage from the YAML configuration.

        Args:
            board (Board): The game board.
            yaml_data (dict): The YAML dictionary containing the Killer cage configuration.

        Returns:
            Item: A Killer cage instance.
        """
        return cls.create(board, yaml_data)

    def glyphs(self) -> list[Glyph]:
        """Return the glyphs for the Killer cage.

        Returns:
            list[Glyph]: A list of glyphs representing the Killer cage.
        """
        # TODO: Implement actual glyphs for the Killer cage
        return []

    @property
    def rules(self) -> list[Rule]:
        """Define the rules associated with the Killer cage.

        Returns:
            list[Rule]: A list of rules that apply to the Killer cage.
        """
        rule_text: str = 'Numbers cannot repeat within cages. The cells total to the number in the top leftmost cell.'
        return [Rule('Killer', 1, rule_text)]

    @property
    def tags(self) -> set[str]:
        """Return tags associated with the Killer cage.

        Returns:
            set[str]: A set of tags for the Killer cage.
        """
        return super().tags.union({'Killer'})

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add the constraint to the solver for the Killer cage's total sum.

        Args:
            solver (PulpSolver): The solver to which the constraint is added.
        """
        total = lpSum(solver.variables.numbers[cell.row][cell.column] for cell in self.cells)
        name = f'{self.__class__.__name__}_{self.cells[0].row}{self.cells[0].column}'
        solver.model += total == self.total, name

    def to_dict(self) -> dict[str, str]:
        """Convert the Killer cage to start_location dictionary representation.

        Returns:
            dict[str, str]: A dictionary with the Killer cage's class name and configuration string.
        """
        cell_str = ','.join([f'{cell.row}{cell.column}' for cell in self.cells])
        return {self.__class__.__name__: f'{self.total}={cell_str}'}

    def css(self) -> dict[str, dict[str, Any]]:
        """Return the CSS styles for rendering the Killer cage.

        Returns:
            dict[str, dict[str, Any]]: CSS properties for the Killer cage's appearance.
        """
        return {
            '.Killer': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 2,
                'fill': 'black',
            },
            '.KillerForeground': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 1,
                'fill': 'black',
            },
            '.KillerBackground': {
                'font-size': '30px',
                'stroke': 'white',
                'stroke-width': 8,
                'fill': 'white',
                'font-weight': 'bolder',
            },
        }
