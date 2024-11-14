from typing import List, Any, Dict

from src.glyphs.glyph import Glyph
from src.glyphs.text_glyph import TextGlyph
from src.items.board import Board
from src.items.first_n import FirstN
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.rule import Rule
from src.utils.side import Side


class Outside(FirstN):
    """Represents a constraint where a clue outside a row or column specifies digits
    that must appear in the first three cells nearest the clue in that row or column.
    """

    def __init__(self, board: Board, side: Side, index: int, digits: List[int]):
        """Initializes the Outside item with the given board, side, index, and digits.

        Args:
            board (Board): The board this item belongs to.
            side (Side): The side of the board (top, left, bottom, right).
            index (int): The index of the row or column.
            digits (List[int]): The list of digits that must appear in the first three cells.
        """
        super().__init__(board, side, index)
        self.digits = digits

    def __repr__(self) -> str:
        """Returns a string representation of the Outside item.

        Returns:
            str: A string representation of the Outside item.
        """
        return (
            f"{self.__class__.__name__}("
            f"{self.board!r}, "
            f"{self.side!r}, "
            f"{self.index!r}, "
            f"{self.digits!r}"
            f")"
        )

    @property
    def rules(self) -> List[Rule]:
        """Returns the rules associated with the Outside constraint.

        Returns:
            List[Rule]: A list containing a single rule for the Outside constraint.
        """
        return [
            Rule(
                'Outside',
                1,
                "A clue outside of a row or column tells you some digits that must appear "
                "in the first three cells nearest the clue in that row or column."
            )
        ]

    def glyphs(self) -> List[Glyph]:
        """Generates the glyphs for the Outside constraint.

        This method generates a text glyph that displays the digits for the Outside constraint
        at the appropriate position.

        Returns:
            List[Glyph]: A list containing a `TextGlyph` showing the digits.
        """
        return [
            TextGlyph('Outside', 0, self.reference + Coord(0.5, 0.5), "".join([str(digit) for digit in self.digits]))
        ]

    @property
    def tags(self) -> set[str]:
        """Returns the tags associated with the Outside item.

        Returns:
            set[str]: A set of tags, including 'Comparison' and 'Order'.
        """
        return super().tags.union({'Comparison', 'Order'})

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Any:
        """Extracts the side, index, and digits for the Outside constraint from the YAML configuration.

        Args:
            board (Board): The board associated with this item.
            yaml (Dict): The YAML configuration containing the Outside data.

        Returns:
            Tuple: A tuple containing the side, index, and digits list.
        """
        data = yaml['Outside']
        side = Side.create(data[0])
        index = int(data[1])
        digits = [int(digit) for digit in data[3:]]
        return side, index, digits

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        """Creates an Outside item from the given YAML configuration.

        Args:
            board (Board): The board associated with this item.
            yaml (Dict): The YAML configuration containing the Outside data.

        Returns:
            Item: The created Outside item.
        """
        side, index, digits = Outside.extract(board, yaml)
        return cls(board, side, index, digits)

    def add_constraint(self, solver: PulpSolver) -> None:
        """Adds the constraint to the solver for the Outside item.

        Args:
            solver (PulpSolver): The solver to which the constraint is added.
        """
        self.add_contains_constraint(solver, self.digits)

    def to_dict(self) -> Dict:
        """Converts the Outside item to a dictionary representation.

        Returns:
            Dict: A dictionary representing the Outside item.
        """
        return {self.__class__.__name__: f"{self.side.value}{self.index}={''.join([str(d) for d in self.digits])}"}

    def css(self) -> Dict:
        """Returns the CSS styles associated with the Outside glyphs.

        Returns:
            Dict: A dictionary containing the CSS styles for the Outside glyphs.
        """
        return {
            ".OutsideForeground": {
                "font-size": "30px",
                "stroke": "black",
                "stroke-width": 1,
                "fill": "black"
            },
            ".OutsideBackground": {
                "font-size": "30px",
                "stroke": "white",
                "stroke-width": 8,
                "fill": "white",
                "font-weight": "bolder"
            }
        }
