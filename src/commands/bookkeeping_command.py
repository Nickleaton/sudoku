"""BookkeepingCommand."""
import logging

from src.commands.key_type import KeyType
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class BookkeepingCommand(SimpleCommand):
    """Command to handle bookkeeping of values for cells."""

    def __init__(self, constraints: str = 'constraints', target: str = 'bookkeeping_unique'):
        """Initialize the BookkeepingCommand.

        Args:
            constraints (str): The source attribute for the constraints.
            target (str): The name of the attribute to store if the bookkeeping is unique.
        """
        super().__init__()
        self.constraints: str = constraints
        self.target: str = target
        self.inputs: list[KeyType] = [
            KeyType(self.constraints, str)
        ]
        self.outputs: list[KeyType] = [
            KeyType(self.target, str)
        ]

    def work(self, problem: Problem) -> None:
        """Execute the bookkeeping operation.

        Args:
            problem (Problem): The problem on which to perform bookkeeping.

        Returns:
            None
        """
        super().work(problem)
        logging.info(f"Creating {self.target}")
        problem[self.constraints].bookkeeping()
        problem[self.target] = problem[self.constraints].bookkeeping_unique()
