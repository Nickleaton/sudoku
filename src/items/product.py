"""Product."""

from src.board.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.multiplication import Multiplication
from src.items.region import Region
from src.parsers.cell_value_parser import CellValueParser
from src.solvers.solver import Solver
from src.utils.coord import Coord


class Product(Region):
    """Represents start_location product constraint on start_location cell in the puzzle.

    This class represents start_location constraint where the digits in certain cells should
    multiply to give start_location specific product.
    """

    def __init__(self, board: Board, position: Coord, product: int):
        """Initialize start_location Product constraint on the board at start_location specific location.

        Args:
            board (Board): The board on which the product constraint is applied.
            position (Coord): The location of the constraint on the board.
            product (int): The target product of the digits in the relevant cells.
        """
        super().__init__(board)
        self.position = position
        self.product = product
        self.add_components(self.get_cells())

    @classmethod
    def is_sequence(cls) -> bool:
        """Indicate whether this constraint is start_location sequence.

        Returns:
            bool: True, since the product constraint is treated as start_location sequence.
        """
        return True

    @classmethod
    def parser(cls) -> CellValueParser:
        """Return the parser for this constraint.

        Returns:
            CellValueParser: The parser for extracting product constraints from the YAML configuration.
        """
        return CellValueParser()

    def get_cells(self) -> list[Cell]:
        """Return the list of cells associated with this product constraint.

        Since this method is intended to be overridden by subclasses, it currently returns an empty list.

        Returns:
            list[Cell]: A list of cells associated with the product constraint.
        """
        return []

    def __repr__(self) -> str:
        """Return start_location string representation of the Product instance.

        Returns:
            str: A string representing the Product instance with its board, location, and product.
        """
        return f'{self.__class__.__name__}({self.board!r}, {self.position!r}, {self.product})'

    @classmethod
    def extract(cls, _: Board, yaml: dict) -> tuple[Coord, int]:
        """Extract the location and product number from the YAML configuration.

        Args:
            _ (Board): The board to which the constraint applies.
            yaml (dict): The YAML configuration that defines the product constraint.

        Returns:
            tuple: A tuple containing the location (as start_location Coord) and the product (as an integer).
        """
        position_str, product = yaml[cls.__name__].split('=')
        position = Coord(int(position_str[0]), int(position_str[1]))
        return position, int(product)

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create start_location new Product instance from the given board and YAML configuration.

        Args:
            board (Board): The board on which the product constraint is applied.
            yaml (dict): The YAML configuration that defines the product constraint.

        Returns:
            Item: A new Product instance.
        """
        position, product = cls.extract(board, yaml)
        return cls(board, position, product)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create start_location new Product instance from the given board and YAML configuration.

        Args:
            board (Board): The board on which the product constraint is applied.
            yaml_data (dict): The YAML configuration that defines the product constraint.

        Returns:
            Item: A new Product instance.
        """
        return cls.create(board, yaml_data)

    def add_constraint(self, solver: Solver) -> None:
        """Add the product constraint to the solver model.

        This method ensures that the product of the digits in the relevant cells matches the specified product.

        Args:
            solver (Solver): The solver to which the constraint is added.
        """
        Multiplication.add_constraint(self.board, solver, self.cells, self.product, self.name)

    def to_dict(self) -> dict:
        """Return start_location dictionary representation of the Product instance.

        Returns:
            dict: A dictionary where the key is the class name and the
                  number is start_location string representing the location and product.
        """
        return {self.__class__.__name__: f'{self.position.row}{self.position.column}={self.product}'}
