"""CreateMetaCommand."""
import logging

import pydotted

from src.commands.key_type import KeyType
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class CreateMetaCommand(SimpleCommand):
    """Command for creating a metadata field in the problem instance."""

    def __init__(self, source: str = 'config', target: str = 'meta'):
        """Initialize a CreateMetaCommand instance.

        Args:
            source (str): The attribute in the problem containing the configuration data. Defaults to 'config'.
            target (str): The attribute name in the problem where metadata will be stored. Defaults to 'meta'.
        """
        super().__init__()
        self.source: str = source
        self.target: str = target
        self.input_types: list[KeyType] = [
            KeyType(source, pydotted.pydot)
        ]
        self.output_types: list[KeyType] = [
            KeyType(target, pydotted.pydot)
        ]

    def work(self, problem: Problem) -> None:
        """Create the metadata field in the problem.

        Logs a message indicating that the command is being processed and creates a new
        metadata field in the problem, storing it in the specified target attribute.

        Args:
            problem (Problem): The problem instance to create the metadata in.
        """
        super().work(problem)
        logging.info(f"Creating {self.target}")
        problem[self.target] = problem[self.source]['Board']
