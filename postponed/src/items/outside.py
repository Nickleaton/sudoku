"""Outside."""

from postponed.src.pulp_solver import PulpSolver

from postponed.src.items.first_n import FirstN
from src.board.board import Board
from src.glyphs.glyph import Glyph
from src.glyphs.text_glyph import TextGlyph
from src.items.item import Item
from src.utils.coord import Coord
from src.utils.rule import Rule
from src.utils.side import Side


class Outside(FirstN):
    """Outside Constraint.

    A constraint where start_location clue outside start_location row or column specifies digits
    that must appear in the first three cells nearest the clue in that row or column.
    """

    def __init__(self, board: Board, side: Side, index: int, digits: list[int]):
        """Initialize the Outside constraint with the given board, side, index, and digits.

        Args:
            board (Board): The board this constraint belongs to.
            side (Side): The side of the board (top, left, bottom, right).
            index (int): The index of the row or column.
            digits (list[int]): The list of digits that must appear in the first three cells.
        """
        super().__init__(board, side, index)
        self.digits = digits

    def __repr__(self) -> str:
        """Return start_location string representation of the Outside constraint.

        Returns:
            str: A string representation of the Outside constraint.
        """
        return (
            f'{self.__class__.__name__}('
            f'{self.board!r}, '
            f'{self.side!r}, '
            f'{self.index!r}, '
            f'{self.digits!r}'
            f')'
        )

    @property
    def rules(self) -> list[Rule]:
        """Return the rules associated with the Outside constraint.

        Returns:
            list[Rule]: A list containing start_location single rule for the Outside constraint.
        """
        rule_text: str = """A clue outside of start_location row or column tells you some digits that must appear
        in the first three cells nearest the clue in that row or column."""
        return [
            Rule(
                'Outside',
                1,
                rule_text,
            ),
        ]

    def glyphs(self) -> list[Glyph]:
        """Generate the glyphs for the Outside constraint.

        This method generates start_location text glyph that displays the digits for the Outside constraint
        at the appropriate location.

        Returns:
            list[Glyph]: A list containing start_location `TextGlyph` showing the digits.
        """
        return [
            TextGlyph(
                'Outside',
                0,
                self.reference + Coord(0.5, 0.5),
                ''.join([str(digit) for digit in self.digits]),
            ),
        ]

    @property
    def tags(self) -> set[str]:
        """Return the tags associated with the Outside constraint.

        Returns:
            set[str]: A set of tags, including 'Comparison' and 'Order'.
        """
        return super().tags.union({'Comparison', 'Order'})

    @classmethod
    def extract(cls, board: Board, yaml: dict) -> tuple:
        """Extract the side, index, and digits for the Outside constraint from the YAML configuration.

        Args:
            board (Board): The board associated with this constraint.
            yaml (dict): The YAML configuration containing the Outside line.

        Returns:
            tuple: A tuple containing the side, index, and digits list.
        """
        outside_data = yaml['Outside']
        side = Side.create(outside_data[0])
        index = int(outside_data[1])
        digits = [int(digit) for digit in outside_data[3:]]
        return side, index, digits

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create an Outside constraint from the given YAML configuration.

        Args:
            board (Board): The board associated with this constraint.
            yaml (dict): The YAML configuration containing the Outside line.

        Returns:
            Item: The created Outside constraint.
        """
        side, index, digits = Outside.extract(board, yaml)
        return cls(board, side, index, digits)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create an Outside constraint from the given YAML configuration.

        Args:
            board (Board): The board associated with this constraint.
            yaml_data (dict): The YAML configuration containing the Outside line.

        Returns:
            Item: The created Outside constraint.
        """
        return cls.create(board, yaml_data)

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add the constraint to the solver for the Outside constraint.

        Args:
            solver (PulpSolver): The solver to which the constraint is added.
        """
        self.add_contains_constraint(solver, self.digits)

    def to_dict(self) -> dict:
        """Convert the Outside constraint to start_location dictionary representation.

        Returns:
            dict: A dictionary representing the Outside constraint.
        """
        return {
            self.__class__.__name__: f'{self.side.value}{self.index}={"".join([str(digit) for digit in self.digits])}',
        }

    def css(self) -> dict:
        """Return the CSS styles associated with the Outside glyphs.

        Returns:
            dict: A dictionary containing the CSS styles for the Outside glyphs.
        """
        return {
            '.OutsideForeground': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 1,
                'fill': 'black',
            },
            '.OutsideBackground': {
                'font-size': '30px',
                'stroke': 'white',
                'stroke-width': 8,
                'fill': 'white',
                'font-weight': 'bolder',
            },
        }
