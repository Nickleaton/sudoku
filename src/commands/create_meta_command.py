import logging

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class CreateMetaCommand(SimpleCommand):
    """
    Command for creating a metadata field in the problem instance.
    """

    def __init__(self, source: str = 'config', target: str = 'meta'):
        """
        Initializes a CreateMetaCommand instance.

        Args:
            source (str): The attribute in the problem containing the configuration data. Defaults to 'config'.
            target (str): The attribute name in the problem where metadata will be stored. Defaults to 'meta'.
        """
        super().__init__()
        self.source: str = source
        self.target: str = target

    def precondition_check(self, problem: Problem) -> None:
        """
        Checks preconditions for command execution.

        Ensures that the source attribute exists in the problem and the target attribute
        does not already exist.

        Args:
            problem (Problem): The problem instance to check.

        Raises:
            CommandException: If the source attribute is missing or the target attribute
                              already exists in the problem.
        """
        if self.source not in problem:
            raise CommandException(f"{self.__class__.__name__} - {self.source} not loaded")
        if self.target in problem:
            raise CommandException(f"{self.__class__.__name__} - {self.target} already in problem")

    def execute(self, problem: Problem) -> None:
        """
        Creates the metadata field in the problem.

        Logs a message indicating that the command is being processed and creates a new
        metadata field in the problem, storing it in the specified target attribute.

        Args:
            problem (Problem): The problem instance to create the metadata in.
        """
        super().execute(problem)
        logging.info(f"Creating {self.target}")
        problem[self.target] = problem[self.source]['Board']

    def __repr__(self) -> str:
        """
        Returns a string representation of the CreateMetaCommand instance.

        Returns:
            str: A string representation of the object.
        """
        return f"{self.__class__.__name__}({self.source!r}, {self.target!r})"
