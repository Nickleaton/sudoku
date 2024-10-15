import re
from typing import List, Any, Dict, Callable

from src.glyphs.glyph import Glyph
from src.glyphs.battenburg_glyph import BattenburgGlyph
from src.items.board import Board
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.rule import Rule


class Battenburg(Item):

    def __init__(self, board: Board, position: Coord):
        super().__init__(board)
        self.position = position

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.position!r})"

    @property
    def rules(self) -> List[Rule]:
        return [Rule('Quadruple', 3, 'Digits appearing in at last one of the cells adjacent to the circle')]

    def glyphs(self) -> List[Glyph]:
        return [
            BattenburgGlyph(class_name="Battenburg", coord=self.position)
        ]

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Any:
        regex = re.compile(f"([{board.digit_values}])([{board.digit_values}])")
        match = regex.match(str(yaml[cls.__name__]))
        assert match is not None
        row_str, column_str = match.groups()
        return Coord(int(row_str), int(column_str))

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        position = Battenburg.extract(board, yaml)
        return cls(board, position)

    def add_constraint(self, solver: PulpSolver) -> None:
        offsets = [Coord(0, 0), Coord(0, 1), Coord(1, 0), Coord(1, 1)]

    def to_dict(self) -> Dict:
        """
        Convert the item to a dictionary for serialisation.

        The dictionary has a single key value pair where the key is the
        item's class name and the value is the row and column values of the
        item's position.

        Returns:
            Dict: A dictionary containing the item's class name and position.
        """
        return {self.__class__.__name__: self.position.row * 10 + self.position.column}
