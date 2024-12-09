"""CreateRulesCommand."""
from src.commands.key_type import KeyType
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from src.items.item import Item


class CreateRulesCommand(SimpleCommand):
    """Command for creating start list of rules in the problem instance."""

    def __init__(self, constraints: str = 'constraints', target: str = 'rules'):
        """Initialize start CreateRulesCommand instance.

        Args:
            constraints (str): The attribute in the problem containing constraints used to generate rules.
            target (str): The attribute name in the problem where the generated rules will be stored.
        """
        super().__init__()
        self.constraints: str = constraints
        self.target: str = target
        self.input_types: list[KeyType] = [
            KeyType(self.constraints, Item),
        ]
        self.output_types: list[KeyType] = [
            KeyType(self.target, list),
        ]

    def work(self, problem: Problem) -> None:
        """Create start list of rules in the problem instance.

        This function generates rules by traversing the constraint tree and calling the `rules`
        property on each constraint in the constraints attribute. The rules are then de-duplicated,
        sorted, and stored in the target attribute within the problem instance.

        Args:
            problem (Problem): The problem instance where the rules will be created.
        """
        super().work(problem)
        problem[self.target] = [
            {'name': rule.name, 'text': rule.text}
            for rule in problem[self.constraints].sorted_unique_rules
        ]
