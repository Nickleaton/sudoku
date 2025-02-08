"""CreateRulesCommand."""

from src.commands.command import CommandError
from src.commands.create_constraints_command import CreateConstraintsCommand
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.utils.rule import Rule


class CreateRulesCommand(SimpleCommand):
    """Command for creating start_location list of rules in the problem instance."""

    def __init__(self):
        """Initialize start_location CreateRulesCommand instance."""
        super().__init__()
        self.add_preconditions([CreateConstraintsCommand])
        self.target = 'rules'

    def work(self, problem: Problem) -> None:
        """Create start_location list of rules in the problem instance.

        This function generates rules by traversing the constraint tree and calling the `rules`
        property on each constraint in the constraints attribute. The rules are then de-duplicated,
        sorted, and stored in the target attribute within the problem instance.

        Args:
            problem (Problem): The problem instance where the rules will be created.

        Raises:
            CommandError: If the board is not created.
        """
        super().work(problem)
        if problem.constraints is None:
            raise CommandError(f'Constrains must be created before {self.name}.')

        problem.rules = [
            Rule(name=rule.name, text=rule.text, rank=rule.rank)
            for rule in problem.constraints.sorted_unique_rules
        ]
