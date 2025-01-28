"""BookkeepingCommand."""
from src.commands.create_constraints_command import CreateConstraintsCommand
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class BookkeepingCommand(SimpleCommand):
    """Command to handle bookkeeping of value_list for cells."""

    def __init__(self):
        """Initialize the BookkeepingCommand."""
        super().__init__()
        self.add_preconditions([CreateConstraintsCommand])

    def work(self, problem: Problem) -> None:
        """Execute the bookkeeping operation.

        Args:
            problem (Problem): The problem on which to perform bookkeeping.
        """
        super().work(problem)
        problem.constraints.bookkeeping()
        problem.bookkeeping_unique = problem.constraints.bookkeeping_unique()
