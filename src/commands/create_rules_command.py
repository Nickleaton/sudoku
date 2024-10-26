import logging

from src.commands.command import CommandException
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class CreateRulesCommand(SimpleCommand):
    """
    Command for creating a list of rules in the problem instance.
    """

    def __init__(self, constraints: str = 'constraints', target: str = 'rules'):
        """
        Initializes a CreateRulesCommand instance.

        Args:
            constraints (str): The attribute in the problem containing constraints used to generate rules.
            target (str): The attribute name in the problem where the generated rules will be stored.
        """
        super().__init__()
        self.constraints: str = constraints
        self.target: str = target

    def precondition_check(self, problem: Problem) -> None:
        """
        Checks preconditions for command execution.

        Ensures that the constraints attribute exists in the problem and the target attribute
        does not already exist.

        Args:
            problem (Problem): The problem instance to check.

        Raises:
            CommandException: If the constraints attribute is missing or the target attribute
                              already exists in the problem.
        """
        if self.constraints not in problem:
            raise CommandException(f"{self.__class__.__name__} - {self.constraints} not loaded")
        if self.target in problem:
            raise CommandException(f"{self.__class__.__name__} - {self.target} already in problem")

    def execute(self, problem: Problem) -> None:
        """
        Creates a list of rules in the problem instance.

        This function generates rules by traversing the item tree and calling the `rules`
        property on each item in the constraints attribute. The rules are then de-duplicated,
        sorted, and stored in the target attribute within the problem instance.

        Args:
            problem (Problem): The problem instance where the rules will be created.
        """
        super().execute(problem)
        logging.info(f"Creating {self.target}")
        problem[self.target] = [
            {'name': rule.name, 'text': rule.text}
            for rule in problem[self.constraints].sorted_unique_rules
        ]

    def __repr__(self) -> str:
        """
        Returns a string representation of the CreateRulesCommand instance.

        Returns:
            str: A string representation of the object.
        """
        return f"{self.__class__.__name__}({self.constraints!r}, {self.target!r})"
