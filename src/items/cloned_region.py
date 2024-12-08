"""ClonedRegion."""
from typing import Type, Iterator

from src.board.board import Board
from src.glyphs.glyph import Glyph
from src.items.cell import Cell
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule
from src.utils.sudoku_exception import SudokuException


class ClonedRegion(Item):
    """Represents a cloned region constraint in a Sudoku variant."""

    def __init__(self, board: Board, cells_a: list[Cell], cells_b: list[Cell]):
        """Initialize a ClonedRegion with two sets of cells that must have the same values.

        Args:
            board (Board): The Sudoku board instance.
            cells_a (list[Cell]): The first set of cells in the cloned region.
            cells_b (list[Cell]): The second set of cells in the cloned region.
        """
        super().__init__(board)
        if len(cells_a) != len(cells_b):
            raise SudokuException(
                f"Length mismatch: cells_a has {len(cells_a)} elements, but cells_b has {len(cells_b)} elements."
            )
        self.region_a: list[Cell] = cells_a
        self.region_b: list[Cell] = cells_b

    def __repr__(self) -> str:
        """Provide a string representation of the ClonedRegion instance.

        Returns:
            str: A string representing the ClonedRegion.
        """
        return (
            f"{self.__class__.__name__}("
            f"{self.board!r}, "
            f"{self.region_a!r}, "
            f"{self.region_b!r}"
            f")"
        )

    @classmethod
    def extract(cls, board: Board, yaml: dict) -> tuple[list[Cell], list[Cell]]:
        """Extract two sets of cells from YAML configuration.

        Args:
            board (Board): The Sudoku board instance.
            yaml (dict): The YAML configuration containing cell coordinates.

        Returns:
            tuple[list[Cell], list[Cell]]: Two lists of cells representing the cloned regions.
        """
        part_a = str(yaml[cls.__name__].split('=')[0])
        part_b = str(yaml[cls.__name__].split('=')[1])
        cells_a = [Cell.make(board, int(rc.strip()[0]), int(rc.strip()[1])) for rc in part_a.split(',')]
        cells_b = [Cell.make(board, int(rc.strip()[0]), int(rc.strip()[1])) for rc in part_b.split(',')]
        return cells_a, cells_b

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create a ClonedRegion from YAML configuration.

        Args:
            board (Board): The Sudoku board instance.
            yaml (dict): The YAML configuration.

        Returns:
            Item: An instance of ClonedRegion.
        """
        cells_a, cells_b = ClonedRegion.extract(board, yaml)
        return ClonedRegion(board, cells_a, cells_b)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        return cls.create(board, yaml_data)

    def glyphs(self) -> list[Glyph]:
        """Retrieve the glyphs for the cloned region.

        Returns:
            list[Glyph]: An empty list, as this region has no specific glyphs.
        """
        return []

    @property
    def used_classes(self) -> set[Type[Item]]:
        """Retrieve the classes used in the cloned region.

        Returns:
            set[Type[Item]]: A set of item types used in the cloned region.
        """
        result = super().used_classes
        for item in self.region_a:
            result |= item.used_classes
        for item in self.region_b:
            result |= item.used_classes
        return result

    def walk(self) -> Iterator[Item]:
        """Walk through all items in the cloned region.

        Yields:
            Iterator[Item]: An iterator of items within the cloned region.
        """
        yield self
        for item in self.region_a:
            yield from item.walk()
        for item in self.region_b:
            yield from item.walk()

    @property
    def rules(self) -> list[Rule]:
        """Define the rule associated with the cloned region.

        Returns:
            list[Rule]: A list containing the rule for cloned regions.
        """
        return [
            Rule(
                "ClonedRegion",
                1,
                "The shaded areas are clones. They contain the same digits at the same locations."
            )
        ]

    @property
    def tags(self) -> set[str]:
        """Retrieve tags for the cloned region.

        Returns:
            set[str]: A set of tags, including 'ClonedRegion'.
        """
        return super().tags.union({'ClonedRegion'})

    # pylint: disable=loop-invariant-statement
    def add_constraint(self, solver: PulpSolver) -> None:
        """Add constraints to ensure cloned regions have the same values.

        Args:
            solver (PulpSolver): The solver to add constraints to.
        """
        for cell_1, cell_2 in zip(self.region_a, self.region_b):
            name = f"{self.__class__.__name__}_{cell_1.row}{cell_1.column}_{cell_2.row}{cell_2.column}"
            value_1 = solver.values[cell_1.row][cell_1.column]
            value_2 = solver.values[cell_2.row][cell_2.column]
            solver.model += value_1 == value_2, name

    def to_dict(self) -> dict:
        """Convert the cloned region to a dictionary representation.

        Returns:
            dict: A dictionary representation of the cloned region.
        """
        cell_str_a = ",".join([f"{cell.row}{cell.column}" for cell in self.region_a])
        cell_str_b = ",".join([f"{cell.row}{cell.column}" for cell in self.region_b])
        return {self.__class__.__name__: f"{cell_str_a}={cell_str_b}"}

    def css(self) -> dict:
        """Return the CSS styling for the cloned region glyphs.

        Returns:
            dict: A dictionary containing CSS styles for the cloned region.
        """
        return {
            '.ClonedRegion': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 2,
                'fill': 'black'
            },
            '.ClonedRegionForeground': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 1,
                'fill': 'black'
            },
            '.ClonedRegionBackground': {
                'font-size': '30px',
                'stroke': 'white',
                'stroke-width': 8,
                'fill': 'white',
                'font-weight': 'bolder'
            }
        }
