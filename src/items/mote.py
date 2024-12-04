"""Mote."""
from pulp import lpSum

from src.glyphs.glyph import Glyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.region import Region
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class Mote(Region):
    """Represents a MOTE cage where the number of odd digits must exceed even digits."""

    def __init__(self, board: Board, total: int, cells: list[Item]):
        """Initialize the MOTE region.

        Args:
            board (Board): The Sudoku board.
            total (int): The total sum for the MOTE cage.
            cells (list[Item]): The list of cells in the cage.
        """
        super().__init__(board)
        self.total = total
        self.add_items(cells)

    def __repr__(self) -> str:
        """Return a string representation of the Mote instance.

        Returns:
            str: A string representation in the format
                Mote(board, total, cells).
        """
        return (
            f"{self.__class__.__name__}("
            f"{self.board!r}, "
            f"{self.total!r}, "
            f"{self.cells!r}"
            f")"
        )

    @classmethod
    def extract(cls, board: Board, yaml: dict) -> tuple[int, list[Item]]:
        """Extract the MOTE configuration from a YAML dictionary.

        Args:
            board (Board): The Sudoku board.
            yaml (dict): The YAML configuration dictionary.

        Returns:
            tuple[int, list[Item]]: The total sum and the list of cells.
        """
        parts: list[str] = yaml[cls.__name__].split("=")
        total: int = int(parts[0].strip())
        cells: list[Item] = [Cell.make(board, int(rc.strip()[0]), int(rc.strip()[1])) for rc in parts[1].split(',')]
        return total, cells

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create a MOTE region from a YAML dictionary.

        Args:
            board (Board): The Sudoku board.
            yaml (dict): The YAML configuration dictionary.

        Returns:
            Item: The created Mote instance.
        """
        total, cells = Mote.extract(board, yaml)
        return Mote(board, total, cells)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
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
        return [
            Rule(
                "MOTE",
                1,
                (
                    "More odd than even or MOTE cages. "
                    "In each cage, the number of odd digits is strictly greater than the number of even digits."
                )
            )
        ]

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
        # TODO: Adjust the constraint for odd digit counts
        odd_count = lpSum(solver.values[cell.row][cell.column] for cell in self.cells)
        name = f"{self.__class__.__name__}_{self.cells[0].row}{self.cells[0].column}"
        solver.model += odd_count > len(self.cells) // 2, name

    def to_dict(self) -> dict:
        """Convert the MOTE to a dictionary representation.

        Returns:
            dict: A dictionary with the MOTE's YAML representation.
        """
        cell_str = ",".join([f"{cell.row}{cell.column}" for cell in self.cells])
        return {self.__class__.__name__: f"{self.total}={cell_str}"}

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
                'fill': 'black'
            },
            '.MOTEForeground': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 1,
                'fill': 'black'
            },
            '.MOTEBackground': {
                'font-size': '30px',
                'stroke': 'white',
                'stroke-width': 8,
                'fill': 'white',
                'font-weight': 'bolder'
            }
        }
