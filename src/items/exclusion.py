"""Exclusion."""
from typing import Any

from pulp import lpSum

from src.glyphs.glyph import Glyph
from src.glyphs.quadruple_glyph import QuadrupleGlyph
from src.items.board import Board
from src.items.item import Item
from src.parsers.cell_value_parser import CellValueParser
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.rule import Rule


class Exclusion(Item):
    """Represents an exclusion constraint where certain digits cannot appear in the cells adjacent to a circle."""

    def __init__(self, board: Board, position: Coord, digits: str):
        """Initialize an Exclusion item.

        Args:
            board (Board): The board on which the exclusion applies.
            position (Coord): The position of the circle in the grid.
            digits (str): The digits that cannot appear in adjacent cells.
        """
        super().__init__(board)
        self.position = position
        self.digits = digits
        self.numbers = "".join([str(d) for d in digits])

    @classmethod
    def is_sequence(cls) -> bool:
        """Indicate if the exclusion is a sequence.

        Returns:
            bool: True, since an exclusion is considered a sequence.
        """
        return True

    @classmethod
    def parser(cls) -> CellValueParser:
        """Return the parser for this item.

        Returns:
            CellValueParser: The parser for extracting Exclusion values.
        """
        return CellValueParser()

    def __repr__(self) -> str:
        """Return a string representation of the Exclusion object.

        Returns:
            str: The string representation of the Exclusion object.
        """
        digit_str = "".join([str(digit) for digit in self.digits])
        return f"{self.__class__.__name__}({self.board!r}, {self.position!r}, '{digit_str}')"

    @property
    def rules(self) -> list[Rule]:
        """Return the rules associated with the Exclusion item.

        Returns:
            list[Rule]: A list of rules for the Exclusion constraint.
        """
        return [Rule('Exclusion', 3, 'Digit(s) cannot appear in the cells adjacent to the circle')]

    def glyphs(self) -> list[Glyph]:
        """Return the glyph for visual representation of the Exclusion item.

        Returns:
            list[Glyph]: A list containing a QuadrupleGlyph representing the Exclusion circle.
        """
        return [
            QuadrupleGlyph(class_name="Exclusion", position=self.position, numbers=self.numbers)
        ]

    @classmethod
    def extract(cls, board: Board, yaml: dict) -> Any:
        """Extract the position and digits from the YAML configuration.

        Args:
            board (Board): The board the item applies to.
            yaml (dict): The YAML data containing the Exclusion definition.

        Returns:
            tuple[Coord, str]: A tuple containing the position (as Coord) and the digits as a string.
        """
        position_str, digits = yaml[cls.__name__].split("=")
        position = Coord(int(position_str[0]), int(position_str[1]))
        return position, digits

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create an Exclusion item from the YAML data.

        Args:
            board (Board): The board the item applies to.
            yaml (dict): The YAML data containing the Exclusion definition.

        Returns:
            Item: An Exclusion item created from the YAML data.
        """
        position, numbers = Exclusion.extract(board, yaml)
        return cls(board, position, numbers)

    # pylint: disable=loop-invariant-statement
    def add_constraint(self, solver: PulpSolver) -> None:
        """Add the exclusion constraint to the solver.

        For each digit, ensures it does not appear in any adjacent cells to the specified position.

        Args:
            solver (PulpSolver): The solver to which the constraint is added.
        """
        offsets = (
            Coord(0, 0),
            Coord(0, 1),
            Coord(1, 0),
            Coord(1, 1)
        )
        for digit in self.digits:
            digit_sum = lpSum(
                [
                    solver.choices[int(digit)][(self.position + offset).row][(self.position + offset).column]
                    for offset in offsets
                ]
            )
            solver.model += digit_sum == 0, f"{self.name}_{digit}"

    def to_dict(self) -> dict:
        """Convert the Exclusion item to a dictionary representation.

        Returns:
            dict: A dictionary representing the Exclusion item in YAML format.
        """
        return {self.__class__.__name__: f"{self.position.row}{self.position.column}={''.join(self.digits)}"}

    def css(self) -> dict:
        """Return the CSS styles for visual rendering of the Exclusion circle.

        Returns:
            dict: A dictionary containing CSS styles for the Exclusion circle and its digits.
        """
        return {
            ".ExclusionCircle": {
                "stroke-width": 2,
                "stroke": "black",
                "fill": "white"
            },
            ".ExclusionText": {
                "stroke": "black",
                "fill": "black",
                "font-size": "30px"
            }
        }
