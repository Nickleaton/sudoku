from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class CreateMetaCommand(SimpleCommand):

    def __init__(self, field_name: str):
        """
        Initialize a CreateMetaCommand object.

        Parameters:
            field_name (str): The name of the field to be created in the problem.
        """
        super().__init__()
        self.field_name: str = field_name

    def execute(self, problem: Problem):
        """
        Create the field in the problem.

        Parameters:
            problem (Problem): The problem to create the field in.
        """
        super().execute(problem)
        problem[self.field_name] = problem.config.Board

    def precondition_check(self, problem: Problem) -> None:
        """
        Check the preconditions for the command.

        :param problem: The problem to check
        :raises CommandException: If the preconditions are not met
        """
        if 'config' not in problem:
            raise CommandException('config')

    def __repr__(self) -> str:
        """
        Return a string representation of the object.

        Returns:
            str: A string representation of the object.
        """
        return f"{self.__class__.__name__}('{self.field_name}')"
