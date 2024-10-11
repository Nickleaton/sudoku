from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class CreateMetaCommand(SimpleCommand):

    def __init__(self,
                 source: str = 'config',
                 target: str = 'meta'
                 ):

        """
        Initialize a CreateMetaCommand.

        :param source: The name of the config to get the metadata from.
            Defaults to 'config'.
        :param target: The name of the field to store the metadata in.
            Defaults to 'meta'.
        """
        super().__init__()
        self.source: str = source
        self.target: str = target

    def precondition_check(self, problem: Problem) -> None:
        """
        Check the preconditions for the command.

        :param problem: The problem to check
        :raises CommandException: If the preconditions are not met
        """
        if self.source not in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.source} not loaded')
        if self.target in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.target} already in problem')

    def execute(self, problem: Problem):
        """
        Create the field in the problem.

        Parameters:
            problem (Problem): The problem to create the field in.
        """
        super().execute(problem)
        problem[self.target] = problem[self.source]['Board']

    def __repr__(self) -> str:
        """
        Return a string representation of the object.

        Returns:
            str: A string representation of the object.
        """
        return f"{self.__class__.__name__}({repr(self.source)}, {repr(self.target)})"
