import re
from typing import List, Any, Dict, Optional

from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.multiplication import Multiplication
from src.items.region import Region
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord


class Product(Region):

    def __init__(self, board: Board, position: Coord, product: int):
        super().__init__(board)
        self.position = position
        self.product = product
        self.add_items(self.get_cells())

    # pylint: disable=no-self-use
    def get_cells(self) -> List[Cell]:
        return []

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.position!r}, {self.product})"

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Any:
        position_str, product = yaml[cls.__name__].split("=")
        position = Coord(int(position_str[0]), int(position_str[1]))
        return position, int(product)

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        position, product = cls.extract(board, yaml)
        return cls(board, position, product)

    def add_constraint(self, solver: PulpSolver) -> None:
        Multiplication.add_constraint(self.board, solver, self.cells, self.product, self.name)

    def to_dict(self) -> Dict:
        return {self.__class__.__name__: f"{self.position.row}{self.position.column}={self.product}"}
