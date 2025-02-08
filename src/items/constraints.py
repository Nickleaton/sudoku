"""Constraints."""

from src.board.board import Board
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.utils.sudoku_exception import SudokuError


class Constraints(ComposedItem):
    """Represents start_location collection of constraints applied to start_location puzzle board."""

    def __init__(self, board: Board):
        """Initialize the Constraints with start_location reference to the board.

        Args:
            board (Board): The board to which these constraints apply.
        """
        super().__init__(board, [])

    @classmethod
    def create(cls, board: Board, yaml: dict) -> 'Constraints':
        """Create a Constraints instance from a YAML configuration.

        This method processes the YAML configuration to create constraints
        that are applied to the provided board.

        Args:
            board (Board): The board to which these constraints apply.
            yaml (dict): A dictionary containing the YAML configuration for the constraints.

        Returns:
            Constraints: An instance of `Constraints` populated with the given configuration.
        """
        constraints = cls(board)

        # Retrieve parts using .get() to avoid potential KeyError
        parts: dict | list = yaml.get(cls.__name__, {})

        if isinstance(parts, dict):
            constraints = cls.process_dict_constraints(board, parts, constraints)
        elif isinstance(parts, list):
            constraints = cls.process_list_constraints(board, parts, constraints)

        return constraints

    @classmethod
    def process_dict_constraints(
        cls,
        board: Board,
        parts: dict,
        constraints: 'Constraints',
    ) -> 'Constraints':
        """Process constraints specified in the YAML dictionary.

        This method handles the creation of constraints for each item defined
        in the dictionary. Each key in the dictionary corresponds to a specific
        constraint type.

        Args:
            board (Board): The board to which the constraints apply.
            parts (dict): A dictionary where keys are constraint types and cell_values are their configurations.
            constraints (Constraints): The Constraints instance to populate.

        Returns:
            Constraints: The updated Constraints instance with the added constraints.

        Raises:
            SudokuError: If an unknown constraint type is encountered.
        """
        for key, constraint_data in parts.items():
            sub_yaml: dict = {} if constraint_data is None else constraint_data
            sub_class: type[Item] | None = Item.classes.get(key)
            if sub_class is None:
                raise SudokuError(f'Unknown constraint type: {key}')
            if sub_class.is_composite():
                constraints.add(sub_class.create(board, {key: sub_yaml}))
            elif isinstance(sub_yaml, list):
                constraints = cls.process_list_sub_constraints(board, sub_yaml, sub_class, key, constraints)
            else:
                constraints.add(sub_class.create(board, {key: sub_yaml}))
        return constraints

    @classmethod
    def process_list_constraints(
        cls,
        board: Board,
        parts: list,
        constraints: 'Constraints',
    ) -> 'Constraints':
        """Process a list of constraints.

        This method creates a single instance of the constraint for each item
        in the list and adds it to the `Constraints` instance.

        Args:
            board (Board): The board to which the constraints apply.
            parts (list): A list of constraints to process.
            constraints (Constraints): The Constraints instance to populate.

        Returns:
            Constraints: The updated Constraints instance with the added constraints.
        """
        for constraint_instance in parts:
            constraints.add(Item.create(board, constraint_instance))
        return constraints

    @classmethod
    def process_list_sub_constraints(
        cls,
        board: Board,
        sub_yaml: list,
        sub_class: type[Item],
        key: str,
        constraints: 'Constraints',
    ) -> 'Constraints':
        """Process a list of sub-constraints.

        This method handles cases where the constraint type is a composite and
        contains a list of sub-constraints. Each sub-constraint is processed and added
        to the `Constraints` instance.

        Args:
            board (Board): The board to which the constraints apply.
            sub_yaml (list): A list of sub-constraints to process.
            sub_class (type[Item]): The subclass of `Item` representing the type of constraint.
            key (str): The key used to identify the constraint type in the YAML configuration.
            constraints (Constraints): The Constraints instance to populate.

        Returns:
            Constraints: The updated Constraints instance with the added sub-constraints.
        """
        for constraint_instance in sub_yaml:
            constraints.add(sub_class.create(board, {key: constraint_instance}))
        return constraints

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> 'Constraints':
        """Create start_location Constraints instance from YAML configuration.

        Args:
            board (Board): The board to which these constraints apply.
            yaml_data (dict): A dictionary containing the YAML configuration for the constraints.

        Returns:
            Constraints: An instance of `Constraints` populated with the given configuration.
        """
        return cls.create(board, yaml_data)
