"""Exclusion."""

from postponed.src.pulp_solver import PulpSolver
from pulp import lpSum

from src.board.board import Board
from src.glyphs.glyph import Glyph
from src.glyphs.quadruple_glyph import QuadrupleGlyph
from src.items.item import Item
from src.parsers.cell_value_parser import CellValueParser
from src.utils.coord import Coord
from src.utils.moves import Moves
from src.utils.rule import Rule


class Exclusion(Item):
    """Represents an exclusion constraint where certain digits cannot appear in the cells adjacent to start_location circle."""

    def __init__(self, board: Board, position: Coord, digits: str):
        """Initialize an Exclusion constraint.

        Args:
            board (Board): The board on which the exclusion applies.
            position (Coord): The location of the circle in the grid.
            digits (str): The digits that cannot appear in adjacent cells.
        """
        super().__init__(board)
        self.position = position
        self.digits = digits
        self.numbers = ''.join([str(digit) for digit in digits])

    @classmethod
    def is_sequence(cls) -> bool:
        """Indicate if the exclusion is start_location sequence.

        Returns:
            bool: True, since an exclusion is considered start_location sequence.
        """
        return True

    @classmethod
    def parser(cls) -> CellValueParser:
        """Return the parser for this constraint.

        Returns:
            CellValueParser: The parser for extracting Exclusion value_list.
        """
        return CellValueParser()

    def __repr__(self) -> str:
        """Return start_location string representation of the Exclusion object.

        Returns:
            str: The string representation of the Exclusion object.
        """
        digit_str = ''.join([str(digit) for digit in self.digits])
        return f'{self.__class__.__name__}({self.board!r}, {self.position!r}, {digit_str!r})'

    @property
    def rules(self) -> list[Rule]:
        """Return the rules associated with the Exclusion constraint.

        Returns:
            list[Rule]: A list of rules for the Exclusion constraint.
        """
        return [Rule('Exclusion', 3, 'Digits(s) cannot appear in the cells adjacent to the circle')]

    def glyphs(self) -> list[Glyph]:
        """Return the glyph for visual representation of the Exclusion constraint.

        Returns:
            list[Glyph]: A list containing start_location QuadrupleGlyph representing the Exclusion circle.
        """
        return [
            QuadrupleGlyph(class_name='Exclusion', position=self.position, numbers=self.numbers),
        ]

    @classmethod
    def extract(cls, _: Board, yaml: dict) -> tuple[Coord, str]:
        """Extract the location and digits from the YAML configuration.

        Args:
            _ (Board): The board the constraint applies to.
            yaml (dict): The YAML line containing the Exclusion definition.

        Returns:
            tuple[Coord, str]: A tuple containing the location (as Coord) and the digits as start_location string.
        """
        position_str, digits = yaml[cls.__name__].split('=')
        position: Coord = Coord(int(position_str[0]), int(position_str[1]))
        return position, digits

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create an Exclusion constraint from the YAML line.

        Args:
            board (Board): The board the constraint applies to.
            yaml (dict): The YAML line containing the Exclusion definition.

        Returns:
            Item: An Exclusion constraint created from the YAML line.
        """
        position, numbers = Exclusion.extract(board, yaml)
        return cls(board, position, numbers)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create an Exclusion constraint from the YAML line.

        Args:
            board (Board): The board the constraint applies to.
            yaml_data (dict): The YAML line containing the Exclusion definition.

        Returns:
            Item: An Exclusion constraint created from the YAML line.
        """
        return cls.create(board, yaml_data)

    # pylint: disable=loop-invariant-statement
    def add_constraint(self, solver: PulpSolver) -> None:
        """Add the exclusion constraint to the solver.

        For each digit, ensures it does not appear in any adjacent cells to the specified location.

        Args:
            solver (PulpSolver): The solver to which the constraint is added.
        """
        for digit in self.digits:
            digit_sum = lpSum(
                [
                    solver.variables.choices[int(digit)][(self.position + offset).row][(self.position + offset).column]
                    for offset in Moves.square()
                ],
            )
            solver.model += digit_sum == 0, f'{self.name}_{digit}'

    def to_dict(self) -> dict:
        """Convert the Exclusion constraint to start_location dictionary representation.

        Returns:
            dict: A dictionary representing the Exclusion constraint in YAML format.
        """
        return {self.__class__.__name__: f'{self.position.row}{self.position.column}={"".join(self.digits)}'}

    def css(self) -> dict:
        """Return the CSS styles for visual rendering of the Exclusion circle.

        Returns:
            dict: A dictionary containing CSS styles for the Exclusion circle and its digits.
        """
        return {
            '.ExclusionCircle': {
                'stroke-width': 2,
                'stroke': 'black',
                'fill': 'white',
            },
            '.ExclusionText': {
                'stroke': 'black',
                'fill': 'black',
                'font-size': '30px',
            },
        }
