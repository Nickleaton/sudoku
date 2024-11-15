"""Product."""
from typing import List, Any, Dict

from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.multiplication import Multiplication
from src.items.region import Region
from src.parsers.cell_value_parser import CellValueParser
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord


class Product(Region):
    """Represents a product constraint on a cell in the puzzle.

    This class represents a constraint where the digits in certain cells should multiply to give a specific product.
    """

    def __init__(self, board: Board, position: Coord, product: int):
        """Initialize a Product constraint on the board at a specific position.

        Args:
            board (Board): The board on which the product constraint is applied.
            position (Coord): The position of the constraint on the board.
            product (int): The target product of the digits in the relevant cells.
        """
        super().__init__(board)
        self.position = position
        self.product = product
        self.add_items(self.get_cells())

    @classmethod
    def is_sequence(cls) -> bool:
        """Indicate whether this item is a sequence.

        Returns:
            bool: True, since the product constraint is treated as a sequence.
        """
        return True

    @classmethod
    def parser(cls) -> CellValueParser:
        """Return the parser for this item.

        Returns:
            CellValueParser: The parser for extracting product constraints from the YAML configuration.
        """
        return CellValueParser()

    def get_cells(self) -> List[Cell]:
        """Return the list of cells associated with this product constraint.

        Since this method is intended to be overridden by subclasses, it currently returns an empty list.

        Returns:
            List[Cell]: A list of cells associated with the product constraint.
        """
        return []

    def __repr__(self) -> str:
        """Return a string representation of the Product instance.

        Returns:
            str: A string representing the Product instance with its board, position, and product.
        """
        return f"{self.__class__.__name__}({self.board!r}, {self.position!r}, {self.product})"

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Any:
        """Extract the position and product value from the YAML configuration.

        Args:
            board (Board): The board to which the constraint applies.
            yaml (Dict): The YAML configuration that defines the product constraint.

        Returns:
            tuple: A tuple containing the position (as a Coord) and the product (as an integer).
        """
        position_str, product = yaml[cls.__name__].split("=")
        position = Coord(int(position_str[0]), int(position_str[1]))
        return position, int(product)

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        """Create a new Product instance from the given board and YAML configuration.

        Args:
            board (Board): The board on which the product constraint is applied.
            yaml (Dict): The YAML configuration that defines the product constraint.

        Returns:
            Item: A new Product instance.
        """
        position, product = cls.extract(board, yaml)
        return cls(board, position, product)

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add the product constraint to the solver model.

        This method ensures that the product of the digits in the relevant cells matches the specified product.

        Args:
            solver (PulpSolver): The solver to which the constraint is added.
        """
        Multiplication.add_constraint(self.board, solver, self.cells, self.product, self.name)

    def to_dict(self) -> Dict:
        """Return a dictionary representation of the Product instance.

        Returns:
            Dict: A dictionary where the key is the class name and the
                  value is a string representing the position and product.
        """
        return {self.__class__.__name__: f"{self.position.row}{self.position.column}={self.product}"}

