from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class CreateRulesCommand(SimpleCommand):

    def __init__(self,
                 constraints: str = 'constraints',
                 target: str = 'rules'):
        """
        Initialize a CreateRulesCommand object.

        Parameters:
            constraints (str): The name of the field in the problem
                containing the constraints to generate rules from.
            target (str): The name of the field in the problem that
                this command will create.
        """
        super().__init__()
        self.constraints: str = constraints
        self.target: str = target

    def precondition_check(self, problem: Problem) -> None:
        """
        Check the preconditions for the command.

        :param problem: The problem to check
        :raises CommandException: If the preconditions are not met
        """
        if self.constraints not in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.constraints} not loaded')
        if self.target in problem:
            raise CommandException(f'{self.__class__.__name__} - {self.target} already in problem')

    def execute(self, problem: Problem) -> None:
        """
        Create a list of rules in the problem.

        The rules are determined by recursively traversing the item tree and
        calling the `rules` property on each item. The resulting list of rules
        is de-duplicated and sorted in order. The rules are stored in the
        problem in the field specified by `target`.

        Parameters:
            problem (Problem): The problem to generate the rules for.

        Returns:
            None
        """
        problem.rules = [
            {'name': rule.name, 'text': rule.text}
            for rule in problem[self.constraints].sorted_unique_rules
        ]

    def __repr__(self) -> str:
        """
        Return a string representation of the object.

        Returns:
            str: A string representation of the object.
        """
        return f"{self.__class__.__name__}({self.constraints!r}, {self.target!r})"
