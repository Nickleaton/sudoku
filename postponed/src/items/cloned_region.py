"""ClonedRegion."""
from collections.abc import Iterator
from typing import Type

from postponed.src.pulp_solver import PulpSolver

from src.board.board import Board
from src.glyphs.glyph import Glyph
from src.items.cell import Cell
from src.items.item import Item
from src.utils.rule import Rule
from src.utils.sudoku_exception import SudokuError


class ClonedRegion(Item):
    """Represents a cloned region constraint in a Sudoku variant."""

    def __init__(self, board: Board, cells_a: list[Cell], cells_b: list[Cell]) -> None:
        """Initialize ClonedRegion with two sets of cells that must have the same cell_values.

        Args:
            board (Board): The Sudoku board instance.
            cells_a (list[Cell]): The first set of cells in the cloned region.
            cells_b (list[Cell]): The second set of cells in the cloned region.

        Raises:
            SudokuError: If the length of `cells_a` does not match the length of `cells_b`.
        """
        super().__init__(board)
        if len(cells_a) != len(cells_b):
            raise SudokuError(
                f'Length mismatch: cells_a has {len(cells_a)} elements, but cells_b has {len(cells_b)} elements.',
            )
        self.region_a: list[Cell] = cells_a
        self.region_b: list[Cell] = cells_b

    def __repr__(self) -> str:
        """Provide string representation of the ClonedRegion instance.

        Returns:
            str: A string representing the ClonedRegion.
        """
        return (
            f'{self.__class__.__name__}('
            f'{self.board!r}, '
            f'{self.region_a!r}, '
            f'{self.region_b!r})'
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
        """Alternative method to create a ClonedRegion from YAML line.

        Args:
            board (Board): The Sudoku board instance.
            yaml_data (dict): The YAML line.

        Returns:
            Item: An instance of ClonedRegion.
        """
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
            set[Type[Item]]: A set of constraint types used in the cloned region.
        """
        used_classes_set = super().used_classes
        for cell_a in self.region_a:
            used_classes_set |= cell_a.used_classes
        for cell_b in self.region_b:
            used_classes_set |= cell_b.used_classes
        return used_classes_set

    def walk(self) -> Iterator[Item]:
        """Walk through all vectors in the cloned region.

        Yields:
            Iterator[Item]: An iterator of vectors within the cloned region.
        """
        yield self
        for cell_a in self.region_a:
            yield from cell_a.walk()
        for cell_b in self.region_b:
            yield from cell_b.walk()

    @property
    def rules(self) -> list[Rule]:
        """Define the rule associated with the cloned region.

        Returns:
            list[Rule]: A list containing the rule for cloned regions.
        """
        rule_description: str = (
            'The shaded areas are clones. They contain the same digits at the same locations.'
        )
        return [Rule('ClonedRegion', 1, rule_description)]

    @property
    def tags(self) -> set[str]:
        """Retrieve tags for the cloned region.

        Returns:
            set[str]: A set of tags, including 'ClonedRegion'.
        """
        return super().tags.union({'ClonedRegion'})

    # pylint: disable=loop-invariant-statement
    def add_constraint(self, solver: PulpSolver) -> None:
        """Add constraints to ensure cloned regions have the same target_value.

        Args:
            solver (PulpSolver): The solver to add constraints to.
        """
        for first_cell, second_cell in zip(self.region_a, self.region_b):
            first_str: str = f'{first_cell.row}{first_cell.column}'
            second_str: str = f'{second_cell.row}{second_cell.column}'
            constraint_name: str = f'{self.__class__.__name__}_{first_str}_{second_str}'
            value_first = solver.variables.numbers[first_cell.row][first_cell.column]
            value_second = solver.variables.numbers[second_cell.row][second_cell.column]
            solver.model += value_first == value_second, constraint_name

    def to_dict(self) -> dict:
        """Convert the cloned region to a dictionary representation.

        Returns:
            dict: A dictionary representation of the cloned region.
        """
        cell_str_a: str = ','.join([f'{cell.row}{cell.column}' for cell in self.region_a])
        cell_str_b: str = ','.join([f'{cell.row}{cell.column}' for cell in self.region_b])
        return {self.__class__.__name__: f'{cell_str_a}={cell_str_b}'}

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
                'fill': 'black',
            },
            '.ClonedRegionForeground': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 1,
                'fill': 'black',
            },
            '.ClonedRegionBackground': {
                'font-size': '30px',
                'stroke': 'white',
                'stroke-width': 8,
                'fill': 'white',
                'font-weight': 'bolder',
            },
        }
