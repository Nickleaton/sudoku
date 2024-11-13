from typing import Dict, Type, List

from src.items.board import Board
from src.items.composed_item import ComposedItem
from src.items.item import Item


class Constraints(ComposedItem):
    """Represents a collection of constraints applied to a puzzle board."""

    def __init__(self, board: Board):
        """Initializes the Constraints with a reference to the board.

        Args:
            board (Board): The board to which these constraints apply.
        """
        super().__init__(board, [])
        self._n = 0  # This could represent the number of constraints or similar purpose

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> 'Constraints':
        """Creates a Constraints instance from YAML configuration.

        Args:
            board (Board): The board to which these constraints apply.
            yaml (Dict): A dictionary containing the YAML configuration for the constraints.

        Returns:
            Constraints: An instance of `Constraints` populated with the given configuration.
        """
        # Instantiate the Constraints object that will hold all parsed constraints
        result = cls(board)

        # Check if the current class name is a key in the YAML configuration
        # If not, skip processing as no relevant constraints are defined
        if cls.__name__ in yaml:
            # Extract the constraints data specific to this class from the YAML configuration
            parts: Dict | List = yaml[cls.__name__]

            # If `parts` is a dictionary, it represents a named set of constraints
            if isinstance(parts, dict):
                for key, value in parts.items():
                    # Each key corresponds to a specific constraint type (subclass of Item)
                    # Each value is a dictionary containing the constraint's configuration or `None`
                    sub_yaml: Dict = {} if value is None else value

                    # Retrieve the appropriate subclass from Item's registered classes
                    sub_class: Type[Item] = Item.classes[key]

                    # If the subclass is composite (contains other constraints),
                    # recursively create and add it as a composite constraint
                    if sub_class.is_composite():
                        result.add(sub_class.create(board, {key: sub_yaml}))

                    # If the subclass expects multiple constraints, represented as a list,
                    # create each item in the list as an individual constraint
                    elif isinstance(sub_yaml, list):
                        for data in sub_yaml:
                            # Create each constraint item and add it to the result
                            result.add(sub_class.create(board, {key: data}))

            # If `parts` is a list, it represents multiple instances of a single constraint type
            elif isinstance(parts, list):
                for data in parts:
                    # Use the generic Item class to create each constraint from the list
                    result.add(Item.create(board, data))

        # Return the populated Constraints instance
        return result
